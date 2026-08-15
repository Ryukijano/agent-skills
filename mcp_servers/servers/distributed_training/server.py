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
import time
import glob
import tempfile
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("distributed-training", "1.0.0")

# Use the interpreter that is running this server for all PyTorch / subprocess checks.
# Can be overridden via MCP_PYTHON_BIN if the server is launched from a non-target env.
PYTHON = os.environ.get("MCP_PYTHON_BIN", sys.executable)

MAX_CHECKPOINT_RESULTS = 50
DEFAULT_CHECKPOINT_PATTERNS = ["*.pt", "*.safetensors", "*.ckpt", "*.bin", "*.pth"]
DEFAULT_CHECKPOINT_DEPTH = 2


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


def _strip_ansi(text: str) -> str:
    return re.sub(r"\x1b\[[0-9;]*m", "", text)


def _visible_gpu_count() -> int:
    """Count visible GPUs using nvidia-smi."""
    r = _run(["nvidia-smi", "-L"])
    if r["returncode"] != 0:
        return 0
    return len(
        [l for l in r["stdout"].splitlines() if re.match(r"GPU\s*\d+:", l.strip())]
    )


def _find_free_port(preferred_start: int = 29500, max_tries: int = 10) -> int:
    """Find an available localhost TCP port, trying a few preferred ports first."""
    for port in range(preferred_start, preferred_start + max_tries):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(("localhost", port))
                return port
            except OSError:
                continue
    # Fallback to an OS-assigned port.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 0))
        return s.getsockname()[1]


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

    raw = _strip_ansi(r["stdout"])
    lines = raw.splitlines()

    # Parse the actual connection matrix, not the legend.
    header: list[str] | None = None
    rows: list[list[str]] = []
    for line in lines:
        if "Legend" in line:
            break
        parts = [p.strip() for p in line.split("\t") if p.strip() != ""]
        if not parts:
            continue
        # The header is the first line whose first token is GPU0. Subsequent
        # lines that start with a GPU label are data rows.
        if header is None and re.match(r"^GPU0$", parts[0]):
            header = parts
            continue
        if header is not None and re.match(r"^GPU\d+$", parts[0]):
            rows.append(parts)

    if not header:
        return "GPU Interconnect Topology:\n" + raw

    gpu_labels = [h for h in header if re.match(r"^GPU\d+$", h)]
    n = len(gpu_labels)
    if n < 2:
        return "GPU Interconnect link summary (1 GPU): no inter-GPU links to report."


    summary = [f"GPU Interconnect link summary ({n} GPUs):"]
    link_counts: dict[str, int] = {}
    for row in rows:
        label = row[0]
        m = re.match(r"GPU(\d+)", label)
        if not m:
            continue
        i = int(m.group(1))
        entries = row[1 : 1 + n]
        for j in range(i + 1, n):
            if j >= len(entries):
                continue
            token = entries[j].strip()
            if token == "X" or not token:
                continue
            if re.match(r"^NV\d+$", token):
                link = token
            else:
                link = f"PCIe ({token})"
            pair = f"GPU{i} <-> GPU{j}"
            summary.append(f"  {pair}: {link}")
            link_counts[link] = link_counts.get(link, 0) + 1

    summary.append("\nLink type counts:")
    if not link_counts:
        summary.append("  No inter-GPU links found.")
    else:
        for link, count in sorted(link_counts.items(), key=lambda x: x[1], reverse=True):
            summary.append(f"  {link}: {count} pair(s)")

    has_nvlink = any(k.startswith("NV") for k in link_counts)
    if not has_nvlink:
        summary.append("\nWARNING: No NVLink detected. Multi-GPU all-reduce will use PCIe (slower).")

    return "\n".join(summary)


@server.tool()
def cuda_visible_devices() -> str:
    """Show current CUDA_VISIBLE_DEVICES setting and how many GPUs are visible to CUDA."""
    env_val = os.environ.get("CUDA_VISIBLE_DEVICES", "not set (all GPUs visible)")
    r = _run([PYTHON, "-c", "import torch; print(f'PyTorch sees {torch.cuda.device_count()} GPU(s)')"])
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
    nccl_ver = torch.cuda.nccl.version()
    print(f"NCCL version: {nccl_ver}")
except Exception as e:
    print(f"NCCL version: not available ({e})")
print(f"NCCL backend available: {dist.is_nccl_available()}")
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
    r = _run([PYTHON, "-c", code], timeout=30)
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
    backend = backend.lower().strip()
    if backend not in {"nccl", "gloo", "mpi"}:
        return f"Unsupported backend: {backend}"

    visible_gpus = _visible_gpu_count()
    if backend == "nccl" and visible_gpus == 0:
        return "DDP NCCL test failed: no GPUs visible."
    if backend == "nccl" and world_size > visible_gpus:
        return f"DDP NCCL test failed: world_size ({world_size}) exceeds visible GPU count ({visible_gpus})."

    port = _find_free_port()

    script = f"""
import os
import torch
import torch.distributed as dist
import torch.multiprocessing as mp


def test_ddp(rank, world_size, backend, port):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = str(port)
    dist.init_process_group(backend=backend, rank=rank, world_size=world_size)

    if torch.cuda.is_available() and backend == 'nccl' and rank < torch.cuda.device_count():
        torch.cuda.set_device(rank)

    model = torch.nn.Linear(10, 10)
    if torch.cuda.is_available() and backend == 'nccl':
        dev_id = rank % max(1, torch.cuda.device_count())
        model = model.cuda(dev_id)
        ddp = torch.nn.parallel.DistributedDataParallel(model, device_ids=[dev_id], output_device=dev_id)
    else:
        ddp = torch.nn.parallel.DistributedDataParallel(model)

    x = torch.randn(4, 10)
    if torch.cuda.is_available() and backend == 'nccl':
        dev_id = rank % max(1, torch.cuda.device_count())
        x = x.cuda(dev_id)
    y = ddp(x)
    y.sum().backward()

    dist.destroy_process_group()
    print(f"Rank {{rank}}: DDP initialized and ran one step with {{backend}} backend, world_size={{world_size}}")


if __name__ == '__main__':
    mp.spawn(test_ddp, args=({world_size}, "{backend}", {port}), nprocs={world_size}, join=True)
    print("DDP test passed.")
"""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(script)
        tmp_path = f.name

    try:
        r = _run([PYTHON, tmp_path], timeout=60)
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass

    if r["returncode"] != 0:
        return f"DDP test failed:\n{r['stderr']}\n{r['stdout']}".strip()
    return r["stdout"] or "DDP test passed (no output)"


@server.tool()
def check_fsdp_setup(
    world_size: Annotated[int, "Number of processes/GPUs"] = 1,
    backend: Annotated[str, "Communication backend: nccl, gloo"] = "gloo",
) -> str:
    """Check that torch.distributed.fsdp.FullyShardedDataParallel can wrap a small model."""
    backend = backend.lower().strip()
    if backend not in {"nccl", "gloo"}:
        return f"FSDP only supports nccl or gloo, got {backend}"

    visible_gpus = _visible_gpu_count()
    if backend == "nccl" and visible_gpus == 0:
        return "FSDP NCCL test failed: no GPUs visible."
    if backend == "nccl" and world_size > visible_gpus:
        return f"FSDP NCCL test failed: world_size ({world_size}) exceeds visible GPU count ({visible_gpus})."

    port = _find_free_port()

    script = f"""
import os
import torch
import torch.distributed as dist
import torch.multiprocessing as mp
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP


def test_fsdp(rank, world_size, backend, port):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = str(port)
    dist.init_process_group(backend=backend, rank=rank, world_size=world_size)

    if torch.cuda.is_available() and backend == 'nccl' and rank < torch.cuda.device_count():
        torch.cuda.set_device(rank)

    dev_id = rank % max(1, torch.cuda.device_count())
    device = torch.device(f"cuda:{{dev_id}}" if torch.cuda.is_available() and backend == 'nccl' else "cpu")
    model = torch.nn.Linear(10, 10).to(device)
    fsdp_model = FSDP(model)

    x = torch.randn(4, 10).to(device)
    out = fsdp_model(x)
    out.sum().backward()

    dist.destroy_process_group()
    print(f"Rank {{rank}}: FSDP wrapper check passed with {{backend}} backend, world_size={{world_size}}")


if __name__ == '__main__':
    mp.spawn(test_fsdp, args=({world_size}, "{backend}", {port}), nprocs={world_size}, join=True)
    print("FSDP test passed.")
"""
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(script)
        tmp_path = f.name

    try:
        r = _run([PYTHON, tmp_path], timeout=60)
    finally:
        try:
            os.unlink(tmp_path)
        except Exception:
            pass

    if r["returncode"] != 0:
        return f"FSDP test failed:\n{r['stderr']}\n{r['stdout']}".strip()
    return r["stdout"] or "FSDP test passed (no output)"


# --- Training Job Management ---

@server.tool()
def training_jobs() -> str:
    """List running training processes (torchrun, python -m torch.distributed, accelerate, deepspeed)."""
    r = _run(["ps", "aux"])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    keywords = [
        "torchrun",
        r"torch\.distributed",
        "accelerate",
        "deepspeed",
        "mpirun",
        "python.*train",
        "python.*finetune",
    ]
    exclude = ["mcp_servers/servers", "server.py"]
    matches: set[str] = set()
    for line in r["stdout"].split("\n"):
        if not line.strip():
            continue
        # Skip the MCP server itself and other server utilities.
        if any(ex in line for ex in exclude):
            continue
        for kw in keywords:
            if re.search(kw, line, re.IGNORECASE):
                # Trim long lines
                matches.add(line[:200])
                break
    if not matches:
        return "Running training processes:\n  No training processes found."
    sorted_matches = sorted(matches)
    return "Running training processes:\n" + "\n".join(f"  {m}" for m in sorted_matches)


@server.tool()
def kill_training_job(
    pid: Annotated[int, "PID of the training process to kill"],
    force: Annotated[bool, "Confirm the kill; required unless dry_run is true"] = False,
    graceful: Annotated[bool, "Send SIGTERM first, then SIGKILL if still alive"] = True,
    dry_run: Annotated[bool, "Show what would be killed without killing"] = False,
) -> str:
    """Kill a training process. Use training_jobs first to find the PID."""
    if pid <= 0:
        return f"Invalid PID: {pid}"
    if pid == os.getpid():
        return f"Refusing to kill the MCP server process (PID {pid})."

    # Validate the PID exists and get a friendly description.
    check = _run(["kill", "-0", str(pid)])
    if check["returncode"] != 0:
        return f"PID {pid} is not running or cannot be signalled."

    r = _run(["ps", "-p", str(pid), "-o", "pid,args", "--no-headers"])
    if r["returncode"] == 0 and r["stdout"].strip():
        target = r["stdout"].strip()
    else:
        target = f"PID {pid}"

    if dry_run:
        return f"Dry run: would kill {target}"

    if not force:
        return (
            f"Safety interlock: set force=true to kill {target}. "
            "Use dry_run=true to preview first."
        )

    if graceful:
        _run(["kill", "-15", str(pid)])  # SIGTERM
        # Poll briefly; no long blocking sleep.
        for _ in range(10):
            time.sleep(0.2)
            alive = _run(["kill", "-0", str(pid)])
            if alive["returncode"] != 0:
                return f"Sent SIGTERM to {target}; process exited gracefully."
        _run(["kill", "-9", str(pid)])  # SIGKILL
        return f"Sent SIGTERM then SIGKILL to {target}."
    else:
        r = _run(["kill", "-9", str(pid)])
        if r["returncode"] == 0:
            return f"Sent SIGKILL to {target}."
        return f"Failed to kill {target}: {r['stderr']}"


# --- Checkpoint Management ---

@server.tool()
def list_checkpoints(
    directory: Annotated[str, "Directory to search for checkpoints"] = "/home/aimsgroupuol",
    pattern: Annotated[
        str,
        "File pattern(s) to match, comma-separated (default: *.pt,*.safetensors,*.ckpt,*.bin,*.pth)",
    ] = ", ".join(DEFAULT_CHECKPOINT_PATTERNS),
    max_depth: Annotated[int, "Maximum directory depth to search"] = DEFAULT_CHECKPOINT_DEPTH,
) -> str:
    """Find checkpoint files in a directory. Searches for .pt, .safetensors, .ckpt, .bin, .pth files
    up to a limited recursion depth and returns at most 50 results.
    """
    import glob

    directory = os.path.expanduser(directory)
    if not os.path.isdir(directory):
        return f"Directory not found: {directory}"

    # Respect the pattern argument; empty string falls back to defaults.
    if pattern and pattern.strip():
        patterns = [p.strip() for p in pattern.split(",") if p.strip()]
    else:
        patterns = list(DEFAULT_CHECKPOINT_PATTERNS)

    # Limit search depth by constructing glob patterns for each level.
    found: set[str] = set()
    for pat in patterns:
        for depth in range(max_depth + 1):
            parts = [directory] + ["*"] * depth + [pat]
            found.update(glob.glob(os.path.join(*parts)))
            if len(found) >= MAX_CHECKPOINT_RESULTS:
                break
        if len(found) >= MAX_CHECKPOINT_RESULTS:
            break

    if not found:
        return f"No checkpoint files found in {directory} (patterns: {', '.join(patterns)})"

    results = []
    for f in found:
        try:
            size_gb = os.path.getsize(f) / (1024 ** 3)
            results.append((f, size_gb))
        except OSError:
            continue

    results.sort(key=lambda x: x[1], reverse=True)
    output = [
        f"Checkpoints in {directory} (patterns: {', '.join(patterns)}; "
        f"{len(results)} found, top {min(MAX_CHECKPOINT_RESULTS, len(results))} by size):"
    ]
    for path, size in results[:MAX_CHECKPOINT_RESULTS]:
        output.append(f"  {size:.2f} GB  {path}")
    if len(results) > MAX_CHECKPOINT_RESULTS:
        output.append(f"  ... and {len(results) - MAX_CHECKPOINT_RESULTS} more")
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
    "check_fsdp_setup": check_fsdp_setup,
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
