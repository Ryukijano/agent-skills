# GPU Cluster Management and Cloud Bursting

## Description

SLURM, PBS, LSF, cloud bursting, hybrid clusters, and AWS ParallelCluster for GPU HPC.

## When to use

You are managing an on-prem or hybrid GPU cluster for training/inference.

## Key concepts

- **SLURM**: `sbatch`, `srun`, job arrays, partitions, fairshare.
- **PBS/LSF**: alternative schedulers with enterprise features.
- **Cloud bursting**: on-prem SLURM + AWS/Azure/GCP spot instances.
- **ParallelCluster**: AWS open-source HPC cluster management.
- **MIG/MPS in HPC**: partition or share GPUs across users.

## Code pattern

```bash
# Submit to SLURM
sbatch --gpus=8 --nodes=2 --ntasks-per-node=8 train.sh

# Cloud bursting config in slurm.conf
ResumeProgram=/usr/local/bin/slurm_resume
SuspendProgram=/usr/local/bin/slurm_suspend
```

## Tuning notes

- Use job arrays for hyperparameter sweeps.
- Cloud bursting needs low-latency network (Direct Connect/ExpressRoute).
- Pre-bake AMIs to meet boot-time requirements.

## Verification

1. Submit a 2-node 8-GPU job and check `squeue`/`sinfo`.
2. Verify NCCL all-reduce across on-prem and cloud nodes.
3. Test cloud burst with a small job and confirm auto-suspend after idle time.

## References

- https://slurm.schedmd.com/
- https://aws.amazon.com/hpc/parallelcluster/
- https://learn.microsoft.com/en-us/azure/cyclecloud/
- https://www.ibm.com/products/lsf
