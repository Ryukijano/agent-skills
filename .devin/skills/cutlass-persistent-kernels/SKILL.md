# CUTLASS Persistent and Warp-Specialized Kernels

## Description

CUTLASS 3.x persistent kernels, cooperative vs ping-pong schedule, warp specialization, and CollectiveBuilder for FP8/FP4.

## When to use

You are writing high-performance GEMM kernels with CUTLASS 3.x/4.x and want to use persistent scheduling or block-scaled FP8/FP4.

## Key concepts

- **Cooperative schedule**: two consumer warpgroups work on the same output tile split along M. Cannot hide epilogue.
- **Ping-pong schedule**: two consumer warpgroups work on different tiles; can hide epilogue behind math.
- **Warp specialization**: producer warps load data (TMA/cp.async), consumer warps do MMA.
- **CollectiveBuilder**: composes mainloop and epilogue for block-scaled FP8/FP4.
- **SM100 vs SM120**: SM100 uses tcgen05/TMA multicast; SM120/121 uses `mma.sync` and cluster size 1.

## Code pattern

```cpp
// Ping-pong schedule on Hopper/Blackwell
using KernelSchedule = cutlass::gemm::KernelTmaWarpSpecializedPingpong;

// CollectiveBuilder for block-scaled FP8
using CollectiveMainloop = typename cutlass::gemm::collective::CollectiveBuilder<
    ArchTag, OperatorClass, ElementA, LayoutA, AlignmentA,
    ElementB, LayoutB, AlignmentB, ElementAccumulator,
    TileShape, ClusterShape, StageCount, KernelSchedule>::CollectiveOp;
```

## Tuning notes

- Persistent kernels amortize launch overhead and improve occupancy.
- SMEM limits: 164 KB (A100), 228 KB (H100), 99 KB (sm_120/121), 228 KB (sm_100).
- CUTLASS 4.4.0 adds SM121 support; CuTe DSL may need `sm_121a` patch.

## Verification

1. Build a CUTLASS example (e.g., `49_collective_builder`) and compare to cuBLAS.
2. Check Nsight Compute for high tensor core utilization and low launch overhead.
3. On GB10, verify the kernel does not use tcgen05/TMEM (will fail to load).

## References

- https://docs.nvidia.com/cutlass/latest/media/docs/cpp/gemm_api_3x.html
- https://github.com/NVIDIA/cutlass/blob/main/examples/48_hopper_warp_specialized_gemm/48_hopper_warp_specialized_gemm.cu
- https://github.com/NVIDIA/cutlass/blob/main/examples/49_hopper_gemm_with_collective_builder/49_collective_builder.cu
- https://docs.nvidia.com/cutlass/4.4.0/CHANGELOG.html
