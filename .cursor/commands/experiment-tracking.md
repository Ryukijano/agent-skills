# Experiment Tracking Setup & Run

1. At start of session: `wandb login` (or use env var on cluster).
2. In code: init with full config + tags + group for ablations.
3. Log train metrics every N steps with explicit step=.
4. Log val at epoch or eval points; include per-tool breakdown for MOT.
5. For DDP: only init/log on rank 0.
6. For Slurm/offline: set WANDB_MODE=offline + WANDB_DIR=/scratch/...; sync after.
7. After run or sweep: pull summary table via API or UI; export to CSV for paper.
8. Record failed runs with tags like "nan", "oom", "no-learning".
9. At end of major phase: generate comparison table in `experiments/<phase>/results.md`.

Apply `experiment-tracking`, `wandb-experiment`, `reproducibility`.
