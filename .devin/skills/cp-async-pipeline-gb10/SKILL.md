---
name: cp-async-pipeline-gb10
description: >-
  Build multi-stage async copy pipelines with `cp.async` on GB10. Covers commit/wait groups, mbarriers, double/triple buffering, and why SM121 uses `cp.async` instead of TMA for GMEM->SMEM staging.
---

# `cp.async` Pipelines on GB10 DGX Spark

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

