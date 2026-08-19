# Ampere A100 for Scientific ML and HPC

## Description

A100 architecture, TF32, structured sparsity, MIG, FP64, and cuBLAS/cuDNN paths for scientific workloads.

## When to use

You are running scientific ML or HPC on A100 (sm_80) or A6000/RTX 30-series (sm_86) and want to use TF32, sparsity, or MIG.

## Key concepts

- **A100 (sm_80)**: 3rd-gen Tensor Cores, HBM2e, MIG, 9.7 TFLOPS FP64.
- **TF32**: FP32 dynamic range with 10-bit mantissa. Enable in PyTorch with `torch.backends.cuda.matmul.allow_tf32 = True` and `torch.backends.cudnn.allow_tf32 = True`.
- **Structured sparsity**: 2:4 pattern in cuSPARSELt for 2× throughput.
- **MIG**: partition A100 into up to 7 isolated GPU instances.
- **sm_86 (A6000/RTX 3090)**: 100 KB SMEM, 48 warps/SM, no MIG, lower FP64.

## Code pattern

```python
import torch
# Enable TF32
 torch.backends.cuda.matmul.allow_tf32 = True
 torch.backends.cudnn.allow_tf32 = True

x = torch.randn(4096, 4096, device='cuda')
# cuBLAS will use TF32 Tensor Cores automatically
```

## Tuning notes

- TF32 is not appropriate for numerically sensitive scientific computing; disable with `torch.backends.cuda.matmul.allow_tf32 = False`.
- For MIG, choose profile based on workload (e.g., 20G MIG for GROMACS MD).
- NHWC layout is preferred for Tensor Core convolutions on Ampere.

## Verification

1. Run `nvidia-smi` and confirm GPU product name and compute capability.
2. Benchmark FP32 GEMM with and without TF32 and compare throughput.
3. If using MIG, verify the correct MIG instance is visible inside the container.

## References

- https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/nvidia-ampere-architecture-whitepaper.pdf
- https://developer.nvidia.com/blog/accelerating-ai-training-with-tf32-tensor-cores/
- https://docs.nvidia.com/cuda/cusparselt/
- https://docs.nvidia.com/datacenter/tesla/pdf/MIG_User_Guide.pdf
