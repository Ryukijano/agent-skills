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


def _missing_jax_message() -> str:
    return "JAX not installed. Install with: pip install jax[tpu] or pip install jax[cuda12]"


def _jax_check_guard(r: dict) -> str | None:
    """Return a friendly missing-JAX message if JAX is not installed, else None."""
    if r["returncode"] != 0:
        r2 = _run(["python3", "-c", "import jax; print(jax.__version__)"])
        if r2["returncode"] != 0:
            return _missing_jax_message()
        return f"Error: {r['stderr']}"
    return None


# --- JAX Device Discovery ---

@server.tool()
def jax_devices() -> str:
    """List all JAX-visible devices (TPU, GPU, CPU). Shows device count, type, and topology.
    Requires JAX to be installed.
    """
    code = r"""
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
        r2 = _run(["python3", "-c", "import jax; print(jax.__version__)"])
        if r2["returncode"] != 0:
            return _missing_jax_message()
        return f"Error: {r['stderr']}"
    return r["stdout"]


@server.tool()
def jax_tpu_info() -> str:
    """Get detailed TPU information including topology, mesh, and memory.
    Only works on TPU VMs (not on GPU/CPU).
    """
    code = r"""
import jax
import jax.numpy as jnp
import sys

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
    sys.exit(0)

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
    err = _jax_check_guard(r)
    if err is not None:
        return err
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
    code = r"""
try:
    import jax
    import jax.distributed
    print("jax.distributed: available")
    print("  Initialize with: jax.distributed.initialize()")
except ImportError:
    print("jax.distributed: not available")
"""
    r = _run(["python3", "-c", code])
    if r["returncode"] == 0:
        results.append(f"\n{r['stdout']}")
    else:
        results.append(f"\nCould not verify jax.distributed: {r['stderr']}")
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
    version: Annotated[str, "TPU VM software image version. Defaults: v4 -> tpu-vm-v4-base, v5e -> v2-alpha, otherwise tpu-vm-v4-base."] = "",
) -> str:
    """Create a TPU VM on Google Cloud. Requires gcloud CLI and auth.
    WARNING: This creates a billable resource. Use gcloud_tpu_delete when done.
    """
    if not version:
        if accelerator_type.startswith("v4"):
            version = "tpu-vm-v4-base"
        elif accelerator_type.startswith("v5e"):
            version = "v2-alpha"
        else:
            version = "tpu-vm-v4-base"
    cmd = ["gcloud", "compute", "tpus", "tpu-vm", "create", name,
           "--accelerator-type", accelerator_type, "--zone", zone,
           "--version", version]
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
    port: Annotated[int, "Profiler server port"] = 6006,
) -> str:
    """Profile a JAX script using jax.profiler. Generates a TensorBoard-compatible trace.
    View with: tensorboard --logdir /tmp/jax_profile
    """
    if not os.path.isfile(script_path):
        return f"Error: script not found: {script_path}"
    if not script_path.endswith(".py"):
        return f"Error: script must be a .py file: {script_path}"

    template = r"""
import jax
import jax.profiler
import os
import subprocess
import sys
import time

output_dir = __OUTPUT__
port = __PORT__
duration_ms = __DURATION_MS__
script_path = os.environ.get('JAX_PROFILE_SCRIPT', '')

if not os.path.isfile(script_path) or not script_path.endswith('.py'):
    print(f"Error: invalid script path: {script_path}")
    sys.exit(1)

jax.profiler.start_server(port)
print(f"Profiler server started on port {port}")

with jax.profiler.trace(output_dir, create_perfetto_link=False):
    proc = subprocess.run([sys.executable, script_path], env=os.environ, capture_output=True, text=True, timeout=120)
    print(proc.stdout[-1000:])
    if proc.stderr:
        print(f"stderr: {proc.stderr[-500:]}")
    print(f"Exit code: {proc.returncode}")
    # Hold the trace for the requested duration
    time.sleep(duration_ms / 1000.0)
"""
    code = (template
            .replace("__OUTPUT__", json.dumps(output))
            .replace("__PORT__", str(port))
            .replace("__DURATION_MS__", str(duration_ms)))
    r = _run(["python3", "-c", code], timeout=180,
             env={"JAX_PROFILE_SCRIPT": script_path, "JAX_PROFILE": "1"})
    if r["returncode"] != 0:
        return f"Profiling failed: {r['stderr']}"
    return f"{r['stdout']}\n\nView profile with: tensorboard --logdir {output}"


# --- JAX Memory and Performance ---

@server.tool()
def jax_memory_info() -> str:
    """Get JAX memory usage and limits for all devices."""
    code = r"""
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
    err = _jax_check_guard(r)
    if err is not None:
        return err
    return r["stdout"]


@server.tool()
def jax_compilation_check(
    function_code: Annotated[str, "JAX function code to compile. Must define a function named 'fn'."],
    input_code: Annotated[str, "Python expression for input(s) to pass to fn. Default: jnp.ones((1, 3))."] = "jnp.ones((1, 3))",
) -> str:
    """Check if a JAX function compiles and see its XLA HLO. Useful for debugging TPU compilation errors."""
    template = r"""
import jax
import jax.numpy as jnp

__FUNCTION_CODE__

fn = jax.jit(fn)
inp = eval(__INPUT_CODE__)
compiled = fn.lower(inp).compiler_ir()
print("Compilation successful!")
print(compiled)
"""
    code = (template
            .replace("__FUNCTION_CODE__", function_code, 1)
            .replace("__INPUT_CODE__", json.dumps(input_code), 1))
    r = _run(["python3", "-c", code])
    err = _jax_check_guard(r)
    if err is not None:
        return err
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
