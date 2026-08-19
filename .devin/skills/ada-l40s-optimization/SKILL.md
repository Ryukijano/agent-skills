# L40S (Ada) Training and Inference Optimization

## Description

L40S-specific tuning: FP8, TensorRT-LLM/Triton, multi-GPU PCIe scaling, and media engines.

## When to use

You have L40S (sm_89) hardware and need to decide whether to use it for training, inference, or video/vision workloads, and how to tune it.

## Key concepts

- **Ada Lovelace (sm_89)**: 4th-gen Tensor Cores, FP8 support, 48 GB GDDR6, 864 GB/s bandwidth, 142 RT cores.
- **No WGMMA, TMA, or thread block clusters** unlike Hopper. Use `mma.sync` or cuBLAS/cuDNN paths.
- **FP8** is supported from PTX 8.1 / CUDA 12.4+.
- **Multi-GPU is PCIe-only**; NCCL must use P2P/PCIe and may need IOMMU passthrough (`iommu=pt`).
- **Media engines**: 3× NVENC + 3× NVDEC with AV1 support; useful for video inference/transcoding.

## Code pattern

```python
import torch
# L40S supports FP8 E4M3/E5M2 and bfloat16
x = torch.randn(1024, 1024, device='cuda', dtype=torch.bfloat16)
```

For inference, use TensorRT-LLM with `--dtype bfloat16` or `--dtype fp8`.

## Tuning notes

- For 7B-13B model inference and fine-tuning, 48 GB is usually enough.
- Use TensorRT-LLM with paged attention for throughput.
- For multi-GPU L40S, set `NCCL_P2P_DISABLE=0` and verify `nvidia-smi topo -p2p`.
- If NCCL hangs, enable IOMMU passthrough: `iommu=pt` in kernel command line.

## Verification

1. Run `nvidia-smi` and confirm product name is `L40S` (compute capability 8.9).
2. Run a small FP8 GEMM via `torch._scaled_mm` and compare to BF16.
3. Run a TensorRT-LLM Llama-3-8B benchmark at batch size 1 and 8.

## References

- https://www.nvidia.com/en-us/data-center/l40s/
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/
- https://forums.developer.nvidia.com/t/nccl-hangs-on-l40s-gpus-pcie-resolved-via-iommu-passthrough/368169
- https://developer.nvidia.com/optical-flow-sdk
