# FP4/NVFP4/MXFP4 Quantization on Blackwell

## Description

Block-scaled 4-bit formats for training and inference on datacenter Blackwell.

## When to use

You want to reduce memory and increase throughput using 4-bit formats on B200/GB200.

## Key concepts

- **NVFP4**: NVIDIA FP4 with hierarchical scaling. 16-element blocks with E4M3 scales + per-tensor FP32 scale.
- **MXFP4/MXFP8**: microscaling formats with 32-element blocks (MXFP8) or 16-element (MXFP4).
- **Block-scaled GEMM**: D = alpha * (SFA * A) * (SFB * B).
- **tcgen05.mma**: datacenter Blackwell path for FP4 GEMM.

## Code pattern

```python
# TransformerEngine FP8/NVFP4 linear
import transformer_engine.pytorch as te
linear = te.Linear(4096, 4096, params_dtype=torch.fp8)
```

For native PTX on sm_100, use `tcgen05.mma.kind::mxf4.block_scale`.

## Tuning notes

- NVFP4 can achieve 3.5× memory reduction vs FP16 with <1% accuracy loss.
- On consumer Blackwell (sm_120/121), native FP4 may be limited; use Marlin/MXFP4 fallback.
- Keep first and last layers in higher precision.

## Verification

1. Quantize a Llama-3-8B layer to NVFP4 and compare ppl to BF16.
2. Run a grouped GEMM with FP4 weights and FP32 accumulators.
3. Profile memory: KV cache should shrink 50% with FP4.

## References

- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/nvfp4/nvfp4.html
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/mxfp8/mxfp8.html
- https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/
- https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_swiglu_fusion.py
