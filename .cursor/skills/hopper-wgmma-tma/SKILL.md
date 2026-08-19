# WGMMA and TMA on Hopper H100/H200

## Description

Low-level Hopper programming with `wgmma.mma_async`, `cp.async.bulk.tensor`, tensor maps, and mbarriers.

## When to use

You are writing or optimizing kernels for H100/H200 (sm_90) and need the highest possible GEMM or attention throughput.

## Key concepts

- **WGMMA**: warpgroup-level (4 warps) asynchronous MMA. PTX is `wgmma.mma_async`. Different from `mma.sync` because one thread issues for the whole warpgroup.
- **TMA**: `cp.async.bulk.tensor` moves a tile from GMEM→SMEM using a pre-encoded `CUtensorMap`. The issuing thread does not participate in the load; hardware pulls the data.
- **mbarrier**: `mbarrier.arrive` / `mbarrier.wait` coordinate TMA arrivals and consumer starts.
- **Thread block clusters**: up to 8 CTAs on Hopper, enabling TMA multicast (same tile into multiple SMs) and distributed shared memory.

## Code pattern

```cpp
// Host: build tensor map for A (must be 128-byte aligned for f16/bf16)
CUtensorMap tmap_a;
cuTensorMapEncodeTiled(&tmap_a, CUtensorMapDataType::CU_TENSOR_MAP_DATA_TYPE_FLOAT16,
                       2, A, globalDim, globalStrides, boxDim, elementStrides,
                       CU_TENSOR_MAP_INTERLEAVE_NONE,
                       CU_TENSOR_MAP_SWIZZLE_128B,
                       CU_TENSOR_MAP_L2_PROMOTION_L2_256B,
                       CU_TENSOR_MAP_FLOAT_OOB_FILL_NONE);

// Device: one thread issues TMA load
cp.async.bulk.tensor.2d.shared::cta.global.mbarrier::complete_tx::bytes
    [sA], [tmap_a, {bx, by}], [mbar_ptr];
```

## Tuning notes

- WGMMA M is fixed at 64; N must be multiple of 8; K is 16 for f16/bf16, 32 for fp8/int8.
- FP8/int8 operands are K-major only for WGMMA.
- Match TMA swizzle to SMEM swizzle (e.g., `Layout.TMA_128B` for row width ≥128 bytes).
- SMEM per block is 228 KB on H100; use deep pipelining (4-6 stages) to hide latency.

## Verification

1. Compile for `sm_90a` with `-arch=sm_90a -gencode arch=compute_90a,code=sm_90a`.
2. Run a known-answer `wgmma.mma_async` FP16 64×64×16 tile and compare to cuBLAS.
3. Check Nsight Compute `Memory > Tensor Memory` and `Compute (Tensor Core)` sections.

## References

- https://docs.nvidia.com/cuda/hopper-tuning-guide/
- https://pyptx.dev/guides/handwritten-gemm/
- https://pytorch.org/blog/hopper-tma-unit/
- https://github.com/NVIDIA/cutlass/blob/main/examples/python/CuTeDSL/hopper/dense_gemm.py
