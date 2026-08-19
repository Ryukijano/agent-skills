#!/usr/bin/env python3
"""Generate 7 advanced CUDA/Tensor Core skills for agent-skills.

Each skill gets the standard 4-file treatment:
  .devin/skills/<name>/SKILL.md     (full reference)
  .devin/workflows/<name>.md        (slash workflow)
  .cursor/skills/<name>/SKILL.md    (full reference, same body)
  .cursor/commands/<name>.md        (slash command)

The .cursor skill body is the SAME as .devin so it is not a hollow stub.

Usage:
    python3 gen_advanced_cuda_skills.py [path-to-agent-skills-repo]
"""

import os
import sys

DEFAULT_BASE = "/home/aimsgroupuol/AIMSgeneral/Gyanateet/mpc_vla_diffusion_study/agent-skills"

SKILLS = [
    {
        "name": "tensor-core-fragment-layouts-gb10",
        "description": (
            "Understand PTX mma.sync fragment layouts for NVIDIA Tensor Cores on GB10 (SM121). "
            "Covers m16n8k16/32/64 shapes, A/B/C/D register mapping, lane-to-element mapping, "
            "and how to stage swizzled shared memory for fragment loads."
        ),
        "devin_body": '''# Tensor Core Fragment Layouts on GB10 DGX Spark

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
''',
    },
    {
        "name": "shared-memory-swizzling-gb10",
        "description": (
            "Eliminate shared memory bank conflicts on GB10 with padding and XOR-based swizzling. "
            "Covers 32-bank layout, 128-byte swizzle patterns, CuTe `Swizzle<>`, and the SMEM "
            "occupancy tradeoff on SM121 (99 KB max per block)."
        ),
        "devin_body": '''# Shared Memory Swizzling on GB10 DGX Spark

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
''',
    },
    {
        "name": "blackwell-fp4-fp8-block-scaling-ptx-gb10",
        "description": (
            "Implement FP8 and block-scaled FP4 (NVFP4) Tensor Core MMA with inline PTX on GB10. "
            "Covers `kind::f8f6f4`, `kind::mxf4nvf4.block_scale`, scale-factor encoding, FP32 "
            "accumulation, and the sm_121f / sm_121a / PTX 9.1 requirements."
        ),
        "devin_body": '''# FP8 / Block-Scaled FP4 PTX MMA on GB10 DGX Spark

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
''',
    },
    {
        "name": "cuda-occupancy-register-pressure-gb10",
        "description": (
            "Tune CUDA kernel occupancy and register pressure on GB10. Covers launch bounds, the "
            "occupancy API, shared-memory vs register tradeoffs, and when high occupancy helps or "
            "hurts performance."
        ),
        "devin_body": '''# CUDA Occupancy and Register Pressure on GB10 DGX Spark

## Overview

Occupancy is the ratio of active warps to the maximum the SM can hold. Higher occupancy gives the warp scheduler more threads to switch to when one warp stalls, hiding latency. But chasing 100% occupancy can backfire: it forces the compiler to use fewer registers per thread, which can spill to local memory and slow things down.

On GB10 (SM121) the limits are:
- 64K 32-bit registers per SM.
- Max 255 registers per thread.
- Max 48 concurrent warps per SM (not 64 like SM100).
- Max 32 thread blocks per SM.
- 128 KB shared memory per SM, max 99 KB per block with opt-in.

## Occupancy limiters

A kernel launch is limited by whichever resource runs out first:
1. **Threads per block** × blocks per SM ≤ 1536 (48 warps × 32 threads).
2. **Registers per thread** determines how many warps fit in the 64K register file.
3. **Shared memory per block** determines how many blocks fit given 128K/SM.

A block with 256 threads and 64 registers/thread uses 256×64 = 16K registers. 64K / 16K = 4 blocks can fit, but only 1536/256 = 6 blocks max by threads, so occupancy is limited by registers to 4 blocks = 1024 threads = 67%.

A block with 1024 threads and 32 registers/thread uses 1024×32 = 32K registers. Only 2 blocks fit, so max active threads = 2048 / 1536 > 1.0? No — max warps per SM is 48 = 1536 threads, so this is also register-limited.

## The occupancy trap

The classic mistake is to assume more occupancy always helps. It does for **memory-bound** kernels, because warps spend most of their time waiting for memory and the scheduler can hide latency with more active warps. For **compute-bound** kernels, especially Tensor Core kernels, extra warps do not help if the compute pipelines are already full. In that case using more registers per thread to keep data in fast registers (no spilling) is better.

Rule of thumb:
- Memory-bound (<10 FLOPs/byte): target 50-100% occupancy.
- Compute-bound (>50 FLOPs/byte): occupancy matters less; avoid register spilling.
- Tensor Core GEMM: often 25-50% occupancy can be near peak if the memory pipeline is well overlapped with `cp.async`.

## Launch bounds

Use `__launch_bounds__` to tell the compiler the target register budget:
```cpp
__launch_bounds__(maxThreadsPerBlock, minBlocksPerMultiprocessor)
__global__ void kernel(...) { ... }
```

For example, `__launch_bounds__(256, 2)` tells the compiler to use at most `64K / (256 * 2) = 128` registers per thread. This can reduce spilling compared to the default, which may allocate more registers and lower occupancy.

## Occupancy API

At runtime you can query the best launch config:
```cpp
int min_grid, best_block;
cudaOccupancyMaxPotentialBlockSize(
    &min_grid, &best_block,
    kernel, 0, 0  // dynamic smem, block size limit
);
```

For a known dynamic shared memory size:
```cpp
cudaOccupancyMaxActiveBlocksPerMultiprocessor(
    &num_blocks, kernel, block_size, dynamic_smem);
```

## Nsight Compute Python occupancy module

Nsight Compute ships `ncu_occupancy`:
```python
from ncu_occupancy import OccupancyCalculator, OccupancyParameters
calc = OccupancyCalculator(major=12, minor=1)
params = OccupancyParameters(
    threads_per_block=256,
    registers_per_thread=64,
    shared_memory_per_block=24*1024,
    blocks_per_sm=None
)
limiters = calc.get_occupancy_limiters(params)
print(calc.get_sm_occupancy(params))
```

## SMEM vs occupancy tradeoff on SM121

SM121 has only 128 KB shared memory per SM and a 99 KB per-block opt-in cap. If a block uses 50 KB SMEM, at most 2 blocks fit per SM, and with 48KB default only 1. This can drop occupancy to ~16% even if registers allow more.

Strategies:
- Reduce tile size or use swizzling instead of padding to save SMEM.
- Use dynamic shared memory only when needed.
- For compute-bound kernels, lower occupancy with larger tiles can still win.

## Tuning notes

- Profile with `ncu --set full` and look at the occupancy section.
- Watch for `local` memory traffic; that is a sign of register spilling.
- The compiler often uses fewer registers than the PTX reports; `nvdisasm` gives the real SASS register count.
- Don't blindly set `__launch_bounds__(1024, 1)` to force 100% occupancy; it may spill everything.

## Verification

1. Implement a simple GEMM kernel.
2. Vary `__launch_bounds__` and block size.
3. Measure wall-clock time and check Nsight Compute `sm__warps_active.avg.pct_of_peak_sustained_active` plus `l1tex__data_bank_conflicts`.
4. Find the point where reducing occupancy no longer hurts but spilling starts to hurt.

## Reference

- `cuda-blackwell-labs/projects/04_occupancy_stalls/`
- NVIDIA Blackwell Tuning Guide: https://docs.nvidia.com/cuda/blackwell-tuning-guide/
- CUDA Occupancy API: https://docs.nvidia.com/cuda/cuda-driver-api/group__CUDA__OCCUPANCY.html
- Nsight Compute occupancy Python interface: https://docs.nvidia.com/nsight-compute/OccupancyCalculatorPythonInterface/
- "The CUDA Metric That Gaslights You": https://blog.melashri.net/posts/cuda-occupancy/
''',
    },
    {
        "name": "cp-async-pipeline-gb10",
        "description": (
            "Build multi-stage async copy pipelines with `cp.async` on GB10. Covers commit/wait "
            "groups, mbarriers, double/triple buffering, and why SM121 uses `cp.async` instead of "
            "TMA for GMEM->SMEM staging."
        ),
        "devin_body": '''# `cp.async` Pipelines on GB10 DGX Spark

## Overview

`cp.async` (also called `cp.async.ca.shared.global`) is the PTX instruction family for copying data asynchronously from global memory to shared memory. It is supported on Ampere and later (SM80+). It lets the memory unit handle the copy while the SMs continue computing, provided you insert proper `commit_group` / `wait_group` synchronization.

On GB10 (SM121) there is no usable TMA (`cp.async.bulk.tensor`) in the current toolchains, so `cp.async` is the primary way to stage tiles for Tensor Cores while overlapping loads with `mma.sync`.

## Single async copy

```cpp
asm volatile("cp.async.cg.shared.global [%0], [%1], 16;"
             : : "r"(smem_ptr), "l"(gmem_ptr));
asm volatile("cp.async.commit_group;");
// ... do other work ...
asm volatile("cp.async.wait_group 0;");  // wait for all in-flight groups
```

- `cp.async.cg` copies 16 bytes (coalesced) from GMEM to SMEM.
- `commit_group` marks the start of a new group.
- `wait_group N` waits until at most N groups are still in-flight.

## Multi-stage pipeline (double buffering)

The goal is to keep the memory pipe and the math pipe busy at the same time. With one SMEM buffer you must wait for the load to finish before computing; with two buffers the next load can happen in parallel with the current MMA.

```cpp
__shared__ float A_smem[2][TILE_K][TILE_M];  // ping-pong
__shared__ float B_smem[2][TILE_K][TILE_N];

int stage = 0;
for (int k = 0; k < K; k += TILE_K) {
    // 1. Issue async loads into buffer `stage`
    cp_async_load(A_smem[stage], &A[...]);
    cp_async_load(B_smem[stage], &B[...]);
    cp_async_commit_group();

    // 2. Wait for previous stage's data to be ready
    cp_async_wait_group(1);  // keep 1 group in flight

    // 3. Compute on the OTHER buffer (1 - stage)
    mma.sync(..., A_smem[1 - stage], B_smem[1 - stage], ...);

    stage = 1 - stage;
}
```

For deeper overlap use 3 or 4 stages. Each stage needs its own SMEM slot, so this is a SMEM/occupancy tradeoff.

## Why not TMA on SM121?

TMA (`cp.async.bulk.tensor`) uses a tensor map descriptor and hardware address generation. It is required for Hopper's WGMMA and datacenter Blackwell's `tcgen05`. However, GB10/SM121 does not expose TMA in the current CUDA 13.x/p txas path for consumer Blackwell, and it lacks the TMEM/WGMMA units that consume TMA output.

Therefore on GB10 you are effectively doing an Ampere-style pipeline: `cp.async` GMEM→SMEM, then `ldmatrix` or manual `ld.shared`→registers, then `mma.sync`. This still reaches good throughput (your Project 37 cuTile persistent matmul hits ~45 TFLOPS with this pattern).

## mbarriers

For more complex synchronizations (multiple warps producing/consuming), use `mbarrier`:
```cpp
__shared__ uint64_t mbar;
asm volatile("mbarrier.init.shared::cta.b64 [%0], %1;" : : "r"(&mbar), "r"(expected_arrive_count));

// Arrive
asm volatile("mbarrier.arrive.expectation.shared::cta.b64 _, [%0];" : : "r"(&mbar));

// Wait
asm volatile("mbarrier.try_wait.shared::cta.b64 %0, [%1];" : "=r"(ready) : "r"(&mbar));
```

In CuTe/CUTLASS 3.x these are wrapped by pipeline classes.

## Tuning notes

- Use `cp.async.cg` (16 bytes) to match the 128-bit memory bus width.
- Stage count: 2 is the minimum for overlap; 3-4 can hide more latency at the cost of SMEM.
- On SM121, keep SMEM usage ≤ 48 KB unless you explicitly request the larger pool.
- Combine with `__launch_bounds__` to leave enough registers for the async pipeline state.

## Verification

1. Start with a synchronous version of a tiled GEMM.
2. Convert GMEM→SMEM loads to `cp.async` with `commit/wait`.
3. Add a second SMEM buffer and stage the loads.
4. Profile with Nsight Compute; `dram__throughput.avg.pct_of_peak_sustained_elapsed` should rise and `sm__cycles_active` should stay high.

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/`
- `cuda-blackwell-labs/projects/37_cutile_advanced/`
- CCCL `cp.async.bulk` docs: https://nvidia.github.io/cccl/unstable/libcudacxx/ptx/instructions/cp_async_bulk.html
- "Asynchronous Pipelining with cp.async": https://deepwiki.com/gau-nernst/learn-cuda/6.2-asynchronous-pipelining-with-cp.async
- PTX ISA: https://docs.nvidia.com/cuda/parallel-thread-execution/
''',
    },
    {
        "name": "nsight-compute-tensor-cores-gb10",
        "description": (
            "Profile CUDA kernels on GB10 with Nsight Compute to find Tensor Core utilization, "
            "memory bottlenecks, and occupancy limiters. Covers the key NCU metrics and how to "
            "interpret them for SM121."
        ),
        "devin_body": '''# Profiling Tensor Cores with Nsight Compute on GB10 DGX Spark

## Overview

Nsight Compute (NCU) is the tool to answer the question "is my kernel actually using Tensor Cores and where is it slow?". On GB10 the standard metrics are the same as other Blackwell/SM12x GPUs, but the interpretation changes because the chip is memory-bandwidth-limited (273 GB/s shared LPDDR5X) and lacks TMEM/WGMMA.

## Key NCU metrics for Tensor Cores

### 1. Did Tensor Cores actually run?

- `sm__pipe_tensor_cycles_active.avg.pct_of_peak_sustained_active` — percentage of cycles the Tensor Core pipe was active.
- `smsp__sass_thread_inst_executed_op_mma.sum` — raw count of `mma` instructions executed.
- Instruction mix: under **Details | Instruction Statistics | Executed Instruction Mix**, look for any `MMA` line. If it is zero, your kernel fell back to CUDA cores.

### 2. Tensor Core throughput

- `sm__pipe_tensor_cycles_active.sum` / `sm__cycles_active.sum` gives active percentage.
- Compare against the theoretical peak for your precision. GB10 is advertised around 1 PFLOP/s at FP4 dense. In practice your ceiling is lower for real kernels due to memory.

### 3. Memory vs compute bound

The **GPU Speed of Light Throughput** section gives:
- `Compute (SM) Throughput %`
- `Memory Throughput %`
- `DRAM Throughput %`

If `Memory Throughput` is close to 100% and `Compute` is low, the kernel is memory-bound. If `Compute` is high and `Memory` is low, it is compute-bound.

For GB10:
- `dram__bytes_read|write.sum.per_second` is the actual bytes/s to LPDDR5X.
- `gpu__compute_memory_request_throughput.avg.pct_of_peak_sustained_elapsed` is the aggregate memory request throughput as % of peak.

### 4. Occupancy and register pressure

- `sm__warps_active.avg.pct_of_peak_sustained_active` — active warps vs max.
- `smsp__sass_thread_inst_executed` per `sm__cycles_active` gives IPC.
- `l1tex__data_bank_conflicts_pipe_lsu_mem_shared` — shared memory bank conflicts.
- Look at the **Occupancy** section for the limiting resource (registers, shared memory, block size).

### 5. Pipe throttles

If you see high `math pipe throttles`, your MMA instruction queue is full and warps are stalling because they cannot issue more Tensor Core instructions. This can happen when `ldmatrix` cannot feed the MMAs fast enough. Solutions:
- More async pipeline stages.
- Larger K-tiles to increase arithmetic intensity.
- Better SMEM swizzling to reduce bank conflicts.

## Launching NCU on GB10

```bash
# Full report
ncu --set full ./my_kernel

# Focused on memory and compute
ncu --section "MemoryWorkloadAnalysis" --section "ComputeWorkloadAnalysis" --section "SpeedOfLight" ./my_kernel

# Specific metrics for a custom kernel
ncu --metrics sm__pipe_tensor_cycles_active.avg.pct_of_peak_sustained_active,\
              dram__bytes_read.sum.per_second,\
              l1tex__data_bank_conflicts_pipe_lsu_mem_shared.sum \
              ./my_kernel
```

Note: on GB10, Nsight Systems may not trace Unified Memory migrations with current drivers. Use NCU for kernel-level analysis and `cat /proc/meminfo` for system-level memory.

## What good looks like on GB10

For a FP16 Tensor Core GEMM at 1024³:
- `Compute (SM) Throughput`: 60-90% depending on tile size.
- `DRAM Throughput`: 40-80% (if the working set fits L2, it can be 0%).
- `Tensor Pipe Active`: >50% is solid; >80% is excellent.
- Bank conflicts: near 0.

For a memory-bound kernel (e.g. streaming copy):
- `DRAM Throughput`: ~85% of peak (~230 GB/s).
- `Compute Throughput`: <10%.

## Roofline model for GB10

Peak FP16 Tensor Core: ~90+ TFLOP/s. Peak DRAM: ~273 GB/s. The ridge point is roughly:
```
ridge_FLOPs_per_byte = 90e12 / 273e9 ≈ 330 FLOPs/byte
```

A kernel with less arithmetic intensity than that is memory-bound. Most decode attention and elementwise ops on GB10 are far below this, which is why memory bandwidth dominates.

## Tuning notes

- Run `ncu --set full` to get a baseline.
- Check `Instruction Mix` for `MMA`; if missing, you are not using Tensor Cores.
- Look at `Speed Of Light` to identify memory vs compute bound.
- If memory-bound: improve coalescing, use `cp.async`, swizzle SMEM, quantize weights to FP8/FP4.
- If compute-bound: increase tile size, reduce bank conflicts, add pipeline stages, check for pipe throttles.
- Iterate and remeasure.

## Verification

1. Profile a known FP16 Tensor Core GEMM and confirm `sm__pipe_tensor_cycles_active.avg.pct_of_peak_sustained_active` > 50%.
2. Compare `Compute (SM) Throughput %` vs `DRAM Throughput %` to label the kernel memory- or compute-bound.
3. Confirm the `MMA` instruction mix is non-zero in Nsight Compute Details.
4. Check `l1tex__data_bank_conflicts_pipe_lsu_mem_shared` is near zero for the suspect SMEM access pattern.

## Reference

- `cuda-blackwell-labs/projects/30_cublas_cudnn_benchmarks/`
- Nsight Compute Profiling Guide: https://docs.nvidia.com/nsight-compute/ProfilingGuide/
- Blackwell Nsight Compute: https://developer.nvidia.com/tools-overview/nsight-compute/get-started-2026_1
- "Understanding Tensor Pipe Throughput and Throttle Stalls": https://forums.developer.nvidia.com/t/understanding-tensor-pipe-throughput-and-throttle-stalls/355572
''',
    },
    {
        "name": "blackwell-sm121-targeting-gb10",
        "description": (
            "Correctly target the GB10 (SM121) architecture: sm_121 vs sm_121f vs sm_121a, PTX "
            "version requirements, Triton ptxas setup, and common compile/runtime errors on DGX Spark."
        ),
        "devin_body": '''# Targeting Blackwell SM121 / GB10 DGX Spark

## Overview

NVIDIA "Blackwell" is not one architecture. Datacenter Blackwell (B100/B200) is SM10x with `tcgen05`, TMEM, and NVSwitch. Consumer and workstation Blackwell (RTX 50 series, RTX PRO 6000, DGX Spark GB10) is SM12x. **SM121 does not have tcgen05, TMEM, WGMMA, or DSMEM.**

This skill is about compiling and launching kernels so they actually run on GB10 instead of failing with `INVALID_PTX`, `no kernel image`, or silent wrong results.

## sm_121, sm_121f, sm_121a

| Target | Meaning | Use case |
|--------|---------|----------|
| `sm_121` | Baseline SM121 | Normal FP32/FP16/BF16 kernels without Tensor Core FP8/FP4 block scaling |
| `sm_121f` | Family mode | Enables `kind::f8f6f4` and `kind::mxf4nvf4` dense block-scaled MMA |
| `sm_121a` | Arch-specific | Required for `mma.sp` sparse block-scaled FP4/FP8 |

Use `sm_121a` if you are unsure; it is a superset of `sm_121f`. For nvcc:
```bash
nvcc -arch=sm_121a -O2 -lineinfo -std=c++17 kernel.cu -o kernel
```

For Triton you need the system ptxas and the correct arch list:
```bash
export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas
export TORCH_CUDA_ARCH_LIST="12.1+PTX"
unset TRITON_OVERRIDE_ARCH   # do NOT set sm_90
```

## PTX version requirement

- CUDA 13.0 ships PTX 9.0.
- `kind::mxf4nvf4.block_scale` (block-scaled FP4) requires **PTX 9.1+**.
- Driver 580.x (CUDA 13.0) will fail to JIT PTX 9.1 with `CUDA_ERROR_UNSUPPORTED_PTX_VERSION`.
- Driver 590+ (CUDA 13.1+) is required for FP4 block-scaled MMA.

So if you compile `-arch=sm_121a` but your driver is 580.x, the kernel may ptxas-assemble but fail at module load.

## Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ptxas error: Feature '...' not supported on .target 'sm_121'` | Using base `sm_121` for FP4/FP8 block scale | Use `sm_121f` or `sm_121a` |
| `CUDA_ERROR_INVALID_PTX` at load | Same as above, or PTX 9.1 on driver 580.x | Use correct arch or upgrade driver |
| `ptxas fatal: Value 'sm_121a' is not defined` | Triton/PyTorch using old bundled ptxas | `TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas` |
| `no kernel image is available for execution on the device` | Triton compiled for sm_90 or missing sm_121 | Set `TORCH_CUDA_ARCH_LIST=12.1+PTX` and use system ptxas |
| `tcgen05.mma` not supported on sm_121a | Using datacenter Blackwell PTX | Use warp-level `mma.sync` instead |

## What works and what does not on SM121

| Feature | SM121 (GB10) | SM100 (B200) |
|---------|--------------|--------------|
| Tensor Cores | ✅ Ampere-style `mma.sync` | ✅ `tcgen05` / WGMMA |
| FP8/FP4 block scale | ✅ with `kind::` modifier | ✅ native / TMEM |
| TMEM | ❌ No | ✅ Yes |
| WGMMA | ❌ No | ✅ Yes |
| DSMEM / clusters | ❌ No | ✅ Yes |
| TMA (`cp.async.bulk.tensor`) | ⚠️ Not reliably exposed | ✅ Yes |
| Shared mem / block | 99 KB max | 227 KB max |
| Shared mem / SM | 128 KB | 228 KB |
| Max warps / SM | 48 | 64 |

## Tuning notes

- Default to `sm_121a` for any kernel using FP8/FP4 block-scaled MMA; `sm_121f` is sufficient for dense FP8/FP4 and `sm_121` only for plain FP32/FP16/BF16.
- Set `TRITON_PTXAS_PATH` to the system `ptxas` from CUDA 13.0+ and avoid `TRITON_OVERRIDE_ARCH=sm90`.
- Pin `TORCH_CUDA_ARCH_LIST=12.1+PTX` for PyTorch builds on DGX Spark.
- Check `cat /proc/driver/nvidia/version` before using `kind::mxf4nvf4.block_scale`: it needs driver 590+/PTX 9.1.
- Test a plain FP16 `mma.sync` first to confirm basic targeting works before adding FP8/FP4 modifiers.

## Triton / PyTorch on GB10

PyTorch stable wheels for Blackwell are a moving target. For DGX Spark you generally need:
- PyTorch compiled with `sm_121` support.
- System `ptxas` from CUDA 13.0+.
- `TORCH_CUDA_ARCH_LIST=12.1+PTX`.

Do not set `TRITON_OVERRIDE_ARCH=sm90`; it causes Triton to emit Hopper PTX that the driver rejects or that runs incorrectly on SM121.

## Verification

1. Build a minimal FP16 `mma.sync` kernel with `-arch=sm_121` and confirm it runs.
2. Build the same kernel with FP8 `kind::f8f6f4` using `-arch=sm_121a` and confirm `INVALID_PTX` goes away.
3. Run `nvidia-smi` and `cat /proc/driver/nvidia/version` to confirm driver version ≥ 580.
4. For FP4 block scaling, confirm driver ≥ 590 or accept that you cannot load the kernel.

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/`
- `cuda-blackwell-labs/projects/26_triton_gb10/`
- `cuda-blackwell-labs/projects/28_wgmma_tmem/`
- NVIDIA Blackwell Compatibility Guide: https://docs.nvidia.com/cuda/blackwell-compatibility-guide/
- Triton SM121 recipe: https://github.com/triton-lang/triton/issues/10331
- Modular SM121 FP4 issue: https://github.com/modular/modular/issues/6597
- Blackwell GPU Wiki: https://0xsero.github.io/blackwell-gpu-wiki/blackwell/sm100-vs-sm120/
''',
    },
]


def make_workflow_md(skill):
    return f"""---
description: {skill['name'].replace('-', ' ').title()} workflow
---

# {skill['name'].replace('-', ' ').title()} on GB10

Skill: `.devin/skills/{skill['name']}/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/{skill['name']}/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune tile sizes, launch bounds, and SMEM layout for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
"""


def make_command_md(skill):
    return f"""# {skill['name'].replace('-', ' ').title()} on GB10

{skill['description']}

Skill: `.cursor/skills/{skill['name']}/SKILL.md`

## Workflow
1. Read `.cursor/skills/{skill['name']}/SKILL.md`
2. Identify the target kernel/pipeline and data layout
3. Implement the pattern with the exact headers/APIs shown
4. Verify against a CPU or PyTorch/CuPy reference
5. Profile with Nsight Compute and report Tensor Core / memory throughput
6. Tune for GB10's 273 GB/s bandwidth and 99 KB SMEM cap
"""


def make_skill_md(skill, is_devin=True):
    body = skill["devin_body"]
    return f"""---
name: {skill['name']}
description: >-
  {skill['description']}
---

{body}
"""


def write(path, content):
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(content)
    except Exception as e:
        print(f"ERROR: failed to write {path}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    base = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_BASE
    if not os.path.isdir(base):
        print(f"ERROR: {base} is not a directory", file=sys.stderr)
        sys.exit(1)

    for skill in SKILLS:
        write(f"{base}/.devin/skills/{skill['name']}/SKILL.md", make_skill_md(skill))
        write(f"{base}/.devin/workflows/{skill['name']}.md", make_workflow_md(skill))
        write(f"{base}/.cursor/skills/{skill['name']}/SKILL.md", make_skill_md(skill))
        write(f"{base}/.cursor/commands/{skill['name']}.md", make_command_md(skill))

    print("Generated", len(SKILLS) * 4, "files in", base)


if __name__ == "__main__":
    main()
