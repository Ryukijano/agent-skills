# MOT Train / Eval

# MOT stage training (Stages 1–4)

**Macro:** `!mot-train-eval`

## Procedure

### Setup
- `BASE=/home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking`
- `conda activate surgi_track` (fallback: `surgi_world_track_cuda`)
- `export XFORMERS_DISABLED=1` on GB10 for DINOv2
- Read `.cursor/skills/mot-training-workflow/SKILL.md`

### Choose stage
| Stage | Script | Config |
|-------|--------|--------|
| 1 | `bash scripts/train_stage1_ddp_3gpu.sh` | `cholec20-mot-stage1-supervised.yaml` |
| 2 | `bash scripts/run_mot_stage2.sh` | `cholec80-ct20-stage2-jepa-pretrain.yaml` |
| 3 | `bash scripts/run_mot_stage3.sh` | `cholec20-mot-stage3-joint-finetune-vits.yaml` |
| 4 lean | `bash scripts/run_mot_stage4.sh` | `cholec20-mot-stage4-lean.yaml` |

### Verify
- `pytest tests/test_mot_smoke.py -q` after code or config changes.
- Report checkpoint path, epoch, and val mAP if available.

## Specifications
- Stage 1: `detector_only: true` (pseudo-label teacher).
- Stage 2: `GOTJEPAWrapper` only — no `model.forward()` or OccuSolver training.
- Stage 4 lean preferred over Stage 4 full unless ablating VGGT geometry.

## Advice
- Spark GB10: `batch_size` 24–32 Stage 1; single-GPU baseline.
- Leeds Aire: 6+ L40S DDP for HP sweeps via `scripts/slurm_*.sh`.
