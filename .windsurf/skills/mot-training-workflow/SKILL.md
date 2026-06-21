---
name: mot-training-workflow
description: >-
  Runs the four-stage surgical MOT training and eval pipeline for
  Gyanateet_tracking: conda env, stage configs, checkpoint chaining, HOTA eval,
  and smoke-stratified metrics. Use when training, resuming, evaluating, or
  debugging MOT stages.
---

# MOT Training Workflow

## Environment

```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track   # fallback: surgi_world_track_cuda
export XFORMERS_DISABLED=1   # GB10 DINOv2
```

## Stage pipeline

| Stage | Config | Output dir | Loads from |
|-------|--------|------------|------------|
| 1 Supervised teacher | `configs/train_mot/dinov2/cholec20-mot-stage1-supervised.yaml` | `outputs/mot/cholec20-stage1-supervised/` | — |
| 2 GOT-JEPA SSL | `configs/train_mot/dinov2/cholec80-ct20-stage2-jepa-pretrain.yaml` | `outputs/mot/cholec80-ct20-stage2-jepa-pretrain/` | Stage 1 `best.pth.tar` |
| 3 Joint finetune | `configs/train_mot/dinov2/cholec20-mot-stage3-joint-finetune-vits.yaml` | `outputs/mot/cholec20-stage3-joint-finetune-vits/` | Stage 2 `latest.pth.tar` |
| 4 Lean (recommended) | `configs/train_mot/dinov2/cholec20-mot-stage4-lean.yaml` | `outputs/mot/cholec20-stage4-lean-vits/` | Stage 3 `best.pth.tar` |

Entry: `python -m core_app.mot.main --fname <config> --devices cuda:0`

## Launch scripts

```bash
# Stage 1 (auto GPU count)
bash scripts/train_stage1_ddp_3gpu.sh

# Stages 2–4 (resume prior checkpoint)
bash scripts/run_mot_stage2.sh
bash scripts/run_mot_stage3.sh
bash scripts/run_mot_stage4.sh
```

## Stage semantics (do not confuse)

- **Stage 1:** `detector_only: true` — precision-lean pseudo-label teacher, not final detector
- **Stage 2:** `encode_frames` + `GOTJEPAWrapper` only — teacher frozen, no OccuSolver training
- **Stage 3:** Full MOT losses (det + track + reid)
- **Stage 4 lean:** CoTracker + Depth-Anything; prefer over Stage 4 full unless ablating VGGT geometry

## Eval

```bash
# HOTA + smoke stratification
python scripts/eval_checkpoint.py --mot-eval --stratify-smoke \
  --checkpoint outputs/mot/cholec20-stage3-joint-finetune-vits/best.pth.tar

python scripts/eval_mot_hota.py --checkpoint <path>
```

Tune tracker gates if zero predictions: lower `birth_score`, reduce `min_hits`.

## Verification gate

Before marking training changes done:

```bash
pytest tests/test_mot_smoke.py -q
```

## Hardware notes

- **GB10 Spark:** `batch_size` 24–32 Stage 1; `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` for long runs
- **Aire L40S:** multi-GPU DDP for sweeps; use `scripts/slurm_*.sh` variants when on cluster

## Current status (Jun 2026)

See `AGENTS.md` for checkpoint paths, val mAP, and blockers (weak detection, no full HOTA yet, `depth_stub: true` in S4 lean).
