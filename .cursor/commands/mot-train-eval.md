# MOT Train / Eval

End-to-end driver for the four-stage surgical MOT pipeline.

## Env (always)
```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track
export XFORMERS_DISABLED=1
```

## Quick start by stage
- **Stage 1 (teacher)**: `bash scripts/train_stage1_ddp_3gpu.sh` or single-GPU with `--max_steps N`.
- **Stage 2 (SSL/JEPA)**: `bash scripts/run_mot_stage2.sh` (loads prior teacher).
- **Stage 3 (joint)**: `bash scripts/run_mot_stage3.sh`.
- **Stage 4 lean (recommended)**: `bash scripts/run_mot_stage4.sh`.

See `mot-training-workflow` skill for stage semantics and config paths.

## Eval after training
Use `/mot-hota-eval` or directly:
```bash
python scripts/eval_checkpoint.py --mot-eval --stratify-smoke --checkpoint <path>
python scripts/eval_mot_hota.py --checkpoint <path>
```

## Smoke discipline
Before any long run:
- 2–5 step forward on the exact config.
- `pytest tests/test_mot_smoke.py -q`.

## Resuming
Most stages support `--resume outputs/.../latest.pth.tar`.

## When stuck
Apply `/debug-training` + `debug-pytorch-gpu` skill.

Apply skill: `mot-training-workflow`.
