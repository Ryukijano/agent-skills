---
name: submit-gpu-job
description: Submit a GPU training job to AIRE HPC Slurm cluster with smoke test verification and monitoring. Use when preparing to launch GPU training jobs, verifying SBATCH scripts, or monitoring running jobs.
---

## Submit GPU Job to AIRE

### Pre-submission checklist

1. Smoke test: `python <script>.py --config <config>.yaml --max-steps 2`
2. SBATCH script has: `--partition=gpu`, `--gres=gpu:l40s:<N>`, `module load cuda/12.6`
3. Conda activation and `LD_LIBRARY_PATH` set in script
4. `logs/` directory exists
5. NCCL workarounds for L40S PCIe: `NCCL_P2P_DISABLE=1`, `NCCL_CUMEM_ENABLE=0`

### Submit and monitor

```bash
sbatch jobs/<name>.slurm
squeue -j <JOBID>
tail -f logs/<name>_<JOBID>.out
```

### Post-run

```bash
seff <JOBID>  # Check GPU util >70%, memory <80%
```
