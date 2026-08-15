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

import requests

from mcp.server import MCPServer

server = MCPServer("endosight-pipeline", "1.0.0")

# Canonical paths from AGENTS.md
ENDOSIGHT_ROOT = "/home/aimsgroupuol/endosight_project/endosight-3d"
BFF_URL = os.environ.get("BFF_URL", "http://localhost:8000")
BACKEND_SCRIPTS = os.path.join(ENDOSIGHT_ROOT, "backend", "scripts")


def _resolve_outputs_root() -> str:
    """Resolve the outputs root, falling back to the active backend/vis/outputs."""
    candidates = [
        os.environ.get("OUTPUTS_ROOT"),
        os.path.join(ENDOSIGHT_ROOT, "vis", "outputs"),
        os.path.join(ENDOSIGHT_ROOT, "backend", "vis", "outputs"),
    ]
    for c in candidates:
        if c and os.path.isdir(c):
            return c
    # Nothing exists yet; create a sensible default.
    if os.path.isdir(os.path.join(ENDOSIGHT_ROOT, "backend", "vis")):
        default = os.path.join(ENDOSIGHT_ROOT, "backend", "vis", "outputs")
    else:
        default = os.path.join(ENDOSIGHT_ROOT, "vis", "outputs")
    try:
        os.makedirs(default, exist_ok=True)
    except Exception as exc:
        print(f"Warning: could not create OUTPUTS_ROOT {default}: {exc}", file=sys.stderr)
    return default


OUTPUTS_ROOT = _resolve_outputs_root()


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


def _find_script(name: str) -> str | None:
    """Look for a script in common Endosight script directories."""
    search_dirs = [
        ENDOSIGHT_ROOT,
        os.path.join(ENDOSIGHT_ROOT, "scripts"),
        BACKEND_SCRIPTS,
        os.path.join(ENDOSIGHT_ROOT, "backend", "pipeline", "scripts", "orchestrate"),
    ]
    for d in search_dirs:
        p = os.path.join(d, name)
        if os.path.isfile(p):
            return p
    return None


def _find_batch_dir(batch_id: str | int) -> str | None:
    """Find a batch directory whose name matches or contains batch_id."""
    batch_id = str(batch_id)
    if not batch_id or not os.path.isdir(OUTPUTS_ROOT):
        return None
    exact = os.path.join(OUTPUTS_ROOT, batch_id)
    if os.path.isdir(exact):
        return exact
    pattern = os.path.join(OUTPUTS_ROOT, "**", f"*{batch_id}*")
    for candidate in glob.glob(pattern, recursive=True):
        if os.path.isdir(candidate):
            return candidate
    return None


def _probe_http(url: str, paths: tuple[str, ...] = ("/",), valid_codes: set[str] | None = None) -> tuple[str, str]:
    """Return (status, code) for an HTTP probe."""
    if valid_codes is None:
        valid_codes = {"200", "201", "204", "301", "302", "303", "304", "307", "308", "404"}
    code = "000"
    for path in paths:
        full = (url.rstrip("/") + path) if path else url.rstrip("/")
        r = _run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", full], timeout=5)
        code = r["stdout"].strip() or "000"
        if code in valid_codes:
            return "UP", code
        if code == "000":
            return "DOWN", code
    if code in valid_codes:
        return "UP", code
    return "DOWN", code


@server.tool()
def list_clips() -> str:
    """List available endoscopy video clips from the outputs directory."""
    if not os.path.isdir(OUTPUTS_ROOT):
        return f"Outputs root missing or inaccessible: {OUTPUTS_ROOT}"
    pattern = os.path.join(OUTPUTS_ROOT, "*")
    entries = sorted(glob.glob(pattern))
    if not entries:
        return f"No clips found in {OUTPUTS_ROOT}"
    results = [f"Available clips/batches (under {OUTPUTS_ROOT}):"]
    for entry in entries:
        name = os.path.basename(entry)
        if os.path.isdir(entry):
            # Count polyps
            try:
                polyps = [d for d in os.listdir(entry) if d.startswith("Polyp_") and os.path.isdir(os.path.join(entry, d))]
            except (OSError, PermissionError):
                polyps = []
            results.append(f"  {name}  ({len(polyps)} polyps)")
    return "\n".join(results)


@server.tool()
def list_reconstructions(
    patient_id: Annotated[str, "Filter by patient ID (empty = all)"] = "",
) -> str:
    """List completed reconstructions. Optionally filter by patient ID."""
    if not os.path.isdir(OUTPUTS_ROOT):
        return f"Outputs root missing or inaccessible: {OUTPUTS_ROOT}"
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
        has_pc = has_pc or any(glob.glob(os.path.join(entry, "**/reconstructed_pc.ply"), recursive=True))
        has_pc = has_pc or any(glob.glob(os.path.join(entry, "**/plain_reconstructed_pc.ply"), recursive=True))
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
    batch_id = str(batch_id)
    batch_dir = _find_batch_dir(batch_id)
    if not batch_dir:
        batch_dir = os.path.join(OUTPUTS_ROOT, batch_id)
    if not os.path.isdir(batch_dir):
        return f"Batch not found: {batch_id}"
    results = [f"Reconstruction stats for {batch_id}:"]
    # Find all polyps
    try:
        polyp_dirs = sorted([d for d in os.listdir(batch_dir) if d.startswith("Polyp_") and os.path.isdir(os.path.join(batch_dir, d))])
    except (OSError, PermissionError):
        polyp_dirs = []
    if not polyp_dirs:
        # Maybe it's a flat structure
        polyp_dirs = [""]
    for polyp in polyp_dirs:
        polyp_path = os.path.join(batch_dir, polyp) if polyp else batch_dir
        if polyp:
            results.append(f"\n  {polyp}:")
        # PC file
        pc_patterns = ["**/accumulated_pc.ply", "**/reconstructed_pc.ply", "**/plain_reconstructed_pc.ply"]
        pc_files = []
        for p in pc_patterns:
            pc_files += glob.glob(os.path.join(polyp_path, p), recursive=True)
        pc_files = sorted(set(pc_files))
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
    """Check if the Endosight pipeline is running (BFF, Node, Vite, Postgres)."""
    results = ["Pipeline status:"]

    # BFF on :8000 (or BFF_URL)
    bff_status, bff_code = _probe_http(f"{BFF_URL}/health", paths=("",), valid_codes={"200"})
    results.append(f"  BFF ({BFF_URL}/health):  {bff_status} (HTTP {bff_code})")

    # Node on :8008
    node_status, node_code = _probe_http("http://localhost:8008", paths=("/index.html", "/"))
    results.append(f"  Node (:8008):          {node_status} (HTTP {node_code})")

    # Vite on :5173 — 404 on root is common; probe index.html first, but accept 2xx/3xx/404
    vite_status, vite_code = _probe_http("http://localhost:5173", paths=("/index.html", "/"))
    results.append(f"  Vite (:5173):          {vite_status} (HTTP {vite_code})")

    # Postgres
    r = _run(["docker", "inspect", "--format", "{{.State.Status}}", "leeds-postgres"], timeout=5)
    pg_status = r["stdout"] if r["returncode"] == 0 else "not found"
    results.append(f"  Postgres (leeds-postgres): {pg_status}")

    # Docker containers
    r = _run(["docker", "ps", "--format", "{{.Names}} ({{.Status}})"], timeout=5)
    if r["stdout"]:
        results.append(f"\n  Docker containers:\n    {r['stdout'].replace(chr(10), chr(10) + '    ')}")

    # Summary
    up_services = []
    if bff_status == "UP":
        up_services.append("BFF")
    if node_status == "UP":
        up_services.append("Node")
    if vite_status == "UP":
        up_services.append("Vite")
    if pg_status == "running":
        up_services.append("Postgres")

    total = 4
    if len(up_services) == total:
        summary = "healthy"
    elif len(up_services) >= 2:
        summary = "degraded"
    else:
        summary = "down"
    results.append(f"\n  Summary: {len(up_services)}/{total} core services up ({summary}).")
    results.append(f"  Services up: {', '.join(up_services) if up_services else 'none'}")

    return "\n".join(results)


@server.tool()
def start_pipeline() -> str:
    """Start the Endosight 3D pipeline (make dev) in the background."""
    try:
        proc = subprocess.Popen(
            ["make", "dev"],
            cwd=ENDOSIGHT_ROOT,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except Exception as exc:
        return (
            f"Failed to launch pipeline: {exc}\n"
            f"Make sure 'make' is installed and a Makefile is present under {ENDOSIGHT_ROOT}."
        )
    return (
        f"Pipeline launch initiated (PID {proc.pid}) from {ENDOSIGHT_ROOT}.\n"
        "make dev is running in the background. The full stack (Postgres, BFF :8000, Node :8008, Vite :5173) typically takes ~60 seconds to become healthy.\n"
        "Use pipeline_status to check readiness."
    )


@server.tool()
def verify_pipeline() -> str:
    """Run the pipeline verification script (./scripts/verify.sh)."""
    verify_script = _find_script("verify.sh")
    if not verify_script:
        return f"verify.sh not found under {ENDOSIGHT_ROOT}"
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
    url = f"{BFF_URL}/api/v1/leeds-algo/upload"
    try:
        with open(video_path, "rb") as f:
            files = {"video": f}
            data = {"patient_id": patient_id, "batch_id": batch_id, "tail_frames": str(tail_frames)}
            resp = requests.post(url, files=files, data=data, timeout=300)
        if resp.status_code == 200:
            return f"Reconstruction started successfully.\nResponse: {json.dumps(resp.json(), indent=2)}"
        return f"Upload failed (HTTP {resp.status_code}): {resp.text[:500]}"
    except requests.exceptions.ConnectionError:
        return f"Error: Could not connect to BFF at {BFF_URL}. Is the pipeline running? Use start_pipeline."
    except Exception as e:
        return f"Error: {e}"


@server.tool()
def run_crop(
    batch_id: Annotated[str, "Batch ID to crop (optional)"] = "",
    video_path: Annotated[str, "Optional video path for cropping"] = "",
) -> str:
    """Trigger frame/clip cropping for a batch via the BFF crop endpoint or a local script."""
    batch_id = str(batch_id)
    # Try the BFF crop endpoint first
    try:
        url = f"{BFF_URL}/api/v1/leeds-algo/crop"
        payload: dict[str, str] = {}
        if batch_id:
            payload["batch_id"] = batch_id
        if video_path:
            payload["video_path"] = video_path
        resp = requests.post(url, json=payload, timeout=30)
        if resp.status_code in (200, 202):
            return f"Crop triggered via BFF.\nResponse: {resp.text[:500]}"
        if resp.status_code == 404:
            pass  # endpoint not available, fall through to script/instructions
        else:
            return f"BFF crop endpoint returned HTTP {resp.status_code}: {resp.text[:500]}"
    except requests.exceptions.ConnectionError:
        pass  # BFF not reachable, try script
    except Exception as exc:
        return f"Error calling BFF crop endpoint: {exc}"

    # Fall back to a local run_crop.sh if it exists
    crop_script = _find_script("run_crop.sh")
    if crop_script:
        cmd = ["bash", crop_script]
        if batch_id:
            cmd.append(batch_id)
        if video_path:
            cmd.append(video_path)
        r = _run(cmd, cwd=ENDOSIGHT_ROOT, timeout=120)
        result = f"run_crop.sh exit code: {r['returncode']}\n"
        if r["stdout"]:
            result += f"\n--- stdout ---\n{r['stdout'][-2000:]}"
        if r["stderr"]:
            result += f"\n--- stderr ---\n{r['stderr'][-1000:]}"
        return result

    return (
        "No BFF crop endpoint or local run_crop.sh is available.\n"
        "To crop locally, run the reconstruction pipeline with cropping enabled:\n"
        f"  python {ENDOSIGHT_ROOT}/backend/pipeline/reconstruction/run_reconstruction_pipeline.py "
        f"--video_path <clip> --output_dir <dir> [--crop]"
    )


@server.tool()
def run_qa(
    batch_id: Annotated[str, "Batch ID to check QA status for"],
) -> str:
    """Run QA script or return QA status for a batch."""
    batch_id = str(batch_id)
    # Try a local scripts/qa.sh if it exists
    qa_script = _find_script("qa.sh")
    if qa_script:
        r = _run(["bash", qa_script, batch_id], cwd=ENDOSIGHT_ROOT, timeout=120)
        result = f"QA script exit code: {r['returncode']}\n"
        if r["stdout"]:
            result += f"\n--- stdout ---\n{r['stdout'][-2000:]}"
        if r["stderr"]:
            result += f"\n--- stderr ---\n{r['stderr'][-1000:]}"
        return result

    # Try to derive QA status from local reconstruction summary
    batch_dir = _find_batch_dir(batch_id)
    if batch_dir:
        summary_files = glob.glob(os.path.join(batch_dir, "**/reconstruction_summary.json"), recursive=True)
        for s in summary_files:
            try:
                with open(s) as f:
                    summary = json.load(f)
            except Exception:
                continue
            qa = summary.get("qa_gating") or summary.get("qa")
            if qa:
                return f"QA status for {batch_id} (from {os.path.relpath(s, OUTPUTS_ROOT)}):\n{json.dumps(qa, indent=2)}"

    # Try the BFF per-polyp status endpoint
    try:
        url = f"{BFF_URL}/api/v1/leeds-algo/recon/{batch_id}/Polyp_1/status"
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            qa = data.get("qa_gating") or data.get("qa")
            if qa:
                return f"QA status for {batch_id} (from BFF):\n{json.dumps(qa, indent=2)}"
            return f"BFF status for {batch_id}:\n{json.dumps(data, indent=2)}"
        if resp.status_code == 404:
            return f"QA status not available for batch {batch_id} (BFF returned 404)."
        return f"Could not fetch QA status for {batch_id}: HTTP {resp.status_code} {resp.text[:200]}"
    except requests.exceptions.ConnectionError:
        return f"BFF at {BFF_URL} is not reachable. Cannot retrieve QA status for {batch_id}."
    except Exception as exc:
        return f"Error fetching QA status for {batch_id}: {exc}"


@server.tool()
def run_video_export(
    batch_id: Annotated[str, "Batch ID to export video for"],
    polyp_key: Annotated[str, "Polyp key (default: Polyp_1)"] = "Polyp_1",
) -> str:
    """Trigger video export for a batch via the BFF export endpoint or a local script."""
    batch_id = str(batch_id)
    # Try the BFF video export endpoint
    try:
        url = f"{BFF_URL}/api/v1/leeds-algo/export/{batch_id}"
        resp = requests.post(url, json={"polyp_key": polyp_key}, timeout=30)
        if resp.status_code in (200, 202):
            return f"Video export triggered for {batch_id}.\nResponse: {resp.text[:500]}"
        if resp.status_code == 404:
            pass  # endpoint not available, fall through
        else:
            return f"BFF export endpoint returned HTTP {resp.status_code}: {resp.text[:500]}"
    except requests.exceptions.ConnectionError:
        pass
    except Exception as exc:
        return f"Error calling BFF export endpoint: {exc}"

    # Fall back to a local export_video.sh
    export_script = _find_script("export_video.sh")
    if export_script:
        r = _run(["bash", export_script, batch_id, polyp_key], cwd=ENDOSIGHT_ROOT, timeout=180)
        result = f"export_video.sh exit code: {r['returncode']}\n"
        if r["stdout"]:
            result += f"\n--- stdout ---\n{r['stdout'][-2000:]}"
        if r["stderr"]:
            result += f"\n--- stderr ---\n{r['stderr'][-1000:]}"
        return result

    return (
        f"No BFF export endpoint or local export_video.sh is available for batch {batch_id}.\n"
        "To export a finished reconstruction manually, use:\n"
        f"  python -m pipeline.bff.leeds_algo_bridge export_leeds_polyps_from_run "
        f"<run_dir> <export_dir> --source_video <video>"
    )


@server.tool()
def pipeline_logs(
    service: Annotated[str, "Service to fetch logs for (bff, node, postgres, frontend)"],
    lines: Annotated[int, "Number of tail lines (default: 100)"] = 100,
) -> str:
    """Fetch recent Docker logs for a pipeline service."""
    containers = {
        "bff": "endosight-bff",
        "node": "endosight-node",
        "postgres": "leeds-postgres",
        "frontend": "endosight-frontend",
        "vite": "endosight-frontend",
    }
    service = service.lower()
    if service not in containers:
        return f"Unknown service: {service}. Choose from {', '.join(containers.keys())}."
    container = containers[service]
    r = _run(["docker", "logs", "--tail", str(lines), container], timeout=30)
    header = f"Docker logs for {service} ({container}, last {lines} lines):"
    if r["returncode"] != 0:
        return f"{header}\nCould not read logs: {r['stderr'] or r['stdout']}"
    return f"{header}\n\n{r['stdout'][-4000:]}"


# Expected Demo-shaped artifacts that should exist after a successful reconstruction + export
_DEMO_ARTIFACTS = [
    (("animation.mp4",), "animation"),
    (("sizes.csv",), "sizes report"),
    (("segment.txt",), "segment label"),
    (("poses.txt",), "poses"),
    (("frame.png",), "thumbnail"),
    (("polyp_highlight.png",), "highlight"),
    (("accumulated_pc.ply", "reconstructed_pc.ply", "plain_reconstructed_pc.ply", "fused_polyp_points.ply"), "point cloud/mesh"),
]


@server.tool()
def validate_reconstruction(
    batch_id: Annotated[str, "Batch ID to validate"],
) -> str:
    """Check if the expected Demo-shaped artifacts exist for a batch under the outputs root."""
    batch_id = str(batch_id)
    if not os.path.isdir(OUTPUTS_ROOT):
        return f"Outputs root missing or inaccessible: {OUTPUTS_ROOT}"

    batch_dir = _find_batch_dir(batch_id)
    if not batch_dir:
        return f"No batch matching '{batch_id}' found under {OUTPUTS_ROOT}"

    results = [f"Validation for batch '{batch_id}' (under {OUTPUTS_ROOT}):"]
    results.append(f"  Candidate: {os.path.relpath(batch_dir, OUTPUTS_ROOT)}")

    all_present = True
    for patterns, label in _DEMO_ARTIFACTS:
        hits = []
        for p in patterns:
            hits += glob.glob(os.path.join(batch_dir, "**", p), recursive=True)
        if hits:
            results.append(f"    [OK] {label}: {os.path.relpath(hits[0], batch_dir)}")
        else:
            all_present = False
            results.append(f"    [MISSING] {label} (looked for {', '.join(patterns)})")

    if all_present:
        results.append(f"\n  -> All Demo artifacts present for {os.path.basename(batch_dir)}.")
    else:
        results.append(f"\n  -> Batch {batch_id} is missing some Demo artifacts.")
    return "\n".join(results)


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
    "run_crop": run_crop,
    "run_qa": run_qa,
    "run_video_export": run_video_export,
    "pipeline_logs": pipeline_logs,
    "validate_reconstruction": validate_reconstruction,
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
