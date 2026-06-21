# Submit GPU Job (AIRE)

Submit a GPU training job to University of Leeds AIRE Slurm (L40S).

Apply skill: `aire-slurm-submit`.

1. Smoke-test locally for 1–2 steps.
2. Verify `jobs/<name>.slurm` (partition=gpu, gres=gpu:l40s:N, cuda/12.6, conda).
3. `sbatch jobs/<name>.slurm` → monitor with `squeue`, `tail -f logs/`, `seff`.

Full procedure: `.windsurf/workflows/submit-gpu-job.md`
