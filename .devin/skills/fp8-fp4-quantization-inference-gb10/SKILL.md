---
name: fp8-fp4-quantization-inference-gb10
description: >-
  Quantize models and activations to FP8/FP4 for fast Blackwell inference on GB10. Covers NVIDIA TensorRT Model Optimizer, cuBLASLt narrow-precision GEMM, and NVFP4 KV cache.
---

# FP8 / FP4 Quantization for Inference on GB10 DGX Spark

## Overview

Blackwell has native FP8 and block-scaled FP4 Tensor Core support. Reducing from BF16/FP16 to FP8 halves memory and roughly doubles throughput; FP4 can halve it again for weights and KV cache.

## Paths

1. **TensorRT Model Optimizer / TensorRT-LLM**
   - PTQ to NVFP4 or FP8 with calibration.
   - `nvidia-modelopt` + `trtllm-build` for Llama/Mistral/DeepSeek.

2. **cuBLASLt FP8 GEMM**
   - `CUBLAS_COMPUTE_32F`, A/B `CUDA_R_8F_E4M3`, C `CUDA_R_32F` or `CUDA_R_16F`.
   - TN format: A must be transposed, B non-transposed.
   - Requires per-tensor scale pointers for A, B, and output.

3. **Block-scaled FP4 in PTX**
   - Use `__nv_fp8_e4m3` / `__nv_fp8_e5m2` and `__nv_fp4x2`.
   - At CUDA C++ level `__nv_fp4_e2m1` is available in `cuda_fp4.h`.

## NVFP4 KV cache

- 4-bit storage, dequantized to FP8 before attention.
- Supported by TensorRT-LLM and Dynamo for long-context and large-batch inference.

## Verification

Quantize a small layer, run FP8/FP4 vs FP32 reference, check max relative error (<1-3%).

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/` and `projects/27_triton_fp8_fp4_gemm/`
- https://developer.nvidia.com/blog/optimizing-inference-for-long-context-and-large-batch-sizes-with-nvfp4-kv-cache/
- https://docs.nvidia.com/deeplearning/tensorrt-model-optimizer/

