# Mixed Precision Training on NVIDIA GPUs

## Description

BF16, FP16, FP8, TF32, FP32 master weights, loss scaling, and when to use each on Ampere/Hopper/Blackwell.

## When to use

You are training deep learning models and want to choose the right precision and scaling strategy for your GPU.

## Key concepts

- **BF16**: 8 exponent / 7 mantissa bits. FP32-like range, no loss scaling needed. Best on Ampere+.
- **FP16**: 5 exponent / 10 mantissa bits. Needs dynamic loss scaling to avoid underflow/overflow.
- **FP32 master weights**: store optimizer state in FP32; forward/backward in lower precision.
- **FP8**: E4M3 forward, E5M2 backward. Use Transformer Engine with current, delayed, or blockwise scaling.
- **TF32**: not a storage format; FP32 matmul uses Tensor Cores. Default on Ampere+.

## Code pattern

```python
import torch
from torch.amp import autocast, GradScaler

scaler = GradScaler()
for x, y in loader:
    with autocast(device_type='cuda', dtype=torch.bfloat16):
        loss = model(x, y)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## Tuning notes

- Keep softmax, LayerNorm, and first/last layers in FP32 for stability.
- Use BF16 on A100/H100/Blackwell; FP16 on V100/T4.
- For FP8, use Transformer Engine and enable blockwise scaling if accuracy regresses.

## Verification

1. Train a small ResNet/Transformer with each format and compare final loss and throughput.
2. Check no NaN/Inf in gradients when using FP16 with loss scaling.
3. Profile memory: lower precision should reduce activation and weight footprint.

## References

- https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html
- https://pytorch.org/blog/what-every-user-should-know-about-mixed-precision-training-in-pytorch/
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/
- https://huggingface.co/docs/transformers/mixed_precision_training
