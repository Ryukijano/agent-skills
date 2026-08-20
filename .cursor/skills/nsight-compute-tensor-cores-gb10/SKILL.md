# Profiling Tensor Cores with Nsight Compute on GB10 DGX Spark

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
ncu --metrics sm__pipe_tensor_cycles_active.avg.pct_of_peak_sustained_active,              dram__bytes_read.sum.per_second,              l1tex__data_bank_conflicts_pipe_lsu_mem_shared.sum               ./my_kernel
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

