---
name: aire-slurm-submit
description: Submit and monitor Slurm jobs on the University of Leeds AIRE HPC cluster. Use when submitting GPU training jobs, checking job status, debugging Slurm failures, or managing compute allocations on AIRE L40S nodes.
---

## AIRE HPC Slurm Job Submission

### Cluster overview
- **Partition**: `gpu` (NVIDIA L40S, 48GB VRAM, max 3 GPUs per node)
- **Login nodes**: `login[1-3].aire.lee.alces.network`
- **Compute nodes**: `gpu[0XX].aire.lee.alces.network`
- **Storage**: `$HOME` (quota-limited), `$SCRATCH` (high-speed, purged)

### Standard SBATCH template

```bash
#!/bin/bash
#SBATCH --job-name=<name>
#SBATCH --partition=gpu
#SBATCH --gres=gpu:l40s:<N>
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=<N>
#SBATCH --cpus-per-task=8
#SBATCH --mem=96G
#SBATCH --time=24:00:00
#SBATCH --output=logs/<name>_%j.out
#SBATCH --error=logs/<name>_%j.err
```

### Key commands

- **Submit**: `sbatch jobs/<script>.slurm`
- **Interactive**: `srun --partition=gpu --gres=gpu:l40s:1 --cpus-per-task=8 --mem=32G --time=02:00:00 --pty bash`
- **Status**: `squeue -u $USER` or `sacct -j <JOBID> --format=JobID,JobName,State,Elapsed,MaxRSS`
- **Cancel**: `scancel <JOBID>`
- **Efficiency**: `seff <JOBID>` (check GPU utilization post-run)
- **Node info**: `sinfo -p gpu -o "%n %G %c %m %T"`

### Common pitfalls

1. **GPU not detected**: Add `export CUDA_VISIBLE_DEVICES=0,1,2` to script
2. **OOM**: Reduce batch_size or use gradient accumulation; L40S has 48GB
3. **DDP hang**: Ensure `--nproc_per_node` matches `--gres=gpu:l40s:N`
4. **Module load**: Use `module load cuda/12.6` before activating conda
5. **Scratch purge**: Check `$SCRATCH` purge policy; move checkpoints to `$HOME` or project dir
6. **Conda on compute nodes**: Source conda before activating: `source /scratch/kcwp264/conda/etc/profile.d/conda.sh`

### Monitoring during training

```bash
# Watch job output in real-time
tail -f logs/<name>_<JOBID>.out

# Check GPU utilization on running job's node
srun --jobid=<JOBID> nvidia-smi

# Check if job is still running
squeue -j <JOBID>
```

### Environment setup for compute nodes

```bash
module load cuda/12.6
source /scratch/kcwp264/conda/etc/profile.d/conda.sh
conda activate <env_name>
export LD_LIBRARY_PATH=/scratch/kcwp264/conda/envs/<env_name>/lib:$LD_LIBRARY_PATH
```
