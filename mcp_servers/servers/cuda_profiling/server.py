#!/usr/bin/env python3
"""
CUDA Profiling MCP Server

Wraps nsys, ncu, compute-sanitizer, cuobjdump as MCP tools so any agent
can profile kernels, check correctness, and inspect SASS/PTX without
writing the commands each time.

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import shlex
import subprocess
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("cuda-profiling", "1.0.0")


import shutil


def _find_tool(name: str) -> str | None:
    """Find a CUDA tool binary, checking common paths."""
    path = shutil.which(name)
    if path:
        return path
    cuda_home = os.environ.get("CUDA_HOME", "/usr/local/cuda")
    candidates = [
        os.path.join(cuda_home, "bin", name),
        os.path.join(cuda_home, "Nsight-Compute-2025.2", name),
        f"/usr/local/cuda/bin/{name}",
    ]
    for c in candidates:
        if os.path.isfile(c):
            return c
    return None


def _run(cmd: list[str], timeout: int = 300) -> dict:
    """Run a shell command and return structured output."""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout
        )
        return {
            "returncode": result.returncode,
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip(),
        }
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": f"Timed out after {timeout}s"}
    except FileNotFoundError:
        return {"returncode": -1, "stdout": "", "stderr": f"Not found: {cmd[0]}"}
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e)}


def _split_command(command: str | list[str]) -> list[str]:
    """Convert a command string or list into a safe argv list.

    Supports paths with spaces when the command is shell-quoted.
    """
    if isinstance(command, list):
        return [str(c) for c in command]
    if isinstance(command, str):
        return shlex.split(command)
    raise TypeError("command must be a string or list of strings")


# --- Nsight Systems Tools ---

@server.tool()
def profile_nsys(
    command: Annotated[str | list[str], "Command to profile (e.g., 'python train.py' or './my_kernel')"],
    output: Annotated[str, "Output report file path prefix (default: /tmp/nsys_profile)"] = "/tmp/nsys_profile",
    capture_cuda: Annotated[bool, "Capture CUDA API calls and kernels"] = True,
    capture_nvtx: Annotated[bool, "Capture NVTX ranges"] = True,
    capture_osrt: Annotated[bool, "Capture OS runtime calls"] = False,
    delay: Annotated[float, "Delay before capture in seconds (0 = immediate)"] = 0,
    duration: Annotated[float, "Capture duration in seconds (0 = until command exits)"] = 0,
    stats: Annotated[bool, "Generate stats report after profiling"] = True,
) -> str:
    """Run Nsight Systems profiling on a command. Returns the report path and key stats.
    Use this for timeline-level profiling (kernel launches, API calls, CPU-GPU overlap).
    """
    nsys = _find_tool("nsys")
    if not nsys:
        return "Error: nsys not found. Install Nsight Systems or set CUDA_HOME."

    cmd = [nsys, "profile", "-o", output, "--force-overwrite=true"]

    trace = []
    if capture_cuda:
        trace.append("cuda")
    if capture_nvtx:
        trace.append("nvtx")
    if capture_osrt:
        trace.append("osrt")
    if trace:
        cmd.append(f"--trace={','.join(trace)}")
    else:
        cmd.append("--trace=none")

    # Keep the default capture range; --duration handles time-bounded capture.
    cmd.append("--capture-range=none")

    if delay > 0:
        cmd.append(f"--delay={delay}")
    if duration > 0:
        cmd.append(f"--duration={duration}")

    cmd.append("--stats=true" if stats else "--stats=false")
    cmd.extend(_split_command(command))

    r = _run(cmd, timeout=600)

    # Nsight Systems 2025.3 writes .nsys-rep + .sqlite; older versions used
    # .qdrep + .qdsqlite. Prefer whatever actually exists, otherwise default
    # to the modern extensions.
    rep_ext = next((e for e in (".nsys-rep", ".qdrep") if os.path.isfile(output + e)), ".nsys-rep")
    sql_ext = next((e for e in (".sqlite", ".qdsqlite") if os.path.isfile(output + e)), ".sqlite")
    report_path = output + rep_ext
    sqlite_path = output + sql_ext

    result_lines = [
        f"nsys profile completed (exit code: {r['returncode']})",
        f"Report: {report_path}",
        f"SQLite: {sqlite_path}",
    ]
    if r["stdout"]:
        result_lines.append(f"\n--- stdout (last 500 chars) ---\n{r['stdout'][-500:]}")
    if r["stderr"]:
        result_lines.append(f"\n--- stderr (last 500 chars) ---\n{r['stderr'][-500:]}")
    return "\n".join(result_lines)


@server.tool()
def parse_nsys_stats(
    report: Annotated[str, "Path to .nsys-rep, .sqlite, or legacy .qdrep file"],
    report_type: Annotated[str, "Report type: cuda_api_sum, cuda_gpu_kern_sum, cuda_gpu_mem_size_sum, nvtx_sum"] = "cuda_gpu_kern_sum",
) -> str:
    """Parse an nsys report and return summary statistics. Use after profile_nsys."""
    nsys = _find_tool("nsys")
    if not nsys:
        return "Error: nsys not found."

    cmd = [nsys, "stats"]
    if report.lower().endswith(".nsys-rep"):
        # Re-export SQLite to avoid "existing SQLite older than input" failures.
        cmd.append("--force-export=true")
    cmd.extend(["--report", report_type, "--format", "csv", report])

    r = _run(cmd, timeout=120)
    if r["returncode"] != 0:
        return f"Error parsing report: {r['stderr']}\n\n--- stdout ---\n{r['stdout'][-2000:]}"

    lines = r["stdout"].split("\n")
    if len(lines) > 50:
        return "\n".join(lines[:50]) + f"\n... ({len(lines) - 50} more lines)"
    return r["stdout"]


# Register an alias so both `parse_nsys_stats` and `parse_nsys_report` work.
server.add_tool(parse_nsys_stats, name="parse_nsys_report")


# --- Nsight Compute Tools ---

@server.tool()
def profile_ncu(
    command: Annotated[str | list[str], "Command to profile (e.g., 'python train.py' or './my_kernel')"],
    output: Annotated[str, "Output .ncu-rep file path (default: /tmp/ncu_profile)"] = "/tmp/ncu_profile",
    metric_set: Annotated[str, "Metric set: full, basic, roofline, speedup"] = "full",
    kernel_filter: Annotated[str, "Regex to filter kernel names (empty = all kernels)"] = "",
    launch_count: Annotated[int, "Number of kernel launches to profile (0 = all)"] = 0,
    target_processes: Annotated[str, "Target processes: all, current"] = "all",
) -> str:
    """Run Nsight Compute kernel profiling. Returns the report path.
    Use this for per-kernel metrics (occupancy, stall reasons, memory throughput).
    WARNING: ncu with --set full is slow (replays kernels). Use launch_count to limit.
    """
    ncu = _find_tool("ncu")
    if not ncu:
        return "Error: ncu not found. Install Nsight Compute or set CUDA_HOME."
    cmd = [ncu, "--set", metric_set, "-o", output, "--force-overwrite"]
    if kernel_filter:
        cmd.extend(["-k", kernel_filter])
    if launch_count > 0:
        cmd.extend(["-c", str(launch_count)])
    cmd.extend([f"--target-processes={target_processes}"])
    cmd.extend(_split_command(command))
    r = _run(cmd, timeout=600)
    result_lines = [f"ncu profile completed (exit code: {r['returncode']})",
                    f"Report: {output}.ncu-rep"]
    if r["stdout"]:
        result_lines.append(f"\n--- stdout (last 500 chars) ---\n{r['stdout'][-500:]}")
    if r["stderr"]:
        # ncu prints progress to stderr
        result_lines.append(f"\n--- stderr (last 500 chars) ---\n{r['stderr'][-500:]}")
    return "\n".join(result_lines)


@server.tool()
def parse_ncu_report(
    report: Annotated[str, "Path to .ncu-rep file"],
    metric: Annotated[str, "Specific metric to extract (empty = summary)"] = "",
    csv_output: Annotated[bool, "Output as CSV"] = True,
) -> str:
    """Parse an ncu report and extract key metrics. Use after profile_ncu."""
    ncu = _find_tool("ncu")
    if not ncu:
        return "Error: ncu not found."
    cmd = [ncu, "--import", report]
    if csv_output:
        cmd.extend(["--csv", "--page", "details"])
    if metric:
        cmd.extend(["--metrics", metric])
    r = _run(cmd, timeout=120)
    if r["returncode"] != 0:
        return f"Error parsing report: {r['stderr']}\n\n--- stdout ---\n{r['stdout'][-2000:]}"
    lines = r["stdout"].split("\n")
    if len(lines) > 80:
        return "\n".join(lines[:80]) + f"\n... ({len(lines) - 80} more lines)"
    return r["stdout"]


# --- Compute Sanitizer Tools ---

@server.tool()
def memcheck(
    command: Annotated[str | list[str], "Command to check (e.g., './my_kernel')"],
) -> str:
    """Run compute-sanitizer memcheck to detect memory errors (out-of-bounds, use-after-free, etc.).
    This is the GPU equivalent of Valgrind memcheck.
    """
    cs = _find_tool("compute-sanitizer")
    if not cs:
        return "Error: compute-sanitizer not found. Set CUDA_HOME."
    cmd = [cs, "--tool", "memcheck"]
    cmd.extend(_split_command(command))
    r = _run(cmd, timeout=300)
    result_lines = [f"memcheck completed (exit code: {r['returncode']})"]
    if r["returncode"] == 0 and not r["stderr"]:
        result_lines.append("No memory errors detected.")
    if r["stdout"]:
        result_lines.append(f"\n--- stdout ---\n{r['stdout'][-1000:]}")
    if r["stderr"]:
        result_lines.append(f"\n--- stderr ---\n{r['stderr'][-1000:]}")
    return "\n".join(result_lines)


@server.tool()
def racecheck(
    command: Annotated[str | list[str], "Command to check"],
) -> str:
    """Run compute-sanitizer racecheck to detect data races in CUDA kernels.
    Use this when debugging intermittent wrong results from shared memory or atomics.
    """
    cs = _find_tool("compute-sanitizer")
    if not cs:
        return "Error: compute-sanitizer not found."
    cmd = [cs, "--tool", "racecheck"]
    cmd.extend(_split_command(command))
    r = _run(cmd, timeout=300)
    result_lines = [f"racecheck completed (exit code: {r['returncode']})"]
    if r["stdout"]:
        result_lines.append(f"\n--- stdout ---\n{r['stdout'][-1000:]}")
    if r["stderr"]:
        result_lines.append(f"\n--- stderr ---\n{r['stderr'][-1000:]}")
    return "\n".join(result_lines)


@server.tool()
def initcheck(
    command: Annotated[str | list[str], "Command to check"],
) -> str:
    """Run compute-sanitizer initcheck to detect use of uninitialized memory."""
    cs = _find_tool("compute-sanitizer")
    if not cs:
        return "Error: compute-sanitizer not found."
    cmd = [cs, "--tool", "initcheck"]
    cmd.extend(_split_command(command))
    r = _run(cmd, timeout=300)
    result_lines = [f"initcheck completed (exit code: {r['returncode']})"]
    if r["stdout"]:
        result_lines.append(f"\n--- stdout ---\n{r['stdout'][-1000:]}")
    if r["stderr"]:
        result_lines.append(f"\n--- stderr ---\n{r['stderr'][-1000:]}")
    return "\n".join(result_lines)


# --- SASS / PTX Inspection Tools ---

@server.tool()
def dump_sass(
    binary: Annotated[str, "Path to compiled CUDA binary (.cubin or executable)"],
    kernel: Annotated[str, "Kernel name regex filter (empty = all kernels)"] = "",
) -> str:
    """Dump SASS (Streaming Assembler) instructions for compiled CUDA kernels.
    Use this to verify what instructions the compiler actually generated.
    """
    cuobjdump = _find_tool("cuobjdump")
    if not cuobjdump:
        return "Error: cuobjdump not found."
    cmd = [cuobjdump, "--dump-sass"]
    if kernel:
        cmd.extend(["--function", kernel])
    cmd.append(binary)
    r = _run(cmd, timeout=60)
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    lines = r["stdout"].split("\n")
    if len(lines) > 100:
        return "\n".join(lines[:100]) + f"\n... ({len(lines) - 100} more lines)"
    return r["stdout"]


@server.tool()
def dump_ptx(
    binary: Annotated[str, "Path to compiled CUDA binary (.cubin or executable)"],
    kernel: Annotated[str, "Kernel name regex filter (empty = all kernels)"] = "",
) -> str:
    """Dump PTX (Parallel Thread Execution) intermediate representation.
    PTX is the virtual instruction set between CUDA C++ and SASS.
    """
    cuobjdump = _find_tool("cuobjdump")
    if not cuobjdump:
        return "Error: cuobjdump not found."
    cmd = [cuobjdump, "--dump-ptx"]
    if kernel:
        cmd.extend(["--function", kernel])
    cmd.append(binary)
    r = _run(cmd, timeout=60)
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    lines = r["stdout"].split("\n")
    if len(lines) > 100:
        return "\n".join(lines[:100]) + f"\n... ({len(lines) - 100} more lines)"
    return r["stdout"]


# --- GPU Info & Kernel Compilation ---

@server.tool()
def gpu_info() -> str:
    """Query GPU information (name, compute capability, memory, PCI bus, driver version)."""
    nvidia_smi = _find_tool("nvidia-smi")
    if not nvidia_smi:
        return "Error: nvidia-smi not found."
    r = _run(
        [nvidia_smi, "--query-gpu=name,compute_cap,memory.total,pci.bus_id,driver_version", "--format=csv"],
        timeout=60,
    )
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def compile_kernel(
    source: Annotated[str, "Path to the .cu source file"],
    output: Annotated[str, "Path for the compiled binary (default: /tmp/cuda_kernel.out)"] = "/tmp/cuda_kernel.out",
    arch: Annotated[str, "CUDA architecture (e.g. sm_121)"] = "sm_121",
    use_fast_math: Annotated[bool, "Add --use_fast_math"] = False,
    extra_flags: Annotated[str, "Extra nvcc flags as a shell-quoted string"] = "",
) -> str:
    """Compile a CUDA kernel with nvcc. Returns the binary path and compile output."""
    nvcc = _find_tool("nvcc")
    if not nvcc:
        return "Error: nvcc not found. Install CUDA toolkit or set CUDA_HOME."
    if not os.path.isfile(source):
        return f"Error: source file not found: {source}"

    cmd = [nvcc, f"-arch={arch}", "-O2", "-lineinfo", "-o", output, source]
    if use_fast_math:
        cmd.append("--use_fast_math")
    if extra_flags:
        cmd.extend(shlex.split(extra_flags))

    r = _run(cmd, timeout=300)
    result_lines = [
        f"nvcc completed (exit code: {r['returncode']})",
        f"Binary: {output}",
    ]
    if r["stdout"]:
        result_lines.append(f"\n--- stdout ---\n{r['stdout'][-1000:]}")
    if r["stderr"]:
        result_lines.append(f"\n--- stderr ---\n{r['stderr'][-1000:]}")
    return "\n".join(result_lines)


# --- Quick Benchmark Tool ---

@server.tool()
def benchmark_kernel(
    command: Annotated[str | list[str], "Command to benchmark"],
    runs: Annotated[int, "Number of runs"] = 5,
    warmup: Annotated[int, "Number of warmup runs (not timed)"] = 1,
) -> str:
    """Run a command multiple times and report timing statistics.
    Use this for quick benchmarks. For detailed profiling, use profile_ncu.
    """
    import time
    argv = _split_command(command)
    times = []
    r = None
    for i in range(warmup + runs):
        start = time.perf_counter()
        r = _run(argv, timeout=300)
        elapsed = time.perf_counter() - start
        if i >= warmup:
            times.append(elapsed)
    if not times:
        return "No successful runs."
    mean = sum(times) / len(times)
    minimum = min(times)
    maximum = max(times)
    stdev = (sum((t - mean) ** 2 for t in times) / len(times)) ** 0.5
    return (
        f"Benchmark results ({len(times)} runs, {warmup} warmup):\n"
        f"  Mean:   {mean:.4f}s\n"
        f"  Min:    {minimum:.4f}s\n"
        f"  Max:    {maximum:.4f}s\n"
        f"  Stdev:  {stdev:.4f}s\n"
        f"  Last exit code: {r['returncode']}"
    )


# --- CLI Mode ---

TOOLS = {
    "profile_nsys": profile_nsys,
    "parse_nsys_stats": parse_nsys_stats,
    "parse_nsys_report": parse_nsys_stats,
    "profile_ncu": profile_ncu,
    "parse_ncu_report": parse_ncu_report,
    "memcheck": memcheck,
    "racecheck": racecheck,
    "initcheck": initcheck,
    "dump_sass": dump_sass,
    "dump_ptx": dump_ptx,
    "benchmark_kernel": benchmark_kernel,
    "gpu_info": gpu_info,
    "compile_kernel": compile_kernel,
}


def cli_mode():
    if len(sys.argv) < 3:
        print("Usage: python3 server.py --cli <tool_name> [--arg value ...]")
        print("\nAvailable tools:")
        for name, func in TOOLS.items():
            doc = func.__doc__ or ""
            print(f"  {name:20} - {doc.split(chr(10))[0]}")
        sys.exit(1)

    tool_name = sys.argv[2]
    if tool_name not in TOOLS:
        print(f"Unknown tool: {tool_name}")
        print(f"Available: {', '.join(TOOLS.keys())}")
        sys.exit(1)

    kwargs = {}
    args = sys.argv[3:]
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                val = args[i + 1]
                if val.lower() in ("true", "false"):
                    kwargs[key] = val.lower() == "true"
                else:
                    try:
                        kwargs[key] = int(val)
                    except ValueError:
                        try:
                            kwargs[key] = float(val)
                        except ValueError:
                            kwargs[key] = val
                i += 2
            else:
                kwargs[key] = True
                i += 1
        else:
            i += 1

    result = TOOLS[tool_name](**kwargs)
    print(result)


if __name__ == "__main__":
    if "--cli" in sys.argv:
        cli_mode()
    else:
        import asyncio
        asyncio.run(server.run_stdio_async())
