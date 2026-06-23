---
name: debug-training
description: Symptom-driven debugging guide for NaN losses, OOM, DDP hangs, poor convergence, and low GPU utilization in PyTorch surgical video / MOT / TDV training. Pairs with the /debug-training command.
---

## Training Debug Reference

### Symptom → Root causes → Fixes

**NaN / Inf loss**
- LR too high, bad init, static frames, missing centering/sharpen in TDV targets, exploding DINO head.
- Fixes: LR /10, clamp logits, clip_grad_norm 1.0, verify rgb_diff non-zero, check EMA.

**CUDA OOM**
- Batch too large, no grad checkpointing, large ViT-B on high-res or long T.
- Fixes: halve batch + accum, gradient_checkpointing, switch to vit-s, expandable_segments, offload metrics.

**DDP hang / NCCL**
- nproc mismatch, P2P on PCIe (L40S), env drift, missing barrier.
- Fixes: NCCL_P2P_DISABLE=1, match Slurm gres to torchrun, identical envs, dist.barrier().

**Flat curves / no learning**
- Wrong params trainable (LoRA not injected, backbone frozen everywhere), data all same video, loss weight zero, LR schedule never warms up.
- Fixes: print requires_grad, check dataloader diversity, log grad/param norms.

**Low GPU util**
- CPU video decode bottleneck (use TorchCodec), low num_workers, blocking .item() in loop, tiny batch.
- Fixes: increase workers/pin_memory, profile dataloader, TorchCodec or DALI, larger effective batch.

### Always do
- 2-step smoke first.
- Log everything (config, git sha, env export).
- Apply verification gate after fix.

Related: `debug-pytorch-gpu`, `tdv-pretrain`, `surgical-mot-eval`, `systematic-debug`.
