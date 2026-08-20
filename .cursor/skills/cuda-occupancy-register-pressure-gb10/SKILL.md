# CUDA Occupancy and Register Pressure on GB10 DGX Spark

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

