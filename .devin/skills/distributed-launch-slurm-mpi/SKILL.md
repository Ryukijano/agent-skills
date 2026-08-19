# Distributed Launch: SLURM, torchrun, MPI, and UCX

## Description

Launching multi-node PyTorch/JAX training with SLURM, torchrun, MPI, CUDA-aware MPI, and UCX.

## When to use

You are running distributed training on a cluster and need to choose/configure the launcher.

## Key concepts

- **torchrun**: PyTorch native; auto-sets RANK, WORLD_SIZE, LOCAL_RANK, MASTER_ADDR.
- **srun (SLURM)**: direct process spawning; set env vars manually.
- **mpirun (Open MPI / MVAPICH2)**: for HPC workloads.
- **CUDA-aware MPI**: pass GPU buffers directly without staging.
- **UCX**: transports `rc` (RDMA), `sm` (shared memory), `cuda_copy`, `cuda_ipc`, `gdr_copy`.

## Code pattern

```bash
# SLURM + torchrun
srun --nodes=2 --ntasks-per-node=8 --gpus-per-node=8   torchrun --nnodes=2 --nproc_per_node=8 train.py
```

For MPI:

```bash
mpirun -np 16 -x LD_LIBRARY_PATH -x NCCL_DEBUG=INFO   -bind-to none -map-by ppr:8:node ./train_mpi
```

## Tuning notes

- Set `UCX_TLS=rc,sm,cuda_copy,cuda_ipc` for InfiniBand.
- For MNNVL/GB200: `UCX_CUDA_IPC_ENABLE_MNNVL=1`.
- Use `--gpu-bind=none` in SLURM unless you want explicit GPU binding.

## Verification

1. Run `nccl-tests/all_reduce_perf` with your launcher.
2. Check `NCCL_DEBUG=INFO` ranks and chosen transports.
3. Confirm each process sees the correct `LOCAL_RANK` and GPU.

## References

- https://docs.pytorch.org/tutorials/intermediate/ddp_series_multinode.html
- https://docs.nersc.gov/machinelearning/launchers/
- https://developer.nvidia.com/blog/introduction-cuda-aware-mpi/
- https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/ucx.html
