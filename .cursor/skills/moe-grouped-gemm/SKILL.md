# MoE and Grouped GEMM on GPU

## Description

Grouped GEMM, MoE routing, cuBLAS/cuDNN/TransformerEngine/FlashInfer/vLLM backends.

## When to use

You are implementing Mixture-of-Experts (MoE) layers or grouped GEMM for variable-size matrices.

## Key concepts

- **Grouped GEMM**: one kernel launch with multiple matrix shapes and per-matrix scaling.
- **MoE routing**: top-k gating, expert capacity, load balancing.
- **Backends**: cuBLASLt, CUTLASS, TransformerEngine, FlashInfer, vLLM `marlin`, TensorRT-LLM.
- **Blackwell**: TMA-based grouped GEMM with block-scaled FP4/FP8.

## Code pattern

```python
import torch
import triton

# vLLM MoE backend selection
# --moe-backend=marlin  # on GB10/sm_121
# --moe-backend=cutlass # on H100/B200
```

For cuBLAS grouped GEMM, see `cublasGemmGroupedBatchedEx`.

## Tuning notes

- On GB10, Marlin is currently the most reliable MoE backend.
- On B200, use FP4 grouped GEMM with TMA multicast.
- Load balancing losses prevent expert collapse.

## Verification

1. Run a small MoE layer and compare grouped GEMM to a loop of individual GEMMs.
2. Verify routing produces balanced expert assignment.
3. On B200, profile with Nsight Compute and check `tcgen05.mma` utilization.

## References

- https://developer.nvidia.com/blog/introducing-grouped-gemm-apis-in-cublas-and-more-performance-updates/
- https://docs.nvidia.com/deeplearning/cudnn/latest/fe-oss-apis/gemm_fusions/grouped_gemm_quant_unified.html
- https://github.com/flashinfer-ai/flashinfer/pull/2725
- https://github.com/vllm-project/vllm/pull/43814
