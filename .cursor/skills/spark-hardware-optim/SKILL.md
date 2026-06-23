---
name: spark-hardware-optim
description: Performance and memory optimization on DGX Spark (GB10 Grace Blackwell 128 GB unified) and AIRE L40S nodes for large vision / video models (DINOv2, Cosmos3, etc.).
---

## Hardware Optimization Notes

### GB10 Spark
- 128 GB unified memory is a big advantage for long context / large batches, but still watch fragmentation.
- `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` often helps.
- For DINOv2: ViT-S comfortable; ViT-B needs care with T and batch.
- XFORMERS may need disabling on some GB10 setups for stability.

### L40S (AIRE)
- 48 GB per GPU; 3 per node typical.
- No NVLink → NCCL_P2P_DISABLE=1 recommended.
- Good for 3-GPU DDP with batch 8–12 per GPU for ViT-B TDV/MOT.

### General
- Profile before optimizing (torch.profiler or nvidia tools).
- Prefer data-parallel over model-parallel for these workloads unless justified.
- Parallelize dataloaders and prefetch.

Related: `debug-pytorch-gpu`, `dgx-spark-cosmos3`.
