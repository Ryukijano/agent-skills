---
name: submit-gpu-job
description: Knowledge for submitting, monitoring, and post-processing GPU training jobs on AIRE (University of Leeds) Slurm cluster with L40S nodes. Companion to the /submit-gpu-job command.
---

## AIRE Slurm Reference

### Resources
- Partition: gpu
- GPU: l40s (48 GB)
- Max practical per job: 3 GPUs (no NVLink; use NCCL_P2P_DISABLE=1)
- Storage: $HOME quota tight; use $SCRATCH for large outputs (ephemeral)

### Key SBATCH knobs
--gres=gpu:l40s:N
--cpus-per-task=8 (or more)
--mem=96G for 3-GPU
--time=24:00:00 typical

### Monitoring
squeue, sacct, seff <JOBID>, tail logs/*_<JOBID>.err

### Post-job
- seff for GPU util / memory high-water
- wandb sync if offline
- Move artifacts off $SCRATCH if needed before purge

### Pitfalls
- Conda env installed on login node not visible on compute → install under /scratch
- LD_LIBRARY_PATH for TorchCodec / FFmpeg
- HOME quota → set conda pkgs dir to scratch

Related: `aire-slurm-submit`, `debug-pytorch-gpu`, `wandb-experiment`.
