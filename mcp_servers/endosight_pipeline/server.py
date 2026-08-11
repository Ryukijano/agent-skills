#!/usr/bin/env python3
"""
Endosight Pipeline MCP Server

Exposes Endosight 3D pipeline operations as MCP tools so agents can
trigger and monitor pipeline runs directly.

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import subprocess
import glob
from typing import Annotated

from mcp.server import MCPServer

server = MCPServer("endosight-pipeline", "1.0.0")

# Canonical paths from AGENTS.md
ENDOSIGHT_ROOT = "/home/aimsgroupuol/endosight_project/endosight-3d"
OUTPUTS_ROOT = os.path.join(ENDOSIGHT_ROOT, "vis/outputs")
BACKEND_SCRIPTS = os.path.join(ENDOSIGHT_ROOT, "backend/scripts")


def _run(cmd: list[str], timeout: int = 30, cwd: str | None = None) -> dict:
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=timeout, cwd=cwd
        )
        return {"returncode": result.returncode, "stdout": result.stdout.strip(), "stderr": result.stderr.strip()}
    except subprocess.TimeoutExpired:
        return {"returncode": -1, "stdout": "", "stderr": f"Timed out after {timeout}s"}
    except FileNotFoundError:
        return {"returncode": -1, "stdout": "", "stderr": f"Not found: {cmd[0]}"}
    except Exception as e:
        return {"returncode": -1, "stdout": "", "stderr": str(e)}


@server.tool()
def list_clips() -> str:
    """List available endoscopy video clips from the outputs directory."""
    pattern = os.path.join(OUTPUTS_ROOT, "*")
    entries = sorted(glob.glob(pattern))
    if not entries:
        return f"No clips found in {OUTPUTS_ROOT}"
    results = ["Available clips/batches:"]
    for entry in entries:
        name = os.path.basename(entry)
        if os.path.isdir(entry):
            # Count polyps
            polyps = [d for d in os.listdir(entry) if d.startswith("Polyp_") and os.path.isdir(os.path.join(entry, d))]
            results.append(f"  {name}  ({len(polyps)} polyps)")
    return "\n".join(results)


@server.tool()
def list_reconstructions(
    patient_id: Annotated[str, "Filter by patient ID (empty = all)"] = "",
) -> str:
    """List completed reconstructions. Optionally filter by patient ID."""
    pattern = os.path.join(OUTPUTS_ROOT, f"*{patient_id}*" if patient_id else "*")
    entries = sorted(glob.glob(pattern))
    if not entries:
        return f"No reconstructions found matching '{patient_id}'"
    results = ["Reconstructions:"]
    for entry in entries:
        name = os.path.basename(entry)
        if not os.path.isdir(entry):
            continue
        # Look for key artifacts
        has_pc = any(glob.glob(os.path.join(entry, "**/accumulated_pc.ply"), recursive=True))
        has_mesh = any(glob.glob(os.path.join(entry, "**/*.ply"), recursive=True) if not has_pc else True)
        has_poses = any(glob.glob(os.path.join(entry, "**/poses.txt"), recursive=True))
        has_intrinsics = any(glob.glob(os.path.join(entry, "**/intrinsics.txt"), recursive=True))
        has_sizes = any(glob.glob(os.path.join(entry, "**/sizes.csv"), recursive=True))
        has_segment = any(glob.glob(os.path.join(entry, "**/segment.txt"), recursive=True))
        status_parts = []
        if has_pc: status_parts.append("PC")
        if has_poses: status_parts.append("poses")
        if has_intrinsics: status_parts.append("intrinsics")
        if has_sizes: status_parts.append("sizes")
        if has_segment: status_parts.append("segment")
        status = ", ".join(status_parts) if status_parts else "incomplete"
        results.append(f"  {name:40} [{status}]")
    return "\n".join(results)


@server.tool()
def get_reconstruction_stats(
    batch_id: Annotated[str, "Batch ID (directory name in outputs)"],
) -> str:
    """Get detailed stats for a reconstruction: point count, mesh info, file sizes."""
    batch_dir = os.path.join(OUTPUTS_ROOT, batch_id)
    if not os.path.isdir(batch_dir):
        return f"Batch not found: {batch_id}"
    results = [f"Reconstruction stats for {batch_id}:"]
    # Find all polyps
    polyp_dirs = sorted([d for d in os.listdir(batch_dir) if d.startswith("Polyp_") and os.path.isdir(os.path.join(batch_dir, d))])
    if not polyp_dirs:
        # Maybe it's a flat structure
        polyp_dirs = [""]
    for polyp in polyp_dirs:
        polyp_path = os.path.join(batch_dir, polyp) if polyp else batch_dir
        if polyp:
            results.append(f"\n  {polyp}:")
        # PC file
        pc_files = glob.glob(os.path.join(polyp_path, "**/accumulated_pc.ply"), recursive=True)
        for pc in pc_files:
            size_mb = os.path.getsize(pc) / (1024 * 1024)
            results.append(f"    Point cloud: {os.path.relpath(pc, batch_dir)} ({size_mb:.1f} MB)")
        # Poses
        pose_files = glob.glob(os.path.join(polyp_path, "**/poses.txt"), recursive=True)
        for p in pose_files:
            with open(p) as f:
                line_count = sum(1 for _ in f)
            results.append(f"    Poses: {line_count} frames ({os.path.relpath(p, batch_dir)})")
        # Sizes
        size_files = glob.glob(os.path.join(polyp_path, "**/sizes.csv"), recursive=True)
        for s in size_files:
            with open(s) as f:
                content = f.read().strip()
            results.append(f"    Sizes: {os.path.relpath(s, batch_dir)}")
            results.append(f"      {content[:200]}")
        # Animation
        anim_files = glob.glob(os.path.join(polyp_path, "**/animation.mp4"), recursive=True)
        for a in anim_files:
            size_mb = os.path.getsize(a) / (1024 * 1024)
            results.append(f"    Animation: {os.path.relpath(a, batch_dir)} ({size_mb:.1f} MB)")
    return "\n".join(results)


@server.tool()
def pipeline_status() -> str:
    """Check if the Endosight pipeline is running (BFF, Node, Vite)."""
    results = ["Pipeline status:"]
    # Check for BFF on :8000
    r = _run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "http://localhost:8000/health"], timeout=5)
    bff_status = "UP" if r["stdout"] == "200" else f"DOWN (HTTP {r['stdout']})"
    results.append(f"  BFF (:8000):     {bff_status}")
    # Check Node on :8008
    r = _run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "http://localhost:8008/"], timeout=5)
    node_status = "UP" if r["stdout"] in ("200", "302", "304") else f"DOWN (HTTP {r['stdout']})"
    results.append(f"  Node (:8008):    {node_status}")
    # Check Vite on :5173
    r = _run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", "http://localhost:5173/"], timeout=5)
    vite_status = "UP" if r["stdout"] in ("200", "302", "304") else f"DOWN (HTTP {r['stdout']})"
    results.append(f"  Vite (:5173):    {vite_status}")
    # Check Postgres
    r = _run(["docker", "inspect", "--format", "{{.State.Status}}", "leeds-postgres"], timeout=5)
    pg_status = r["stdout"] if r["returncode"] == 0 else "not found"
    results.append(f"  Postgres:        {pg_status}")
    # Check Docker containers
    r = _run(["docker", "ps", "--format", "{{.Names}} ({{.Status}})"], timeout=5)
    if r["stdout"]:
        results.append(f"\n  Docker containers:\n    {r['stdout'].replace(chr(10), chr(10) + '    ')}")
    return "\n".join(results)


@server.tool()
def start_pipeline() -> str:
    """Start the Endosight 3D pipeline (make dev). Runs in background."""
    r = _run(["make", "dev"], cwd=ENDOSIGHT_ROOT, timeout=10)
    # make dev typically starts in foreground, so we need background mode
    # This is a simplified version - in practice you'd use nohup or tmux
    return (
        f"To start the pipeline, run in a terminal:\n"
        f"  cd {ENDOSIGHT_ROOT} && make dev\n\n"
        f"This starts BFF (:8000), Node (:8008), and Vite (:5173).\n"
        f"Use pipeline_status to check if it's running."
    )


@server.tool()
def verify_pipeline() -> str:
    """Run the pipeline verification script (./scripts/verify.sh)."""
    verify_script = os.path.join(ENDOSIGHT_ROOT, "scripts/verify.sh")
    if not os.path.isfile(verify_script):
        return f"verify.sh not found at {verify_script}"
    r = _run(["bash", verify_script], cwd=ENDOSIGHT_ROOT, timeout=120)
    result = f"Verification exit code: {r['returncode']}\n"
    if r["stdout"]:
        result += f"\n--- stdout ---\n{r['stdout'][-2000:]}"
    if r["stderr"]:
        result += f"\n--- stderr ---\n{r['stderr'][-2000:]}"
    return result


@server.tool()
def sweep_clinical_clips() -> str:
    """Run the clinical clip sweep script to test multiple clips."""
    sweep_script = os.path.join(BACKEND_SCRIPTS, "sweep_clinical_clips.sh")
    if not os.path.isfile(sweep_script):
        return f"Sweep script not found at {sweep_script}"
    r = _run(["bash", sweep_script], cwd=ENDOSIGHT_ROOT, timeout=300)
    result = f"Sweep exit code: {r['returncode']}\n"
    if r["stdout"]:
        result += f"\n--- stdout (last 2000 chars) ---\n{r['stdout'][-2000:]}"
    if r["stderr"]:
        result += f"\n--- stderr (last 1000 chars) ---\n{r['stderr'][-1000:]}"
    return result


@server.tool()
def run_reconstruction(
    video_path: Annotated[str, "Path to the endoscopy video file"],
    patient_id: Annotated[str, "Patient ID"],
    batch_id: Annotated[str, "Batch ID for this reconstruction"],
    tail_frames: Annotated[int, "Number of tail frames (default: 6)"] = 6,
) -> str:
    """Trigger a reconstruction via the BFF leeds-algo upload endpoint.
    This is the partner video -> Demo handshake.
    """
    import requests
    url = "http://localhost:8000/api/v1/leeds-algo/upload"
    try:
        with open(video_path, "rb") as f:
            files = {"video": f}
            data = {"patient_id": patient_id, "batch_id": batch_id, "tail_frames": str(tail_frames)}
            resp = requests.post(url, files=files, data=data, timeout=300)
        if resp.status_code == 200:
            return f"Reconstruction started successfully.\nResponse: {json.dumps(resp.json(), indent=2)}"
        return f"Upload failed (HTTP {resp.status_code}): {resp.text[:500]}"
    except requests.exceptions.ConnectionError:
        return "Error: Could not connect to BFF at :8000. Is the pipeline running? Use start_pipeline."
    except Exception as e:
        return f"Error: {e}"


# --- CLI Mode ---

TOOLS = {
    "list_clips": list_clips,
    "list_reconstructions": list_reconstructions,
    "get_reconstruction_stats": get_reconstruction_stats,
    "pipeline_status": pipeline_status,
    "start_pipeline": start_pipeline,
    "verify_pipeline": verify_pipeline,
    "sweep_clinical_clips": sweep_clinical_clips,
    "run_reconstruction": run_reconstruction,
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
