#!/usr/bin/env python3
"""
Distributed Training MCP Server

Tools for multi-GPU monitoring, DDP/FSDP diagnostics, NCCL checks,
PyTorch distributed setup, and training job management.

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import subprocess
import socket
import re
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("distributed-training", "1.0.0")


def _run(cmd: list[str], timeout: int = 60, env: dict | None = None) -> dict:
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout,
            env={**os.environ, **(env or {})}
        )
        return {"returncode": result.returncode, "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": f"Timed out after {timeout}s"}
    except FileNotFoundError:
        return {"returncode": -1, "stdout": "", "stderr": f"Not found: {cmd[0]}"}
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e)}


# --- Multi-GPU Discovery ---

@server.tool()
def list_gpus() -> str:
    """List all visible GPUs with their indices, names, compute capability, and interconnect topology.
    Works for both single-node (nvidia-smi) and detects NVLink/NVSwitch topology.
    """
    r = _run(["nvidia-smi", "-L"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    results = ["GPU List:"]
    results.append(r["stdout"])
    # Get topology
    r2 = _run(["nvidia-smi", "topo", "-m"])
    if r2["returncode"] == 0:
        results.append("\n--- Topology ---")
        results.append(r2["stdout"])
    return "\n".join(results)


@server.tool()
def gpu_interconnect() -> str:
    """Check GPU interconnect type (NVLink, NVSwitch, PCIe) and bandwidth between GPUs.
    Critical for distributed training — NVLink is 6x faster than PCIe for all-reduce.
    """
    r = _run(["nvidia-smi", "topo", "-m"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    # Parse topology matrix
    lines = r["stdout"].split("\n")
    results = ["GPU Interconnect Topology:"]
    for line in lines:
        results.append(line)
    # Check for NVLink
    has_nvlink = "NV" in r["stdout"]
    results.append(f"\nNVLink detected: {has_nvlink}")
    if not has_nvlink:
        results.append("WARNING: No NVLink detected. Multi-GPU all-reduce will use PCIe (slower).")
    return "\n".join(results)


@server.tool()
def cuda_visible_devices() -> str:
    """Show current CUDA_VISIBLE_DEVICES setting and how many GPUs are visible to CUDA."""
    env_val = os.environ.get("CUDA_VISIBLE_DEVICES", "not set (all GPUs visible)")
    r = _run(["python3", "-c", "import torch; print(f'PyTorch sees {torch.cuda.device_count()} GPU(s)')"])
    torch_info = r["stdout"] if r["returncode"] == 0 else f"PyTorch check failed: {r['stderr']}"
    return f"CUDA_VISIBLE_DEVICES: {env_val}\n{torch_info}"


# --- NCCL Diagnostics ---

@server.tool()
def nccl_test_all_reduce(
    num_gpus: Annotated[int, "Number of GPUs to test"] = 1,
    min_bytes: Annotated[str, "Minimum message size (e.g., '1B')"] = "1B",
    max_bytes: Annotated[str, "Maximum message size (e.g., '1GB')"] = "1GB",
    step_factor: Annotated[int, "Multiplicative step factor"] = 2,
) -> str:
    """Run NCCL all-reduce bandwidth test. Measures inter-GPU communication speed.
    Requires NCCL tests to be installed (build from nccl-tests repo or apt install).
    """
    # Try common paths for all_reduce_perf
    candidates = [
        os.path.join(os.environ.get("NCCL_HOME", "/usr/local/nccl"), "build", "all_reduce_perf"),
        "/usr/local/nccl-tests/build/all_reduce_perf",
        "all_reduce_perf",
    ]
    binary = None
    for c in candidates:
        check = _run(["which", c]) if not os.path.isabs(c) else {"returncode": 0 if os.path.isfile(c) else 1, "stdout": "", "stderr": ""}
        if os.path.isfile(c) if os.path.isabs(c) else check["returncode"] == 0:
            binary = c
            break
    if not binary:
        return (
            "NCCL all_reduce_perf not found. Install with:\n"
            "  git clone https://github.com/NVIDIA/nccl-tests\n"
            "  cd nccl-tests && make CUDA_HOME=/usr/local/cuda NCCL_HOME=/usr/local/nccl\n"
            "Or: apt install nccl-tests (if available)"
        )
    cmd = [binary, "-g", str(num_gpus), "-b", min_bytes, "-e", max_bytes, "-f", str(step_factor)]
    r = _run(cmd, timeout=120)
    if r["returncode"] != 0:
        return f"NCCL test failed: {r['stderr']}"
    # Trim output
    lines = r["stdout"].split("\n")
    if len(lines) > 40:
        return "\n".join(lines[:40]) + f"\n... ({len(lines) - 40} more lines)"
    return r["stdout"]


@server.tool()
def check_nccl_env() -> str:
    """Check NCCL-related environment variables and their current values.
    These control communication behavior in distributed training.
    """
    nccl_vars = [
        "NCCL_DEBUG", "NCCL_SOCKET_IFNAME", "NCCL_IB_DISABLE", "NCCL_IB_HCA",
        "NCCL_NET_GDR_LEVEL", "NCCL_P2P_DISABLE", "NCCL_SHM_DISABLE",
        "NCCL_BUFFSIZE", "NCCL_NTHREADS", "NCCL_MIN_NCHANNELS",
        "NCCL_IB_TIMEOUT", "NCCL_IB_RETRY_CNT", "NCCL_IB_SL",
        "NCCL_CUMEM_ENABLE", "NCCL_NET", "NCCL_TOPO_FILE",
    ]
    results = ["NCCL Environment Variables:"]
    found = False
    for var in nccl_vars:
        val = os.environ.get(var)
        if val is not None:
            results.append(f"  {var}={val}")
            found = True
    if not found:
        results.append("  (none set — using NCCL defaults)")
    # Also check network interfaces
    r = _run(["ip", "-o", "addr", "show"])
    if r["returncode"] == 0:
        results.append("\n--- Network Interfaces ---")
        for line in r["stdout"].split("\n")[:10]:
            results.append(f"  {line.strip()}")
    return "\n".join(results)


# --- PyTorch Distributed ---

@server.tool()
def torch_distributed_info() -> str:
    """Check PyTorch distributed training setup: version, backend, process group, world size."""
    code = """
import torch
import torch.distributed as dist
print(f"PyTorch version: {torch.__version__}")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"GPU count: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    for i in range(torch.cuda.device_count()):
        props = torch.cuda.get_device_properties(i)
        print(f"  GPU {i}: {props.name}, CC {props.major}.{props.minor}, {props.total_memory / 1e9:.1f} GB")
print(f"Distributed available: {dist.is_available()}")
print(f"Distributed initialized: {dist.is_initialized()}")
if dist.is_initialized():
    print(f"  Backend: {dist.get_backend()}")
    print(f"  World size: {dist.get_world_size()}")
    print(f"  Rank: {dist.get_rank()}")
# Check NCCL
try:
    import torch_c_nccl
    print(f"NCCL backend: available")
except:
    print(f"NCCL backend: {dist.is_nccl_available() if hasattr(dist, 'is_nccl_available') else 'check manually'}")
# Check FSDP
try:
    from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
    print("FSDP: available")
except ImportError:
    print("FSDP: not available (need PyTorch >= 1.12)")
# Check DDP
try:
    from torch.nn.parallel import DistributedDataParallel as DDP
    print("DDP: available")
except ImportError:
    print("DDP: not available")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def check_ddp_setup(
    world_size: Annotated[int, "Number of processes/GPUs"] = 1,
    backend: Annotated[str, "Communication backend: nccl, gloo, mpi"] = "nccl",
) -> str:
    """Verify DDP (DistributedDataParallel) can be initialized with the given parameters.
    Runs a quick test to check if the backend and process group work.
    """
    code = f"""
import os
import torch
import torch.distributed as dist
import torch.multiprocessing as mp

def test_ddp(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '29500'
    dist.init_process_group(backend='{backend}', rank=rank, world_size=world_size)
    if torch.cuda.is_available():
        torch.cuda.set_device(rank)
    model = torch.nn.Linear(10, 10).cuda() if torch.cuda.is_available() else torch.nn.Linear(10, 10)
    ddp = torch.nn.parallel.DistributedDataParallel(model, device_ids=[rank] if torch.cuda.is_available() else None)
    print(f"Rank {{rank}}: DDP initialized successfully with {{backend}} backend, world_size={{world_size}}")
    dist.destroy_process_group()

if __name__ == '__main__':
    mp.spawn(test_ddp, args=({world_size},), nprocs={world_size}, join=True)
    print("DDP test passed.")
"""
    r = _run(["python3", "-c", code], timeout=30)
    if r["returncode"] != 0:
        return f"DDP test failed:\n{r['stderr']}"
    return r["stdout"] or "DDP test passed (no output)"


# --- Training Job Management ---

@server.tool()
def training_jobs() -> str:
    """List running training processes (torchrun, python -m torch.distributed, accelerate, deepspeed)."""
    r = _run(["ps", "aux"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    keywords = ["torchrun", "torch.distributed", "accelerate", "deepspeed", "mpirun", "python.*train", "python.*finetune"]
    results = ["Running training processes:"]
    for line in r["stdout"].split("\n"):
        for kw in keywords:
            if re.search(kw, line, re.IGNORECASE):
                # Trim long lines
                results.append(f"  {line[:200]}")
                break
    if len(results) == 1:
        results.append("  No training processes found.")
    return "\n".join(results)


@server.tool()
def kill_training_job(
    pid: Annotated[int, "PID of the training process to kill"],
    graceful: Annotated[bool, "Send SIGTERM first, then SIGKILL after 5s"] = True,
) -> str:
    """Kill a training process. Use training_jobs first to find the PID."""
    if graceful:
        _run(["kill", "-15", str(pid)])  # SIGTERM
        import time
        time.sleep(5)
        # Check if still alive
        check = _run(["kill", "-0", str(pid)])
        if check["returncode"] == 0:
            _run(["kill", "-9", str(pid)])  # SIGKILL
            return f"Sent SIGTERM then SIGKILL to PID {pid}"
        return f"Sent SIGTERM to PID {pid}, process exited gracefully."
    else:
        r = _run(["kill", "-9", str(pid)])
        if r["returncode"] == 0:
            return f"Sent SIGKILL to PID {pid}"
        return f"Failed to kill PID {pid}: {r['stderr']}"


# --- Checkpoint Management ---

@server.tool()
def list_checkpoints(
    directory: Annotated[str, "Directory to search for checkpoints"] = "/home/aimsgroupuol",
    pattern: Annotated[str, "File pattern to match (default: *.pt, *.safetensors, *.ckpt)"] = "*.pt",
) -> str:
    """Find checkpoint files in a directory. Searches for .pt, .safetensors, .ckpt files."""
    import glob
    patterns = [pattern, "*.safetensors", "*.ckpt", "*.bin", "*.pth"]
    results = []
    for p in patterns:
        found = glob.glob(os.path.join(directory, "**", p), recursive=True)
        for f in found[:20]:  # Limit per pattern
            size_gb = os.path.getsize(f) / (1024 ** 3)
            results.append((f, size_gb))
    if not results:
        return f"No checkpoint files found in {directory}"
    results.sort(key=lambda x: x[1], reverse=True)
    output = [f"Checkpoints in {directory} ({len(results)} found, sorted by size):"]
    for path, size in results[:30]:
        output.append(f"  {size:.2f} GB  {path}")
    if len(results) > 30:
        output.append(f"  ... and {len(results) - 30} more")
    return "\n".join(output)


# --- Hostfile / Node Discovery ---

@server.tool()
def hostfile_info() -> str:
    """Get hostname, IP addresses, and check if this machine can be a distributed training node."""
    hostname = socket.gethostname()
    results = [f"Hostname: {hostname}"]
    # Get all IP addresses
    try:
        r = _run(["hostname", "-I"])
        if r["returncode"] == 0:
            results.append(f"IP addresses: {r['stdout']}")
    except:
        pass
    # Check SSH
    r = _run(["which", "ssh"])
    results.append(f"SSH available: {r['returncode'] == 0}")
    # Check for common distributed training tools
    for tool in ["torchrun", "accelerate", "deepspeed", "mpirun", "srun"]:
        r = _run(["which", tool])
        if r["returncode"] == 0:
            results.append(f"  {tool}: {r['stdout']}")
    # Check network bandwidth (quick)
    r = _run(["cat", "/sys/class/net/eth0/speed"]) if os.path.exists("/sys/class/net/eth0/speed") else {"returncode": -1, "stdout": "", "stderr": ""}
    if r["returncode"] == 0:
        results.append(f"eth0 speed: {r['stdout']} Mbps")
    return "\n".join(results)


# --- CLI Mode ---

TOOLS = {
    "list_gpus": list_gpus,
    "gpu_interconnect": gpu_interconnect,
    "cuda_visible_devices": cuda_visible_devices,
    "nccl_test_all_reduce": nccl_test_all_reduce,
    "check_nccl_env": check_nccl_env,
    "torch_distributed_info": torch_distributed_info,
    "check_ddp_setup": check_ddp_setup,
    "training_jobs": training_jobs,
    "kill_training_job": kill_training_job,
    "list_checkpoints": list_checkpoints,
    "hostfile_info": hostfile_info,
}


def cli_mode():
    if len(sys.argv) < 3:
        print("Usage: python3 server.py --cli <tool_name> [--arg value ...]")
        print("\nAvailable tools:")
        for name, func in TOOLS.items():
            doc = func.__doc__ or ""
            print(f"  {name:25} - {doc.split(chr(10))[0]}")
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
