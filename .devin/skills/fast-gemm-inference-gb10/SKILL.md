# Fast GEMM for Inference on GB10 DGX Spark

## Overview

For LLM inference, GEMM is the dominant op in prefill; in decode, it becomes small and latency-sensitive. The right precision, layout, and epilogue fusion are critical.

## cuBLASLt checklist

```cpp
cublasLtMatmulDesc_t op;
cublasLtMatmulDescCreate(&op, CUBLAS_COMPUTE_32F, CUDA_R_32F);
cublasLtMatmulDescSetAttribute(op, CUBLASLT_MATMUL_DESC_TRANSA, &transa, sizeof(transa));
cublasLtMatmulDescSetAttribute(op, CUBLASLT_MATMUL_DESC_TRANSB, &transb, sizeof(transb));

// Epilogue fusion: bias + ReLU / GELU / bias only
cublasLtEpilogue_t epilogue = CUBLASLT_EPILOGUE_RELU;  // or GELU, DEFAULT, BIAS
cublasLtMatmulDescSetAttribute(op, CUBLASLT_MATMUL_DESC_EPILOGUE, &epilogue, sizeof(epilogue));

cublasLtMatmulAlgoGetHeuristic(handle, op, Adesc, Bdesc, Cdesc, Ddesc,
                               &preference, 1, &heuristic, &returned);
```

## Batched GEMM

For batched decode:

```cpp
cublasGemmStridedBatchedEx(handle, transa, transb, m, n, k,
                           alpha, A, Atype, lda, strideA,
                           B, Btype, ldb, strideB, beta,
                           C, Ctype, ldc, strideC,
                           batch_count, computeType, algo);
```

## Precision ladder

| Situation | Try |
|-----------|-----|
| Maximum accuracy | BF16/FP16 with FP32 acc |
| 2x memory/speed | FP8 E4M3/E5M2 |
| 4x weight compression | FP4 block-scaled |
| Tiny matmuls, CPU fallback | FP32 with TF32 |

## Verification

Compare cuBLASLt output to a CPU FP32 reference; use relative tolerance appropriate to the precision.

## Reference

- `cuda-blackwell-labs/projects/30_cublas_cudnn_benchmarks/`
- `cuda-blackwell-labs/projects/37_cutile_advanced/`
- https://docs.nvidia.com/cuda/cublas/

