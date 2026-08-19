---
name: blackwell-fp4-fp8-block-scaling-ptx-gb10
description: >-
  Implement FP8 and block-scaled FP4 (NVFP4) Tensor Core MMA with inline PTX on GB10. Covers `kind::f8f6f4`, `kind::mxf4nvf4.block_scale`, scale-factor encoding, FP32 accumulation, and the sm_121f / sm_121a / PTX 9.1 requirements.
---

# FP8 / Block-Scaled FP4 PTX MMA on GB10 DGX Spark

## Overview

Blackwell (SM121) has native FP8 and block-scaled FP4 (NVFP4) Tensor Core support, but it uses a different PTX path than Ada/Hopper. On GB10 the only way to access it is via warp-level `mma.sync` with the correct `kind::` modifiers. There is no `tcgen05`, no WGMMA, and no TMEM.

This skill focuses on the implementation details: the PTX instruction forms, the scale-factor encoding, and the SM121-specific compilation targets.

## FP8 E4M3 / E5M2 MMA

On SM121 you must use the `kind::f8f6f4` modifier. Ada/Hopper style:
```ptx
mma.sync.aligned.m16n8k32.row.col.f32.e4m3.e4m3.f32
```
will be rejected or fall back. The Blackwell form is:
```ptx
mma.sync.aligned.kind::f8f6f4.m16n8k32.row.col.f32.e4m3.e4m3.f32
  {%0,%1,%2,%3}, {%4,%5,%6,%7}, {%8,%9}, {%0,%1,%2,%3};
```

Supported shapes include m16n8k32, m16n8k64, m16n8k128, m16n8k256 for FP8. Always use **FP32 accumulators**; FP16 accumulators overflow silently.

## Block-scaled FP4 (NVFP4) MMA

NVFP4 represents values as E2M1 (1 sign, 2 exponent, 1 mantissa) plus a per-block scale. The scale itself is a narrow FP8 E4M3 or UE4M3 value. The PTX instruction for SM121 looks like:
```ptx
mma.sync.aligned.m16n8k64.row.col.kind::mxf4nvf4.block_scale.scale_vec::4X
  .f32.e2m1.e2m1.f32.ue4m3
  D, A, B, C, sfa, /*scaleB=*/{}, sfb, /*scaleA=*/{};
```

- `A` and `B` are E2M1 FP4 values packed in `b32` registers.
- `C`/`D` are FP32.
- `sfa`, `sfb` are `b32` registers holding UE4M3 scale factors.
- `scale_vec::4X` means one scale per 16 consecutive values along the K dimension.

The scale layout is the trickiest part: the scale registers must be populated in the exact lane pattern the PTX ISA expects. For a minimal correctness test you can use an identity scale (`0x38383838` for UE4M3 `1.0` packed four per byte).

## Hierarchical scaling

A real quantizer computes:
```
scale_global  = global_amax / (fp8_max * fp4_max)   // fp8_max = 448, fp4_max = 6
scale_block   = (block_amax / fp4_max) / scale_global
x_fp4         = (x / scale_global / scale_block).to(E2M1)
```

At runtime the hardware dequantizes each FP4 element using the per-block scale before the MMA. You must compute `scale_block` as FP8 E4M3 (or UE4M3) and load the scale-fragment registers in the right order.

## SM121 targeting: sm_121 vs sm_121a vs sm_121f

| Target | Meaning | FP8/FP4 block scale? |
|--------|---------|----------------------|
| `sm_121` | Baseline | No block-scaled MMA |
| `sm_121f` | Family mode, enables FP8/FP4 | Yes for dense MMA |
| `sm_121a` | Arch-specific, enables sparse MMA | Required for `mma.sp` with FP4 |

For most dense FP8/FP4 GEMM, `sm_121f` (or equivalently `compute_121f`) is enough. Plain `sm_121` will give `INVALID_PTX` at module load for `kind::mxf4nvf4` instructions.

Also note: the PTX `.version` must be **9.1 or higher** for `kind::mxf4nvf4.block_scale`. CUDA 13.0 ships PTX 9.0 and driver 580.x; those will assemble the code but fail to load with `CUDA_ERROR_UNSUPPORTED_PTX_VERSION`. You need CUDA 13.1+ and driver 590+ to run these kernels.

## Code: identity-scale FP4 test

From `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/fp4_gemm.cu`:
```cpp
uint32_t scale = 0x38383838;  // 1.0 in UE4M3, packed 4 per b32
asm volatile(
    "mma.sync.aligned.m16n8k64.row.col.kind::mxf4nvf4.block_scale.scale_vec::4X "
    ".f32.e2m1.e2m1.f32.ue4m3 "
    "{%0,%1,%2,%3}, {%4,%5,%6,%7}, {%8,%9}, "
    "{%0,%1,%2,%3}, {%10}, {0, 0}, {%11}, {0, 0};"
    : "+f"(C[0]), "+f"(C[1]), "+f"(C[2]), "+f"(C[3])
    : "r"(A[0]), "r"(A[1]), "r"(A[2]), "r"(A[3]),
      "r"(B[0]), "r"(B[1]),
      "r"(scale), "r"(scale));
```

## Tuning notes

- `m16n8k64` is a natural FP4 shape because 64 K-values fit in 32 bytes per A/B tile, matching the fragment packing.
- FP8 `m16n8k32` uses one `b32` A-fragment per lane (4 bytes × 8 values = 32 bits).
- For both, use **row-major A and column-major B** (the PTX `row.col` form).
- Run bit-exact verification against an FP32 CPU reference. With identity scales the answer should be exact (max relative error 0).

## Verification

1. Build with `-arch=sm_121f` or `-arch=sm_121a`.
2. Use identity scales and A/B filled with known constants (e.g. all 1.0).
3. Compare each lane's C fragment against the hand-computed `sum(A*B)+C0`.
4. Once identity works, add real block scaling and check max relative error (<1-3%).

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/`
- `cuda-blackwell-labs/projects/27_triton_fp8_fp4_gemm/`
- PTX ISA 9.1/9.2: https://docs.nvidia.com/cuda/parallel-thread-execution/
- Modular issue on SM121 NVFP4: https://github.com/modular/modular/issues/6597
- cuDNN block scaling: https://docs.nvidia.com/deeplearning/cudnn/latest/operations/BlockScaling.html
- Transformer Engine NVFP4: https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/nvfp4/nvfp4.html

