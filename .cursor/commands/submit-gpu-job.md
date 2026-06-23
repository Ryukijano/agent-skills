# Submit GPU Job (AIRE)

Submit a training or eval job to University of Leeds AIRE Slurm (L40S 48GB).

## Prerequisites
- Code committed or on feature branch.
- Local smoke test passed (`max_steps: 2` or 5-step train + eval).
- `jobs/<name>.slurm` exists and is executable.
- Logs dir: `mkdir -p logs`.

## 1. Prepare job script (use aire-slurm-submit skill)
Typical header:
```bash
#!/bin/bash
#SBATCH --job-name=tdv-pretrain-vitb
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:3
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=3
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=24:00:00
#SBATCH --output=logs/tdv_%j.out
#SBATCH --error=logs/tdv_%j.err

source /scratch/kcwp264/conda/etc/profile.d/conda.sh
conda activate <env>
export LD_LIBRARY_PATH=...   # for TorchCodec if needed
export NCCL_P2P_DISABLE=1

torchrun --nproc_per_node=3 scripts/pretrain_tdv.py --config configs/... --ddp
```

## 2. Smoke on login node or interactive
```bash
srun --partition=gpu --gres=gpu:l40s:1 --cpus-per-task=4 --mem=32G --time=00:30:00 --pty bash
# inside: python ... --max_steps 2
```

## 3. Submit
```bash
sbatch jobs/<name>.slurm
```
Note the JOBID.

## 4. Monitor
```bash
squeue -u $USER
tail -f logs/<name>_<JOBID>.out
tail -f logs/<name>_<JOBID>.err
seff <JOBID>   # after completion: GPU util, MaxRSS, etc.
```

## 5. Post-run
- If GPU util < 60% or MaxRSS > 90% of alloc: adjust for next run.
- Sync WandB if offline: `wandb sync wandb/offline-run-*/`
- Save key metrics to `results/<JOBID>-summary.md`.

## 6. Common failures
- Quota: move outputs to $SCRATCH or purge.
- Env not found on compute: install in /scratch conda, not $HOME.
- NCCL: add the env vars above.
- Time limit: request more or checkpoint more frequently.

Apply skill `aire-slurm-submit` for details and templates.

Always run targeted verification (smoke + narrow eval) after job completes before declaring success.
