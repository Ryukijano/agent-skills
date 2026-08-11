#!/usr/bin/env python3
"""
Cloud GPU & SSH MCP Server

Tools for managing remote GPU instances (Lambda Labs, RunPod, Vast.ai, SSH),
running commands on remote machines, syncing files, and monitoring remote training.

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import subprocess
import paramiko
from typing import Annotated

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
    os.makedirs(os.path.dirname(CONFIG_PATH), exist_ok=True)
    with open(CONFIG_PATH, "w") as f:
        json.dump(config, f, indent=2)


def _ssh_connect(host: str, user: str, key_path: str, port: int = 22) -> paramiko.SSHClient:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=user, key_filename=key_path, timeout=10)
    return client


def _ssh_run(client: paramiko.SSHClient, command: str, timeout: int = 60) -> dict:
    try:
        stdin, stdout, stderr = client.exec_command(command, timeout=timeout)
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
    """Upload a file to a remote GPU machine via SCP/SFTP."""
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found."
    if not os.path.isfile(local_path):
        return f"Local file not found: {local_path}"
    try:
        import paramiko
        transport = paramiko.Transport((m["host"], m.get("port", 22)))
        transport.connect(username=m["user"], pkey=paramiko.RSAKey.from_private_key_file(m["key_path"]))
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.put(local_path, remote_path)
        sftp.close()
        transport.close()
        size_mb = os.path.getsize(local_path) / (1024 * 1024)
        return f"Uploaded {local_path} ({size_mb:.1f} MB) -> {machine}:{remote_path}"
    except Exception as e:
        return f"Upload failed: {e}"


@server.tool()
def download_file(
    machine: Annotated[str, "Registered machine name"],
    remote_path: Annotated[str, "Remote file path"],
    local_path: Annotated[str, "Local destination path"],
) -> str:
    """Download a file from a remote GPU machine via SCP/SFTP."""
    config = _load_config()
    m = config.get("machines", {}).get(machine)
    if not m:
        return f"Machine '{machine}' not found."
    try:
        import paramiko
        transport = paramiko.Transport((m["host"], m.get("port", 22)))
        transport.connect(username=m["user"], pkey=paramiko.RSAKey.from_private_key_file(m["key_path"]))
        sftp = paramiko.SFTPClient.from_transport(transport)
        sftp.get(remote_path, local_path)
        sftp.close()
        transport.close()
        size_mb = os.path.getsize(local_path) / (1024 * 1024)
        return f"Downloaded {machine}:{remote_path} -> {local_path} ({size_mb:.1f} MB)"
    except Exception as e:
        return f"Download failed: {e}"


# --- Cloud Provider Pricing (Lambda Labs) ---

@server.tool()
def lambda_gpu_pricing() -> str:
    """Get current Lambda Labs GPU instance pricing. Requires LAMBDA_API_KEY env var."""
    import urllib.request
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
    "lambda_gpu_pricing": lambda_gpu_pricing,
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
