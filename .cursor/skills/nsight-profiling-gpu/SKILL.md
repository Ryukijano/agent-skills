# Nsight Compute and Nsight Systems Profiling

## Description

Nsight Compute sections/metrics, Nsight Systems gap analysis, hardware CUDA trace, and Tile profiling for cuTile.

## When to use

You need to profile GPU kernels and identify memory vs compute bottlenecks, occupancy, register pressure, or gaps in a CUDA graph.

## Key concepts

- **Nsight Compute**: section-based profiling. Key sections: ComputeWorkloadAnalysis, MemoryWorkloadAnalysis, Occupancy, InstructionStats.
- **Nsight Systems**: application-level tracing. Use `--trace=cuda-hw` on Blackwell for hardware event system trace.
- **Tile profiling**: Nsight Compute 2026.1+ has a Tile section for cuTile/CUDA Tile kernels.
- **Serialization**: Nsight Compute serializes kernel launches by default; use Range Replay for concurrent kernels.

## Code pattern

```bash
# Nsight Compute
ncu -o profile.ncu-rep --set full ./my_kernel

# Nsight Systems
nsys profile --trace=cuda-hw --cuda-graph-trace=graph -o profile.nsys-rep ./train.py

# Nsight Python
nsys profile --trace=cuda,nvtx,osrt,python -o profile.nsys-rep python train.py
```

## Tuning notes

- A memory-bound kernel has high `memory__bytes` relative to compute; increase data reuse or occupancy.
- A compute-bound kernel has high `sm__pipe_tensor_cycles_active`; check tensor core utilization.
- Register spilling shows up as `sass__inst_executed_register_spilling` in Nsight Compute 2026.1+.

## Verification

1. Profile a GEMM kernel and confirm tensor core utilization is >80%.
2. Run Nsight Systems on a training step and identify the largest GPU idle gap.
3. For cuTile, verify the Tile section appears in Nsight Compute with driver 580.126.09+.

## References

- https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html
- https://docs.nvidia.com/nsight-systems/UserGuide/index.html
- https://docs.nvidia.com/nsight-compute/ReleaseNotes/topics/library-support-tile.html
- https://developer.nvidia.com/nsight-compute-2026_1-new-features
