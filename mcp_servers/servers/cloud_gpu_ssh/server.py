#!/usr/bin/env python3
"""
Cloud GPU & SSH MCP Server

Tools for managing remote GPU instances (generic SSH, Lambda Labs, RunPod, Vast.ai),
running commands on remote machines, syncing files, and monitoring remote training.

Supported cloud API tools:
  - lambda_gpu_pricing   (needs LAMBDA_API_KEY)
  - runpod_pricing       (needs RUNPOD_API_KEY)
  - runpod_machines      (needs RUNPOD_API_KEY)
  - vast_pricing         (public Vast bundles/offers)
  - vast_machines        (public Vast bundles/offers)

SSH/SFTP tools require paramiko. Install with: pip install paramiko

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import stat
import urllib.request
import urllib.error
from typing import Annotated, Any

try:
    import paramiko
    PARAMIKO_AVAILABLE = True
except ImportError:
    paramiko = None
    PARAMIKO_AVAILABLE = False

from mcp.server import MCPServer

server = MCPServer("cloud-gpu-ssh", "1.0.0")

# Config file for registered remote machines
CONFIG_PATH = os.environ.get("GPU_REMOTE_CONFIG", os.path.expanduser("~/.config/gpu-remotes.json"))


def _load_config() -> dict:
    if os.path.isfile(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {"machines": {}}


def _save_config(config: dict):
    parent = os.path.dirname(CONFIG_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def _ssh_connect(host: str, user: str, key_path: str, port: int = 22):
    if not PARAMIKO_AVAILABLE:
        raise RuntimeError("paramiko is not installed. Install it with 'pip install paramiko'.")
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, key_filename=key_path, timeout=10)
    return client


def _ssh_run(client, command: str, timeout: int = 60) -> dict:
    try:
        _stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
        return {
            "returncode": stdout.channel.recv_exit_status(),
            "stdout": stdout.read().decode().strip(),
            "stderr": stderr.read().decode().strip(),
        }
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e)}


# --- Machine Registration ---

@server.tool()
def register_machine(
    name: Annotated[str, "Friendly name for this machine (e.g., 'lambda-h100-1')"],
    host: Annotated[str, "IP address or hostname"],
    user: Annotated[str, "SSH username (usually 'ubuntu' or 'root')"],
    key_path: Annotated[str, "Path to SSH private key"],
    gpu_type: Annotated[str, "GPU type (e.g., 'H100', 'A100', 'GB10')"] = "unknown",
    gpu_count: Annotated[int, "Number of GPUs"] = 1,
    provider: Annotated[str, "Cloud provider: lambda, runpod, vast, custom"] = "custom",
    port: Annotated[int, "SSH port"] = 22,
) -> str:
    """Register a remote GPU machine for SSH access via MCP tools.
    After registration, you can run commands, sync files, and monitor training on it.
    """
    config = _load_config()
    config["machines"][name] = {
        "host": host, "user": user, "key_path": key_path,
        "gpu_type": gpu_type, "gpu_count": gpu_count,
        "provider": provider, "port": port,
    }
    _save_config(config)
    return f"Registered machine '{name}': {user}@{host}:{port} ({gpu_count}x {gpu_type}, {provider})"


@server.tool()
def list_machines() -> str:
    """List all registered remote GPU machines and their status."""
    config = _load_config()
    machines = config.get("machines", {})
    if not machines:
        return f"No machines registered. Use register_machine to add one.\nConfig: {CONFIG_PATH}"
    results = ["Registered GPU machines:"]
    for name, info in machines.items():
        results.append(
            f"  {name:20} {info['user']}@{info['host']}:{info['port']} "
            f"({info['gpu_count']}x {info['gpu_type']}, {info['provider']})"
        )
    return "\n".join(results)


@server.tool()
def unregister_machine(
    name: Annotated[str, "Machine name to remove"],
) -> str:
    """Remove a registered machine."""
    config = _load_config()
    if name not in config.get("machines", {}):
        return f"Machine '{name}' not found."
    del config["machines"][name]
    _save_config(config)
    return f"Removed machine '{name}'."


# --- Remote Command Execution ---

@server.tool()
def remote_command(
    machine: Annotated[str, "Registered machine name"],
    command: Annotated[str, "Shell command to run on the remote machine"],
    timeout: Annotated[int, "Timeout in seconds"] = 60,
) -> str:
    """Run a command on a remote GPU machine via SSH.
    Example: remote_command('lambda-h100-1', 'nvidia-smi')
    """
    if not PARAMIKO_AVAILABLE:
        return "paramiko is not installed. Install it with 'pip install paramiko' to use SSH tools."
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found. Use list_machines to see available machines."
    try:
        client = _ssh_connect(m["host"], m["user"], m["key_path"], m.get("port", 22))
        r = _ssh_run(client, command, timeout)
        client.close()
        result = f"[{machine}] $ {command}\nexit: {r['returncode']}"
        if r["stdout"]:
            result += f"\n--- stdout ---\n{r['stdout'][-2000:]}"
        if r["stderr"]:
            result += f"\n--- stderr ---\n{r['stderr'][-1000:]}"
        return result
    except Exception as e:
        return f"SSH connection failed: {e}"


@server.tool()
def remote_gpu_status(
    machine: Annotated[str, "Registered machine name"],
) -> str:
    """Get GPU status (nvidia-smi) on a remote machine."""
    return remote_command(machine, "nvidia-smi")


@server.tool()
def remote_training_status(
    machine: Annotated[str, "Registered machine name"],
) -> str:
    """Check for running training processes on a remote machine."""
    cmd = "ps aux | grep -E 'torchrun|python.*train|accelerate|deepspeed' | grep -v grep"
    return remote_command(machine, cmd)


@server.tool()
def remote_disk_usage(
    machine: Annotated[str, "Registered machine name"],
    path: Annotated[str, "Path to check"] = "/",
) -> str:
    """Check disk usage on a remote machine."""
    return remote_command(machine, f"df -h {path}")


@server.tool()
def remote_tail_log(
    machine: Annotated[str, "Registered machine name"],
    log_path: Annotated[str, "Path to the log file"],
    lines: Annotated[int, "Number of lines to show"] = 50,
) -> str:
    """Tail a log file on a remote machine. Useful for monitoring training output."""
    return remote_command(machine, f"tail -n {lines} {log_path}")


# --- File Sync ---

@server.tool()
def upload_file(
    machine: Annotated[str, "Registered machine name"],
    local_path: Annotated[str, "Local file path"],
    remote_path: Annotated[str, "Remote destination path"],
) -> str:
    """Upload a file to a remote GPU machine via SFTP."""
    if not PARAMIKO_AVAILABLE:
        return "paramiko is not installed. Install it with 'pip install paramiko' to use SFTP."
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found."
    if not os.path.isfile(local_path):
        return f"Local file not found: {local_path}"

    local_path = os.path.abspath(local_path)
    remote_dir = os.path.dirname(remote_path) or "."

    client = None
    sftp = None
    try:
        client = _ssh_connect(m["host"], m["user"], m["key_path"], m.get("port", 22))
        sftp = client.open_sftp()

        try:
            dir_stat = sftp.stat(remote_dir)
        except Exception:
            return f"Remote destination directory does not exist: {remote_dir}"
        if not stat.S_ISDIR(dir_stat.st_mode):
            return f"Remote destination is not a directory: {remote_dir}"

        sftp.put(local_path, remote_path)

        try:
            sftp.stat(remote_path)
        except Exception:
            return f"Upload appeared to succeed but remote file was not found: {remote_path}"

        size_mb = os.path.getsize(local_path) / (1024 * 1024)
        return f"Uploaded {local_path} ({size_mb:.1f} MB) -> {machine}:{remote_path}"
    except Exception as e:
        return f"Upload failed: {e}"
    finally:
        if sftp:
            sftp.close()
        if client:
            client.close()


@server.tool()
def download_file(
    machine: Annotated[str, "Registered machine name"],
    remote_path: Annotated[str, "Remote file path"],
    local_path: Annotated[str, "Local destination path"],
) -> str:
    """Download a file from a remote GPU machine via SFTP."""
    if not PARAMIKO_AVAILABLE:
        return "paramiko is not installed. Install it with 'pip install paramiko' to use SFTP."
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found."

    local_path = os.path.abspath(local_path)
    local_dir = os.path.dirname(local_path)
    if not os.path.isdir(local_dir):
        return f"Local destination directory does not exist: {local_dir}"
    if os.path.isdir(local_path):
        return f"Local destination path is a directory: {local_path}"

    client = None
    sftp = None
    try:
        client = _ssh_connect(m["host"], m["user"], m["key_path"], m.get("port", 22))
        sftp = client.open_sftp()

        try:
            remote_stat = sftp.stat(remote_path)
        except Exception:
            return f"Remote file not found: {remote_path}"
        if stat.S_ISDIR(remote_stat.st_mode):
            return f"Remote path is a directory, not a file: {remote_path}"

        sftp.get(remote_path, local_path)

        if not os.path.isfile(local_path):
            return f"Download appeared to succeed but local file was not found: {local_path}"

        size_mb = os.path.getsize(local_path) / (1024 * 1024)
        return f"Downloaded {machine}:{remote_path} -> {local_path} ({size_mb:.1f} MB)"
    except Exception as e:
        return f"Download failed: {e}"
    finally:
        if sftp:
            sftp.close()
        if client:
            client.close()


@server.tool()
def remote_sftp_list(
    machine: Annotated[str, "Registered machine name"],
    remote_path: Annotated[str, "Remote directory path"] = ".",
) -> str:
    """List files and directories on a remote machine via SFTP."""
    if not PARAMIKO_AVAILABLE:
        return "paramiko is not installed. Install it with 'pip install paramiko' to use SFTP."
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found."

    client = None
    sftp = None
    try:
        client = _ssh_connect(m["host"], m["user"], m["key_path"], m.get("port", 22))
        sftp = client.open_sftp()

        try:
            path_stat = sftp.stat(remote_path)
        except Exception:
            return f"Remote path not found: {remote_path}"

        if not stat.S_ISDIR(path_stat.st_mode):
            return (
                f"Remote path is a file, not a directory: {remote_path}\n"
                f"  size={path_stat.st_size} bytes  mode={oct(stat.S_IMODE(path_stat.st_mode))}"
            )

        entries = sftp.listdir_attr(remote_path)
        rows = [f"{'Type':<6} {'Size':>10}  Name", "-" * 40]
        for entry in sorted(entries, key=lambda e: e.filename):
            entry_type = "dir" if stat.S_ISDIR(entry.st_mode) else "file"
            rows.append(f"{entry_type:<6} {entry.st_size:>10}  {entry.filename}")
        return "\n".join(rows)
    except Exception as e:
        return f"SFTP list failed: {e}"
    finally:
        if sftp:
            sftp.close()
        if client:
            client.close()


# --- Cloud Provider Pricing & Machines ---

def _http_get_json(url: str, headers: dict | None = None, timeout: int = 15) -> Any:
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def _first_value(item: dict, keys: list[str]) -> str:
    for k in keys:
        if k in item and item[k] is not None:
            return str(item[k])
    return "unknown"


def _format_price(item: dict) -> str:
    price = item.get("price", {})
    if isinstance(price, dict):
        for k in ("secure", "community", "cluster", "uninterruptablePrice", "minimumBidPrice"):
            if k in price and price[k] is not None:
                return f"{price[k]:.4f}" if isinstance(price[k], (int, float)) else str(price[k])
    for k in ("dph_total", "securePrice", "communityPrice", "clusterPrice",
              "price_cents_per_hour", "pricePerHour", "cost", "costPerHr"):
        if k in item and item[k] is not None:
            return f"{item[k]:.4f}" if isinstance(item[k], (int, float)) else str(item[k])
    return "?"


@server.tool()
def lambda_gpu_pricing() -> str:
    """Get current Lambda Labs GPU instance pricing. Requires LAMBDA_API_KEY env var."""
    api_key = os.environ.get("LAMBDA_API_KEY", "")
    if not api_key:
        return "LAMBDA_API_KEY not set. Get one at https://cloud.lambda.ai/api-keys"
    try:
        req = urllib.request.Request(
            "https://cloud.lambda.ai/api/v1/instance-types",
            headers={"Authorization": f"Bearer {api_key}"},
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        results = ["Lambda Labs GPU Pricing:"]
        for name, info in data.get("data", {}).items():
            spec = info.get("instance_type", {})
            gpu = spec.get("description", "unknown")
            price = spec.get("price_cents_per_hour", "?")
            results.append(f"  {name:30} {gpu:40} ${price}/hr")
        return "\n".join(results)
    except Exception as e:
        return f"Error fetching pricing: {e}"


@server.tool()
def runpod_pricing() -> str:
    """Get current RunPod GPU pricing. Requires RUNPOD_API_KEY env var."""
    api_key = os.environ.get("RUNPOD_API_KEY", "")
    if not api_key:
        return "RUNPOD_API_KEY not set. Get one at https://www.runpod.io/console/user/settings"
    try:
        data = _http_get_json(
            "https://api.runpod.io/v2/cloud/prices",
            headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
            timeout=15,
        )
    except Exception:
        # Try the documented catalog endpoint if cloud/prices is unavailable.
        try:
            data = _http_get_json(
                "https://api.runpod.io/v2/catalog/gpus",
                headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
                timeout=15,
            )
        except Exception as e2:
            return f"Error fetching RunPod pricing: {e2}"

    items = []
    if isinstance(data, dict):
        if isinstance(data.get("gpus"), list):
            items = data["gpus"]
        elif isinstance(data.get("data"), list):
            items = data["data"]
        elif isinstance(data.get("data"), dict):
            items = list(data["data"].values())
        elif all(isinstance(v, dict) for v in data.values()):
            items = list(data.values())
    elif isinstance(data, list):
        items = data

    results = ["RunPod GPU Pricing:"]
    for item in items[:15]:
        name = _first_value(item, ["displayName", "name", "id"])
        price = _format_price(item)
        memory = item.get("memory", item.get("memoryInGb", ""))
        avail = item.get("availability", "")
        results.append(f"  {name:30} {str(memory):>6}GB  ${price:>8}/hr  {avail}")
    if len(results) == 1:
        return "No pricing data found in RunPod response."
    return "\n".join(results)


@server.tool()
def runpod_machines() -> str:
    """List RunPod pods in your account. Requires RUNPOD_API_KEY env var."""
    api_key = os.environ.get("RUNPOD_API_KEY", "")
    if not api_key:
        return "RUNPOD_API_KEY not set. Get one at https://www.runpod.io/console/user/settings"
    try:
        data = _http_get_json(
            "https://api.runpod.io/v2/pods",
            headers={"Authorization": f"Bearer {api_key}", "Accept": "application/json"},
            timeout=15,
        )
    except Exception as e:
        return f"Error fetching RunPod pods: {e}"

    pods = data if isinstance(data, list) else data.get("data", data.get("pods", []))
    if not pods:
        return "No RunPod pods found."

    results = ["RunPod pods:"]
    for pod in pods[:15]:
        pod_id = pod.get("id", "unknown")
        name = pod.get("name", "")
        status = pod.get("status", "")
        gpu = pod.get("gpu", {})
        if isinstance(gpu, dict):
            gpu_name = gpu.get("id", gpu.get("displayName", ""))
            count = gpu.get("count", 1)
        else:
            gpu_name = str(gpu)
            count = 1
        cost = pod.get("cost", pod.get("costPerHr", "?"))
        results.append(
            f"  {pod_id:20} {name:20} {status:12} {count}x {gpu_name:25} ${cost}/hr"
        )
    return "\n".join(results)


def _vast_fetch_public(primary_path: str, fallback_path: str) -> dict:
    """Try the requested Vast public path, then fall back to the public bundles API."""
    headers = {"Accept": "application/json", "User-Agent": "cloud-gpu-ssh-mcp/1.0"}
    for path in (primary_path, fallback_path):
        url = f"https://vast.ai/api/v0{path}"
        try:
            return _http_get_json(url, headers=headers, timeout=20)
        except urllib.error.HTTPError as e:
            if e.code == 404 and path == primary_path:
                continue
            raise
    return {}


@server.tool()
def vast_pricing(
    limit: Annotated[int, "Number of offers to display"] = 10,
) -> str:
    """Get public Vast.ai GPU pricing (no API key required)."""
    try:
        data = _vast_fetch_public("/gpus/", "/bundles/")
    except Exception as e:
        return f"Error fetching Vast pricing: {e}"

    offers = data.get("offers", [])
    if not offers:
        return "No Vast offers found."

    offers = sorted(offers, key=lambda o: float(o.get("dph_total") or float("inf")))[:limit]
    results = ["Vast.ai GPU Pricing (public offers, $/hr):"]
    for o in offers:
        results.append(
            f"  ID {o.get('id','?'):<12} {o.get('num_gpus',1)}x {o.get('gpu_name','unknown'):15} "
            f"${float(o.get('dph_total',0)):.3f}/hr  {o.get('geolocation','')}"
        )
    return "\n".join(results)


@server.tool()
def vast_machines(
    limit: Annotated[int, "Number of offers to display"] = 10,
) -> str:
    """List public Vast.ai machine offers (no API key required)."""
    try:
        data = _vast_fetch_public("/offers/", "/bundles/")
    except Exception as e:
        return f"Error fetching Vast machines: {e}"

    offers = data.get("offers", [])
    if not offers:
        return "No Vast offers found."

    offers = offers[:limit]
    results = ["Vast.ai Machine Offers (public):"]
    for o in offers:
        results.append(
            f"  ID {o.get('id','?'):<12} {o.get('num_gpus',1)}x {o.get('gpu_name','unknown'):15} "
            f"${float(o.get('dph_total',0)):.3f}/hr  {o.get('geolocation','')} "
            f"reliability={o.get('reliability','?')}  rentable={o.get('rentable',False)}"
        )
    return "\n".join(results)


# --- CLI Mode ---

TOOLS = {
    "register_machine": register_machine,
    "list_machines": list_machines,
    "unregister_machine": unregister_machine,
    "remote_command": remote_command,
    "remote_gpu_status": remote_gpu_status,
    "remote_training_status": remote_training_status,
    "remote_disk_usage": remote_disk_usage,
    "remote_tail_log": remote_tail_log,
    "upload_file": upload_file,
    "download_file": download_file,
    "remote_sftp_list": remote_sftp_list,
    "lambda_gpu_pricing": lambda_gpu_pricing,
    "runpod_pricing": runpod_pricing,
    "runpod_machines": runpod_machines,
    "vast_pricing": vast_pricing,
    "vast_machines": vast_machines,
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
