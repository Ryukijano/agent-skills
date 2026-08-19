---
name: tensor-core-fragment-layouts-gb10
description: >-
  Understand PTX mma.sync fragment layouts for NVIDIA Tensor Cores on GB10 (SM121). Covers m16n8k16/32/64 shapes, A/B/C/D register mapping, lane-to-element mapping, and how to stage swizzled shared memory for fragment loads.
---

# Tensor Core Fragment Layouts on GB10 DGX Spark

## Overview

PTX `mma.sync` is the lowest-level way to drive Tensor Cores. A single `mma.sync` is executed by a full warp (32 threads). Each thread holds a piece (fragment) of the A, B, C, and D matrices in its registers. The layout is fixed by the PTX ISA and must be reproduced exactly when loading data from shared memory or global memory into fragments.

This matters for you because `nvcuda::wmma` hides the layout and is now a compatibility/fallback interface; for FP8/FP4 block-scaled MMA on SM121, PTX `mma.sync` is the only path.

## Fragment layout for m16n8k16 (FP16/BF16, FP32 accumulator)

The PTX instruction is:
```ptx
mma.sync.aligned.m16n8k16.row.col.f32.f16.f16.f32
  D, A, B, C;
```

- A is 16×K, row-major in registers, K-major inside the fragment.
- B is K×8, column-major in registers, K-major inside the fragment.
- C/D is 16×8 FP32 in registers.

For the C/D accumulator, the standard layout is:
- `lane_id / 4` gives the row group (0..3 for rows 0,2,4,6 then 8,10,12,14).
- `(lane_id % 4) * 2` gives the column pair (0 or 2, then 1 or 3).
- Each lane holds 4 FP32 registers: `d0,d1` for row `r`/col `c,c+1` and `d2,d3` for row `r+8`/col `c,c+1`.

That is:
```cpp
int r = (lane_id / 4) * 2;          // 0,2,4,6 or 8,10,12,14
int c = (lane_id % 4) * 2;          // 0 or 2
// lane holds C[r][c], C[r][c+1], C[r+8][c], C[r+8][c+1]
```

This is a scattered layout. `d0` and `d2` differ by 8 rows, not adjacent rows.

## Fragment layout for m16n8k64 with block-scaled FP4 (NVFP4)

For Blackwell SM121, the FP4 MMA uses the `kind::mxf4nvf4.block_scale` modifier. Example PTX:
```ptx
mma.sync.aligned.m16n8k64.row.col.kind::mxf4nvf4.block_scale.scale_vec::4X
  .f32.e2m1.e2m1.f32.ue4m3
  D, A, B, C, sfa, /*scaleB=*/{}, sfb, /*scaleA=*/{};
```

- A is 16×64 FP4 E2M1, B is 64×8 FP4 E2M1.
- Each FP4 value is 4 bits, packed in pairs in `b32` registers.
- Scale factors are UE4M3 (4-bit exponent, 0 mantissa) packed 4 per `b32` for `scale_vec::4X`.
- C/D FP32 fragment layout is the same `m16n8` base pattern as m16n8k16; only the K dimension and input packing change.

The exact per-lane A/B packing for SM120/SM121 is not fully documented in the public PTX ISA; the safest reference is the upstream CUTLASS `MmaMXF4NVF4Op` implementation or the `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/fp4_gemm.cu` file in this repo.

## Staging fragments from shared memory

Because the fragments are scattered, you usually do not load A/B directly from GMEM. The standard pattern is:
1. Load a tile from GMEM into shared memory with coalesced 128-bit vector loads.
2. Apply a swizzled shared-memory layout so that each warp's `ldmatrix` (or manual PTX `ld.shared`) reads conflict-free.
3. Move from SMEM to registers in the exact PTX fragment order.

```cpp
// Example: swizzle a 128-byte-wide row so column access rotates banks
size_t linear = row * row_stride_bytes + col * sizeof(half);
size_t swizzled = linear ^ ((row & 0x7) << 4);
```

For `ldmatrix` (SM75+), the SMEM layout must already match the `mma.sync` fragment layout that `ldmatrix` targets. This is why CuTe/CUTLASS spend so much effort on layout algebra.

## PTX `mma.sync` vs `nvcuda::wmma` vs CuTe

| Approach | Control | Fragment visible? | FP8/FP4 block scale? | Recommendation |
|----------|---------|-------------------|----------------------|----------------|
| `nvcuda::wmma` | Low | No | No | Prototyping only |
| PTX `mma.sync` | Full | Yes (from PTX ISA) | Yes (with `kind::`) | Production kernels, research |
| CuTe `TiledMMA` | High | Yes (via layout algebra) | Yes (via `MmaAtom`) | Production code, CUTLASS 3.x |
| cuTile Python | High | Hidden by compiler | Yes (`ct.mma`, `ct.mma_scaled`) | Fast Python DSL path |

## Tuning notes

- Use **FP32 accumulators** for FP8/FP4 to avoid overflow. Never accumulate FP8 in FP16.
- For SM121, the matrix core is the same Ampere-style warp-level `mma.sync`; there is **no WGMMA and no tcgen05**.
- Each `mma.sync` is 32 threads. Do not issue it from a subset of the warp.
- The `m16n8k*` family is the workhorse. Larger K values (32, 64, 128, 256) exist for FP8/FP4/INT8 to improve arithmetic intensity.

## Verification

- Write a tiny kernel that sets A/B to known constants and confirm D matches the hand-computed result for each lane's fragment.
- Compare your hand-rolled fragment loader against `nvcuda::wmma::load_matrix_sync` for the same data on FP16; the final D should be bit-exact.

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/`
- `cuda-blackwell-labs/projects/37_cutile_advanced/`
- PTX ISA 9.2/9.3: https://docs.nvidia.com/cuda/parallel-thread-execution/
- CUTLASS CuTe MMA atom docs: https://docs.nvidia.com/cutlass/latest/media/docs/cpp/cute/0t_mma_atom.html
- Blackwell GPU wiki tcgen05/TMEM: https://0xsero.github.io/blackwell-gpu-wiki/blackwell/tcgen05-and-tmem/

