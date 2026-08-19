---
name: shared-memory-swizzling-gb10
description: >-
  Eliminate shared memory bank conflicts on GB10 with padding and XOR-based swizzling. Covers 32-bank layout, 128-byte swizzle patterns, CuTe `Swizzle<>`, and the SMEM occupancy tradeoff on SM121 (99 KB max per block).
---

# Shared Memory Swizzling on GB10 DGX Spark

## Overview

Shared memory is the fastest programmer-managed on-chip memory. It is split into 32 banks, each 4 bytes wide. A warp can issue one 128-byte transaction per cycle if all 32 threads access different banks; otherwise the accesses serialize.

For Tensor Core GEMM, the classic pattern is to stage a tile in shared memory and then load it into per-thread `mma.sync` fragments. If the tile is stored naively in row-major order, a column access by a warp becomes a 32-way bank conflict.

## Why row-major 32×32 tiles conflict

Consider a row-major `float tile[32][32]`:
- Element `tile[r][c]` is at byte `4 * (r * 32 + c)`.
- Thread `i` reading `tile[r][i]` maps to bank `(r * 32 + i) % 32 = i`. No conflict for a row.
- But thread `i` reading `tile[i][c]` maps to bank `(i * 32 + c) % 32 = c`. All 32 threads hit bank `c`. 32-way conflict.

GEMM needs both row-wise and column-wise access (A is row-major, B is effectively column-major), so you need a layout that is conflict-free for both.

## Fix 1: Padding

Add a padding column:
```cpp
__shared__ float tile[32][33];  // 32 rows, 33 columns
```
Now `tile[r][c]` is at `4 * (r * 33 + c)`, so a column access maps to bank `(r * 33 + c) % 32 = (r + c) % 32`, which rotates across banks. Simple and effective.

**Tradeoff:** Extra shared memory can reduce occupancy. On SM121 the max shared mem per block is only 99 KB, and the default carve-out is 48 KB, so padding can push you over a threshold.

## Fix 2: XOR swizzling

Swizzling permutes the address without allocating extra columns. The 128-byte swizzle pattern used for TMA/Hopper is also useful for manual `ldmatrix`:
```cpp
// XOR lower column bits with row index bits
size_t linear = r * (TILE_DIM * sizeof(T)) + c * sizeof(T);
size_t swizzled = linear ^ ((r & 0x7) << 4);  // bits [4:6] XOR row
```

For a 2D `float` tile where each row is 128 bytes (32 columns), this means:
- Row 0 keeps banks 0..31.
- Row 1 rotates by 1: banks 1..30,0.
- Row 2 rotates by 2: banks 2..31,1,0.
- Column access now touches a different bank per row.

In CuTe the same pattern is:
```cpp
auto tileLayout = make_layout(make_shape(Int<32>{}, Int<32>{}), GenRowMajor{});
auto swizzledLayout = composition(Swizzle<5,0,5>{}, tileLayout);
```

## SM121 specifics

- 128 KB shared memory per SM, max **99 KB per block** with opt-in (`cudaFuncSetAttribute(... cudaFuncAttributeMaxDynamicSharedMemorySize, 101376)`).
- Default static shared memory carve-out is 48 KB per block.
- If a block uses >48 KB, only one block fits per SM unless you explicitly request the larger pool.
- Occupancy drops fast. On SM121 max warps/SM is 48 (vs 64 on SM100).

Therefore swizzling is usually better than padding on GB10: it saves the scarce shared memory budget.

## Compute-to-SMEM mapping

To check whether a pattern is conflict-free:
```cpp
// bank of a 4-byte access
int bank = (addr_in_smem_bytes / 4) % 32;
```

For an access pattern, collect the bank of every lane in the same warp instruction. If two lanes touch different addresses in the same bank, that is a conflict. If they all touch the **same** address, it is a broadcast (no conflict).

## Tuning notes

- Prefer swizzling over padding when SMEM is the occupancy limiter.
- Use `__ldsm` or `ld.shared` with 128-bit transactions (`LDG.E.128`, `LDS.128`) where possible; this is the natural width for Tensor Core fragment loads.
- For FP16/BF16 tiles, the swizzle granularity is 16 bytes (eight FP16 values). For FP8/FP4, the granularity is also 16 bytes (16 bytes = 16 FP8 = 32 FP4).
- Always verify with Nsight Compute: look for `l1tex__data_bank_conflicts_pipe_lsu_mem_shared`.

## Verification

Write a microbenchmark that does 1000 iterations of the suspect SMEM access pattern and compare:
1. Naive row-major.
2. Padded.
3. Swizzled.

Use Nsight Compute to confirm the bank-conflict counter is near zero for the swizzled version. Bandwidth should increase 2-4x for a conflict-heavy access.

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/` (swizzled SMEM staging)
- `cuda-blackwell-labs/projects/37_cutile_advanced/`
- KernelWiki swizzling: https://github.com/mit-han-lab/KernelWiki/blob/master/wiki/techniques/swizzling.md
- Lei Mao SMEM swizzling blog: https://leimao.github.io/blog/CUDA-Shared-Memory-Swizzling/
- NVIDIA Blackwell Tuning Guide: https://docs.nvidia.com/cuda/blackwell-tuning-guide/

