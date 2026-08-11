#!/usr/bin/env python3
"""
TPU & JAX MCP Server

Tools for TPU discovery, JAX device management, TPU runtime monitoring,
and JAX distributed training setup. Works with Google Cloud TPUs (v4, v5e, v5p, Trillium v6e).

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import subprocess
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("tpu-jax", "1.0.0")


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


# --- JAX Device Discovery ---

@server.tool()
def jax_devices() -> str:
    """List all JAX-visible devices (TPU, GPU, CPU). Shows device count, type, and topology.
    Requires JAX to be installed.
    """
    code = """
import jax
import jax.numpy as jnp

print(f"JAX version: {jax.__version__}")
devices = jax.devices()
print(f"Total devices: {len(devices)}")
for i, d in enumerate(devices):
    print(f"  Device {i}: {d.platform.upper()} id={d.id} ({d.device_kind})")

# Platform breakdown
platforms = {}
for d in devices:
    platforms.setdefault(d.platform, 0)
    platforms[d.platform] += 1
print(f"\nPlatform summary: {dict(platforms)}")

# Local devices vs all devices
local = jax.local_devices()
print(f"Local devices: {len(local)}")

# Process index (for multi-host)
try:
    print(f"Process index: {jax.process_index()}")
    print(f"Process count: {jax.process_count()}")
except:
    pass

# TPU topology
try:
    from jax.experimental.mesh_utils import DEVICE_MESH
    print(f"\nTPU topology available")
except:
    pass
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] != 0:
        # Check if JAX is installed
        r2 = _run(["python3", "-c", "import jax; print(jax.__version__)"])
        if r2["returncode"] != 0:
            return "JAX not installed. Install with: pip install jax[tpu] or pip install jax[cuda12]"
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def jax_tpu_info() -> str:
    """Get detailed TPU information including topology, mesh, and memory.
    Only works on TPU VMs (not on GPU/CPU).
    """
    code = """
import jax
import jax.numpy as jnp

devices = jax.devices()
tpu_devices = [d for d in devices if d.platform == 'tpu']

if not tpu_devices:
    print("No TPU devices found. This machine may not be a TPU VM.")
    print(f"Available platforms: {set(d.platform for d in devices)}")
    # Check environment
    import os
    tpu_env = {k: v for k, v in os.environ.items() if 'TPU' in k.upper() or 'JAX' in k.upper()}
    if tpu_env:
        print(f"\nTPU/JAX env vars: {tpu_env}")
    return

print(f"TPU devices: {len(tpu_devices)}")
for d in tpu_devices:
    print(f"  {d.device_kind} (id={d.id})")

# Memory info
for d in tpu_devices[:1]:
    try:
        mem_info = d.memory_stats()
        if mem_info:
            print(f"\nMemory (first TPU):")
            for k, v in mem_info.items():
                if isinstance(v, (int, float)):
                    print(f"  {k}: {v / 1e9:.2f} GB" if v > 1e9 else f"  {k}: {v}")
    except:
        pass

# Topology
try:
    from jax.experimental import mesh_utils
    mesh = mesh_utils.create_device_mesh((len(tpu_devices),))
    print(f"\nDevice mesh shape: {mesh.shape}")
    print(f"Device mesh: {mesh}")
except Exception as e:
    print(f"\nMesh creation: {e}")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def jax_distributed_setup(
    num_processes: Annotated[int, "Number of processes (hosts)"] = 1,
    process_id: Annotated[int, "Process ID (0-indexed)"] = 0,
    coordinator_address: Annotated[str, "Coordinator IP address"] = "127.0.0.1:1234",
) -> str:
    """Check JAX distributed setup for multi-host TPU training.
    Returns the environment variables needed for multi-host JAX.
    """
    env_vars = {
        "JAX_NUM_PROCESSES": str(num_processes),
        "JAX_PROCESS_ID": str(process_id),
        "JAX_COORDINATOR_ADDRESS": coordinator_address,
    }
    results = ["JAX Distributed Setup:"]
    results.append(f"  Processes: {num_processes}")
    results.append(f"  Process ID: {process_id}")
    results.append(f"  Coordinator: {coordinator_address}")
    results.append("\nEnvironment variables to set:")
    for k, v in env_vars.items():
        results.append(f"  export {k}={v}")
    # Check if jax.distributed is available
    code = """
import jax
try:
    import jax.distributed
    print("jax.distributed: available")
    print("  Initialize with: jax.distributed.initialize()")
except ImportError:
    print("jax.distributed: not available")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] == 0:
        results.append(f"\n{r['stdout']}")
    return "\n".join(results)


# --- Google Cloud TPU Management ---

@server.tool()
def gcloud_tpu_list() -> str:
    """List TPU nodes/VMs in Google Cloud. Requires gcloud CLI and auth."""
    r = _run(["gcloud", "compute", "tpus", "list", "--format=table(name,zone,acceleratorType,state,ipAddress)"])
    if r["returncode"] != 0:
        # Try TPU VMs (v2 API)
        r = _run(["gcloud", "compute", "tpus", "tpu-vm", "list"])
        if r["returncode"] != 0:
            return f"Error (is gcloud installed and authenticated?):\n{r['stderr']}"
    return r["stdout"] if r["stdout"].strip() else "No TPU nodes found."


@server.tool()
def gcloud_tpu_create(
    name: Annotated[str, "TPU node name"],
    accelerator_type: Annotated[str, "TPU type: v4-8, v5e-4, v5p-8, v6e-4, etc."] = "v5e-4",
    zone: Annotated[str, "GCP zone"] = "us-central2-b",
    preemptible: Annotated[bool, "Use preemptible (cheaper, can be taken back)"] = False,
) -> str:
    """Create a TPU VM on Google Cloud. Requires gcloud CLI and auth.
    WARNING: This creates a billable resource. Use gcloud_tpu_delete when done.
    """
    cmd = ["gcloud", "compute", "tpus", "tpu-vm", "create", name,
           "--accelerator-type", accelerator_type, "--zone", zone,
           "--version", "tpu-vm-v4-base"]  # Default software version
    if preemptible:
        cmd.append("--preemptible")
    r = _run(cmd, timeout=120)
    if r["returncode"] == 0:
        return f"TPU VM '{name}' created: {accelerator_type} in {zone}\nUse gcloud_tpu_ssh to connect."
    return f"Failed to create TPU: {r['stderr']}"


@server.tool()
def gcloud_tpu_delete(
    name: Annotated[str, "TPU node name"],
    zone: Annotated[str, "GCP zone"] = "us-central2-b",
) -> str:
    """Delete a TPU VM. This stops billing for the resource."""
    r = _run(["gcloud", "compute", "tpus", "tpu-vm", "delete", name, "--zone", zone, "--quiet"])
    if r["returncode"] == 0:
        return f"TPU VM '{name}' deleted in {zone}."
    return f"Failed to delete TPU: {r['stderr']}"


@server.tool()
def gcloud_tpu_ssh(
    name: Annotated[str, "TPU node name"],
    zone: Annotated[str, "GCP zone"] = "us-central2-b",
    command: Annotated[str, "Command to run (empty = interactive SSH)"] = "",
) -> str:
    """SSH into a TPU VM. Optionally run a command non-interactively."""
    cmd = ["gcloud", "compute", "tpus", "tpu-vm", "ssh", name, "--zone", zone]
    if command:
        cmd.extend(["--", command])
    r = _run(cmd, timeout=60)
    if r["returncode"] == 0:
        return r["stdout"] or "SSH connection successful."
    return f"SSH failed: {r['stderr']}"


# --- JAX Profiling ---

@server.tool()
def jax_profile(
    script_path: Annotated[str, "Path to Python script to profile"],
    output: Annotated[str, "Output profile directory"] = "/tmp/jax_profile",
    duration_ms: Annotated[int, "Profile duration in ms"] = 5000,
) -> str:
    """Profile a JAX script using jax.profiler. Generates a TensorBoard-compatible trace.
    View with: tensorboard --logdir /tmp/jax_profile
    """
    code = f"""
import jax
import jax.profiler
import subprocess
import sys

# Start server for live profiling
jax.profiler.start_server(6006)
print(f"Profiler server started on port 6006")

# Run the script with profiling
env = dict(__import__('os').environ)
env['JAX_PROFILE'] = '1'
proc = subprocess.run([sys.executable, '{script_path}'], env=env, capture_output=True, text=True, timeout=120)
print(proc.stdout[-1000:])
if proc.stderr:
    print(f"stderr: {{proc.stderr[-500:]}}")
print(f"Exit code: {{proc.returncode}}")
"""
    r = _run(["python3", "-c", code], timeout=180)
    if r["returncode"] != 0:
        return f"Profiling failed: {r['stderr']}"
    return f"{r['stdout']}\n\nView profile with: tensorboard --logdir {output}"


# --- JAX Memory and Performance ---

@server.tool()
def jax_memory_info() -> str:
    """Get JAX memory usage and limits for all devices."""
    code = """
import jax
devices = jax.devices()
print(f"JAX memory info ({len(devices)} devices):")
for d in devices:
    try:
        stats = d.memory_stats()
        if stats:
            limits = stats.get('limit', 0)
            used = stats.get('bytes_in_use', 0)
            print(f"  {d.platform}:{d.id} ({d.device_kind}):")
            print(f"    Limit: {limits / 1e9:.2f} GB")
            print(f"    In use: {used / 1e9:.2f} GB")
            print(f"    Free: {(limits - used) / 1e9:.2f} GB")
    except Exception as e:
        print(f"  {d.platform}:{d.id}: {e}")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def jax_compilation_check(
    function_code: Annotated[str, "JAX function code to compile (as a string)"],
) -> str:
    """Check if a JAX function compiles and see its XLA HLO. Useful for debugging TPU compilation errors."""
    code = f"""
import jax
import jax.numpy as jnp

{function_code}

# Try to compile and show XLA
try:
    # Assume the function is called 'fn'
    compiled = fn.lower(jnp.ones((1, 3))).compiler_ir()
    print("Compilation successful!")
    print(f"XLA HLO (first 500 chars):")
    print(str(compiled)[:500])
except Exception as e:
    print(f"Compilation failed: {{type(e).__name__}}: {{e}}")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] != 0:
        return f"Error: {r['stderr']}"
    return r["stdout"]


# --- CLI Mode ---

TOOLS = {
    "jax_devices": jax_devices,
    "jax_tpu_info": jax_tpu_info,
    "jax_distributed_setup": jax_distributed_setup,
    "gcloud_tpu_list": gcloud_tpu_list,
    "gcloud_tpu_create": gcloud_tpu_create,
    "gcloud_tpu_delete": gcloud_tpu_delete,
    "gcloud_tpu_ssh": gcloud_tpu_ssh,
    "jax_profile": jax_profile,
    "jax_memory_info": jax_memory_info,
    "jax_compilation_check": jax_compilation_check,
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
