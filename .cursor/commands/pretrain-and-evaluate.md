# Pretrain and Evaluate

Full TDV pretrain → Stage 1 detection → eval pipeline on AIRE.

Apply skills: `tdv-pretrain`, `surgical-mot-eval`, `wandb-experiment`.

1. Smoke-test `scripts/pretrain_tdv.py` with `max_steps: 2`.
2. Submit full job: `sbatch jobs/tdv-pretrain.slurm` (see `aire-slurm-submit`).
3. Point detection config at `outputs/tdv_pretrain/tdv_frame_encoder.pth`.
4. Run `scripts/eval_checkpoint.py --mot-eval --stratify-smoke` and compare to baseline.

Full procedure: `.windsurf/workflows/pretrain-and-evaluate.md`
