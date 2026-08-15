#!/usr/bin/env python3
"""
DGX Spark Monitor MCP Server

Dual CLI + MCP interface for monitoring GPU, memory, Docker, and conda
on the DGX Spark (GB10 Grace Blackwell).

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import subprocess
import shutil
import tempfile
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("dgx-monitor", "1.0.0")


def _run(cmd: list[str], timeout: int = 30) -> dict:
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
        return {"returncode": -1, "stdout": "", "stderr": f"Command timed out after {timeout}s"}
    except FileNotFoundError:
        return {"returncode": -1, "stdout": "", "stderr": f"Command not found: {cmd[0]}"}
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e)}


# --- GPU Tools ---

@server.tool()
def gpu_status() -> str:
    """Get current GPU utilization, memory usage, temperature, and power.
    Returns a formatted summary of nvidia-smi output.

    NOTE: On GB10 DGX Spark, GPU memory is unified with system RAM (128GB LPDDR5X).
    nvidia-smi reports [N/A] for memory fields. This tool falls back to system
    memory (free -h) when GPU memory queries return [N/A].
    """
    r = _run([
        "nvidia-smi",
        "--query-gpu=name,compute_cap,memory.total,memory.used,memory.free,"
        "utilization.gpu,utilization.memory,temperature.gpu,power.draw,power.limit,clocks.sm,clocks.mem",
        "--format=csv,noheader,nounits",
    ])
    if r["returncode"] != 0:
        return f"Error getting GPU status: {r['stderr']}"
    parts = [p.strip() for p in r["stdout"].split(",")]
    if len(parts) < 12:
        return f"Unexpected nvidia-smi output: {r['stdout']}"

    # Handle GB10 unified memory: nvidia-smi returns [N/A] for memory fields
    mem_total = parts[2]
    mem_used = parts[3]
    mem_free = parts[4]
    mem_note = ""
    if "[N/A]" in (mem_total, mem_used, mem_free):
        # Fall back to system memory (unified on GB10)
        r2 = _run(["free", "-h"])
        if r2["returncode"] == 0:
            lines = r2["stdout"].split("\n")
            mem_line = [l for l in lines if l.startswith("Mem:")]
            if mem_line:
                mem_parts = mem_line[0].split()
                mem_total = f"{mem_parts[1]} (unified)"
                mem_used = f"{mem_parts[2]} (unified)"
                mem_free = f"{mem_parts[3]} (unified)"
                mem_note = "\nNote: GB10 uses unified LPDDR5X memory. See system_memory for details."

    return (
        f"GPU: {parts[0]}\n"
        f"Compute Capability: {parts[1]}\n"
        f"Memory: {mem_total} total, {mem_used} used, {mem_free} free{mem_note}\n"
        f"Utilization: GPU {parts[5]}%, Memory {parts[6]}%\n"
        f"Temperature: {parts[7]}C\n"
        f"Power: {parts[8]}W / {parts[9]}W limit\n"
        f"Clocks: SM {parts[10]}MHz, Mem {parts[11]}MHz"
    )


@server.tool()
def gpu_processes() -> str:
    """List all processes using GPU memory with PID, process name, and memory.
    Useful for finding what's consuming GPU memory.
    """
    r = _run([
        "nvidia-smi",
        "--query-compute-apps=pid,process_name,used_memory",
        "--format=csv,noheader",
    ])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    if not r["stdout"].strip():
        return "No processes are currently using GPU memory."
    lines = r["stdout"].strip().split("\n")
    result = ["PID    | Process Name                    | Memory (MiB)", "-" * 60]
    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            result.append(f"{parts[0]:6} | {parts[1]:30} | {parts[2]}")
    return "\n".join(result)


@server.tool()
def kill_gpu_process(
    pid: Annotated[int, "PID of the process to kill"],
    force: Annotated[bool, "Use SIGKILL instead of SIGTERM"] = False,
) -> str:
    """Kill a process that is using GPU memory. Use gpu_processes first to find the PID.

    Defaults to force=False (sends SIGTERM first). Use force=True for SIGKILL.
    """
    sig = "SIGKILL" if force else "SIGTERM"
    flag = "-9" if force else "-15"
    r = _run(["kill", flag, str(pid)])
    if r["returncode"] == 0:
        return f"Sent {sig} to PID {pid}. Verify with gpu_processes."
    return f"Failed to kill PID {pid}: {r['stderr']}"


@server.tool()
def top_gpu_processes(
    limit: Annotated[int, "Number of top processes to return (default: 10)"] = 10,
) -> str:
    """List the top GPU memory-consuming processes sorted by used_memory descending."""
    r = _run([
        "nvidia-smi",
        "--query-compute-apps=pid,process_name,used_memory",
        "--format=csv,noheader",
    ])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    if not r["stdout"].strip():
        return "No processes are currently using GPU memory."

    entries = []
    for line in r["stdout"].strip().split("\n"):
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            mem_str = parts[2]
            try:
                mem_val = int(mem_str.split()[0])
            except Exception:
                mem_val = 0
            entries.append((mem_val, parts[0], parts[1], mem_str))

    if not entries:
        return "No GPU processes parsed."

    entries.sort(key=lambda x: x[0], reverse=True)
    top = entries[:limit]
    result = [
        f"Top {len(top)} GPU processes by memory",
        "-" * 60,
        "PID    | Process Name                    | Memory",
    ]
    for _, pid, name, mem in top:
        result.append(f"{pid:6} | {name:30} | {mem}")
    return "\n".join(result)


@server.tool()
def nvdec_status() -> str:
    """Return NVDEC/NVENC encoder session stats (session count, average FPS, average latency)."""
    # Some drivers report latency as averageLatencyMs, others as averageLatency (us).
    queries = [
        "encoder.stats.sessionCount,encoder.stats.averageFps,encoder.stats.averageLatencyMs",
        "encoder.stats.sessionCount,encoder.stats.averageFps,encoder.stats.averageLatency",
    ]
    r = None
    for q in queries:
        r = _run(["nvidia-smi", f"--query-gpu={q}", "--format=csv"])
        if r["returncode"] == 0:
            break
        combined = (r["stdout"] + " " + r["stderr"]).lower()
        if "not a valid field" in combined:
            continue
        break
    if r is None or r["returncode"] != 0:
        return f"Error: {r['stderr'] or r['stdout'] if r else 'unknown'}"

    lines = [l for l in r["stdout"].strip().split("\n") if l.strip()]
    if not lines:
        return "No encoder stats available."

    header = [h.strip() for h in lines[0].split(",")]
    rows = lines[1:]
    if not rows:
        return "No encoder stats returned."

    out = ["NVDEC/NVENC encoder stats:"]
    for i, line in enumerate(rows):
        parts = [p.strip() for p in line.split(",")]
        out.append(f"GPU {i}:")
        for h, v in zip(header, parts):
            if v == "[N/A]":
                v = "N/A"
            out.append(f"  {h}: {v}")
    return "\n".join(out)


# --- System Memory Tools ---

@server.tool()
def system_memory() -> str:
    """Get system RAM usage. Critical on DGX Spark because memory is unified
    (GPU and CPU share 128GB LPDDR5X). High system memory usage can limit GPU allocations.
    """
    r = _run(["free", "-h"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    r2 = _run(["cat", "/proc/meminfo"])
    meminfo_lines = []
    if r2["returncode"] == 0:
        for line in r2["stdout"].split("\n")[:10]:
            meminfo_lines.append(line)
    return f"{r['stdout']}\n\n--- /proc/meminfo (first 10 lines) ---\n" + "\n".join(meminfo_lines)


@server.tool()
def disk_usage(
    path: Annotated[
        str,
        "Comma-separated directory paths to check (e.g. '/home,/tmp'). If empty, checks /home, /, /tmp, and /var/lib/docker.",
    ] = "",
) -> str:
    """Check disk space for one or more paths. If no path is provided, checks common DGX locations.

    Useful before large downloads or dataset generation.
    """
    if not path.strip():
        paths = ["/home", "/", "/tmp", "/var/lib/docker"]
    else:
        paths = [p.strip() for p in path.split(",") if p.strip()]
    if not paths:
        return "No valid paths provided."

    lines = ["Path         | Filesystem    | Size | Used | Avail | Use% | Mounted on", "-" * 72]
    for p in paths:
        r = _run(["df", "-h", "--output=source,size,used,avail,pcent,target", p])
        if r["returncode"] != 0:
            lines.append(f"{p:12} | error: {r['stderr']}")
            continue
        rows = [l for l in r["stdout"].strip().split("\n") if l.strip()]
        if len(rows) < 2:
            lines.append(f"{p:12} | no output")
            continue
        parts = rows[-1].split()
        if len(parts) >= 6:
            fs, size, used, avail, usep, mount = parts[:6]
            lines.append(f"{p:12} | {fs:13} | {size:>4} | {used:>4} | {avail:>5} | {usep:>4} | {mount}")
        else:
            lines.append(f"{p:12} | {rows[-1]}")
    return "\n".join(lines)


# --- Docker Tools ---

@server.tool()
def docker_ps() -> str:
    """List running Docker containers with their ports and images."""
    r = _run([
        "docker", "ps", "--format",
        "table {{.ID}}\t{{.Names}}\t{{.Status}}\t{{.Ports}}\t{{.Image}}",
    ])
    if r["returncode"] != 0:
        return f"Error (is Docker running?): {r['stderr']}"
    return r["stdout"] if r["stdout"].strip() else "No Docker containers running."


@server.tool()
def docker_logs(
    container: Annotated[str, "Container name or ID"],
    lines: Annotated[int, "Number of recent log lines to show"] = 50,
) -> str:
    """Get recent logs from a Docker container."""
    r = _run(["docker", "logs", "--tail", str(lines), container])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    output = r["stdout"]
    if r["stderr"]:
        output += f"\n--- stderr ---\n{r['stderr']}"
    return output if output.strip() else "No logs."


@server.tool()
def docker_gpu_stats() -> str:
    """Show which Docker containers are using the GPU and how much memory."""
    r = _run(["docker", "ps", "--format", "{{.Names}}"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    containers = r["stdout"].strip().split("\n") if r["stdout"].strip() else []
    if not containers:
        return "No Docker containers running."
    r2 = _run(["nvidia-smi", "--query-compute-apps=pid,process_name,used_memory", "--format=csv,noheader"])
    gpu_procs = {}
    if r2["returncode"] == 0 and r2["stdout"].strip():
        for line in r2["stdout"].strip().split("\n"):
            parts = [p.strip() for p in line.split(",")]
            if len(parts) >= 3:
                gpu_procs[parts[0]] = {"name": parts[1], "mem": parts[2]}
    results = []
    for name in containers:
        r3 = _run(["docker", "inspect", "--format", "{{.State.Pid}}", name])
        if r3["returncode"] == 0 and r3["stdout"].strip():
            pid = r3["stdout"].strip()
            if pid in gpu_procs:
                results.append(f"  {name}: PID {pid} -> GPU {gpu_procs[pid]['mem']} ({gpu_procs[pid]['name']})")
            else:
                results.append(f"  {name}: PID {pid} -> no GPU usage")
    return "Docker GPU usage:\n" + "\n".join(results)


# --- Conda Tools ---

@server.tool()
def conda_envs() -> str:
    """List all conda environments with their paths."""
    r = _run(["conda", "env", "list"])
    if r["returncode"] != 0:
        r = _run(["mamba", "env", "list"])
        if r["returncode"] != 0:
            return f"Error: conda not found. {r['stderr']}"
    return r["stdout"]


@server.tool()
def conda_packages(
    env: Annotated[str, "Conda environment name (e.g., '3d_recon', 'base')"] = "base",
    pip: Annotated[bool, "Also show pip-installed packages"] = False,
) -> str:
    """List packages installed in a conda environment. Use pip=True to also show pip packages."""
    r = _run(["conda", "list", "-n", env])
    if r["returncode"] != 0:
        return f"Error listing packages in '{env}': {r['stderr']}"
    output = r["stdout"]
    if pip:
        r2 = _run(["conda", "run", "-n", env, "pip", "list", "--format=columns"])
        if r2["returncode"] == 0:
            output += f"\n--- pip packages in {env} ---\n{r2['stdout']}"
    return output


# --- CUDA / Compilation Tools ---

@server.tool()
def cuda_info() -> str:
    """Get CUDA version, nvcc version, and driver version."""
    results = []
    r = _run(["nvidia-smi", "--query-gpu=driver_version", "--format=csv,noheader"])
    results.append(f"Driver: {r['stdout']}" if r["returncode"] == 0 else f"Driver: {r['stderr']}")
    r = _run(["nvcc", "--version"])
    if r["returncode"] == 0:
        for line in r["stdout"].split("\n"):
            if "release" in line.lower():
                results.append(f"nvcc: {line.strip()}")
                break
    else:
        results.append("nvcc: not found")
    cuda_path = os.environ.get("CUDA_HOME", "/usr/local/cuda")
    results.append(f"CUDA_HOME: {cuda_path}")
    r = _run(["nvidia-smi", "--query-gpu=compute_cap", "--format=csv,noheader"])
    results.append(f"Compute Capability: {r['stdout']}" if r["returncode"] == 0 else f"Compute Capability: {r['stderr']}")
    return "\n".join(results)


@server.tool()
def compile_cuda(
    source: Annotated[str, "Path to .cu source file"],
    output: Annotated[str, "Output binary path"],
    arch: Annotated[str, "Compute architecture (default: sm_121 for GB10)"] = "sm_121",
    extra_flags: Annotated[str, "Extra nvcc flags (e.g., '-O2 -lineinfo')"] = "-O2 -lineinfo",
    include_dirs: Annotated[str, "Comma-separated include directories"] = "",
    libraries: Annotated[str, "Comma-separated libraries to link (e.g., 'cudart,cublas')"] = "cudart",
) -> str:
    """Compile a CUDA .cu file with nvcc using correct flags for the target architecture.
    Defaults to sm_121 (GB10 DGX Spark) with -lineinfo for profiling support.
    """
    cmd = ["nvcc", f"-arch={arch}"]
    if extra_flags:
        cmd.extend(extra_flags.split())
    if include_dirs:
        for d in include_dirs.split(","):
            cmd.extend(["-I", d.strip()])
    if libraries:
        for lib in libraries.split(","):
            cmd.extend(["-l", lib.strip()])
    cmd.extend(["-o", output, source])
    r = _run(cmd, timeout=120)
    if r["returncode"] == 0:
        return f"Compiled successfully: {output}\nCommand: {' '.join(cmd)}"
    return f"Compilation failed:\nCommand: {' '.join(cmd)}\nstderr: {r['stderr']}"


BANDWIDTH_CU = r"""
#include <cuda_runtime.h>
#include <iostream>
#include <iomanip>
#include <cstring>
#include <vector>

int main(int argc, char** argv) {
    const char* kind = argc > 1 ? argv[1] : "device_to_device";
    std::vector<size_t> sizes = {64*1024*1024, 256*1024*1024, 1024*1024*1024};
    int iterations = 10;
    cudaMemcpyKind k = cudaMemcpyDeviceToDevice;
    bool host_src = false, host_dst = false;

    if (strcmp(kind, "host_to_device") == 0) { k = cudaMemcpyHostToDevice; host_src = true; }
    else if (strcmp(kind, "device_to_host") == 0) { k = cudaMemcpyDeviceToHost; host_dst = true; }
    else if (strcmp(kind, "device_to_device") != 0) {
        std::cerr << "Unknown kind: " << kind << std::endl;
        return 1;
    }

    std::cout << "Kind: " << kind << std::endl;
    std::cout << "Size (MiB)\tGB/s\tms/iter" << std::endl;

    for (size_t size : sizes) {
        unsigned char *d_src = nullptr, *d_dst = nullptr, *h_src = nullptr, *h_dst = nullptr;
        cudaMalloc(&d_src, size);
        cudaMalloc(&d_dst, size);
        if (host_src) { cudaMallocHost(&h_src, size); std::memset(h_src, 0xAB, size); }
        if (host_dst) { cudaMallocHost(&h_dst, size); }

        if (!host_src) {
            cudaMemset(d_src, 0xAB, size);
        }

        // Warm-up
        for (int i = 0; i < 3; ++i) {
            if (host_src) cudaMemcpy(d_dst, h_src, size, k);
            else if (host_dst) cudaMemcpy(h_dst, d_src, size, k);
            else cudaMemcpy(d_dst, d_src, size, k);
        }
        cudaDeviceSynchronize();

        cudaEvent_t start, stop;
        cudaEventCreate(&start);
        cudaEventCreate(&stop);
        cudaEventRecord(start);
        for (int i = 0; i < iterations; ++i) {
            if (host_src) cudaMemcpy(d_dst, h_src, size, k);
            else if (host_dst) cudaMemcpy(h_dst, d_src, size, k);
            else cudaMemcpy(d_dst, d_src, size, k);
        }
        cudaEventRecord(stop);
        cudaEventSynchronize(stop);

        float ms = 0.0f;
        cudaEventElapsedTime(&ms, start, stop);

        double total_bytes = double(size) * iterations;
        double seconds = ms / 1000.0;
        double gbps = (total_bytes / seconds) / 1e9;
        double ms_per = ms / iterations;

        std::cout << std::fixed << std::setprecision(1);
        std::cout << (size / (1024*1024)) << "\t" << gbps << "\t" << ms_per << std::endl;

        if (host_src) cudaFreeHost(h_src);
        if (host_dst) cudaFreeHost(h_dst);
        cudaFree(d_src);
        cudaFree(d_dst);
        cudaEventDestroy(start);
        cudaEventDestroy(stop);
    }
    return 0;
}
"""


@server.tool()
def bandwidth_test(
    kind: Annotated[
        str,
        "Memcpy kind to benchmark: 'device_to_device', 'host_to_device', or 'device_to_host' (default: device_to_device)",
    ] = "device_to_device",
) -> str:
    """Generate, compile, and run a tiny CUDA bandwidth benchmark. Requires nvcc and a GPU."""
    if not shutil.which("nvcc"):
        return "Error: nvcc not found in PATH."
    if kind not in ("device_to_device", "host_to_device", "device_to_host"):
        return "Error: kind must be one of device_to_device, host_to_device, device_to_host."

    with tempfile.TemporaryDirectory() as tmpdir:
        source = os.path.join(tmpdir, "bandwidth.cu")
        binary = os.path.join(tmpdir, "bandwidth")
        with open(source, "w") as f:
            f.write(BANDWIDTH_CU)

        r = _run(["nvcc", f"-arch=sm_121", "-O2", "-o", binary, source], timeout=120)
        if r["returncode"] != 0:
            return f"Compilation failed:\n{r['stderr']}"

        r2 = _run([binary, kind], timeout=120)
        if r2["returncode"] != 0:
            return f"Benchmark run failed:\n{r2['stderr']}"

    return f"CUDA bandwidth test ({kind}):\n{r2['stdout']}"


# --- CLI Mode ---

TOOLS = {
    "gpu_status": gpu_status,
    "gpu_processes": gpu_processes,
    "top_gpu_processes": top_gpu_processes,
    "kill_gpu_process": kill_gpu_process,
    "system_memory": system_memory,
    "disk_usage": disk_usage,
    "docker_ps": docker_ps,
    "docker_logs": docker_logs,
    "docker_gpu_stats": docker_gpu_stats,
    "conda_envs": conda_envs,
    "conda_packages": conda_packages,
    "cuda_info": cuda_info,
    "compile_cuda": compile_cuda,
    "nvdec_status": nvdec_status,
    "bandwidth_test": bandwidth_test,
}


def cli_mode():
    """Handle CLI invocation: python3 server.py --cli <tool> [--args ...]"""
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

    # Parse simple --key value args from sys.argv[3:]
    kwargs = {}
    args = sys.argv[3:]
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                val = args[i + 1]
                # Try to parse as bool/int/float
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
