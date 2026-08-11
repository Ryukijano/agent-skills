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
    force: Annotated[bool, "Use SIGKILL instead of SIGTERM"] = True,
) -> str:
    """Kill a process that is using GPU memory. Use gpu_processes first to find the PID."""
    sig = "SIGKILL" if force else "SIGTERM"
    flag = "-9" if force else "-15"
    r = _run(["kill", flag, str(pid)])
    if r["returncode"] == 0:
        return f"Sent {sig} to PID {pid}. Verify with gpu_processes."
    return f"Failed to kill PID {pid}: {r['stderr']}"


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
    path: Annotated[str, "Directory path to check (default: /home)"] = "/home",
) -> str:
    """Check disk space on a given path. Useful before large downloads or dataset generation."""
    r = _run(["df", "-h", path])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


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
                results.append(f"  {name}: PID {pid} -> GPU {gpu_procs[pid]['mem']}MiB ({gpu_procs[pid]['name']})")
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


# --- CLI Mode ---

TOOLS = {
    "gpu_status": gpu_status,
    "gpu_processes": gpu_processes,
    "system_memory": system_memory,
    "disk_usage": disk_usage,
    "docker_ps": docker_ps,
    "docker_logs": docker_logs,
    "docker_gpu_stats": docker_gpu_stats,
    "conda_envs": conda_envs,
    "conda_packages": conda_packages,
    "cuda_info": cuda_info,
    "compile_cuda": compile_cuda,
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
