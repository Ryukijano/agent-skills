# CUDA Kernel Optimization for GB10 DGX Spark

## Overview
Techniques for optimizing CUDA kernels on the GB10 Grace Blackwell (SM121, 128GB unified LPDDR5X).

## GB10 Architecture
- **Compute Capability**: 12.1 (sm_121)
- **Memory**: 128GB unified LPDDR5X (~273 GB/s peak, NOT HBM)
- **SMs**: 10 SMs, 128 CUDA cores/SM
- **Tensor Cores**: Blackwell 5th gen, FP4/FP8/FP16/BF16/TF32
- **Key constraint**: Memory bandwidth is the primary bottleneck (no HBM)

## Optimization Workflow
1. **Profile with ncu**: `python3 mcp_servers/cuda_profiling/server.py --cli profile_ncu --command ./kernel`
2. **Check occupancy**: Aim for >50% occupancy
3. **Memory coalescing**: Ensure 128-byte aligned accesses
4. **Shared memory**: Use for data reuse, bank conflict avoidance
5. **Tensor Cores**: Use `wmma` or `tcgen05` for matrix ops
6. **SASS inspection**: `python3 mcp_servers/cuda_profiling/server.py --cli dump_sass --binary ./kernel`
7. **Benchmark**: `python3 mcp_servers/cuda_profiling/server.py --cli benchmark_kernel --command ./kernel`

## Common Bottlenecks on GB10
- **Memory bandwidth**: LPDDR5X is 6x slower than HBM. Optimize memory access patterns first.
- **Occupancy**: Large register files reduce occupancy. Use `__launch_bounds__`.
- **Warp divergence**: Minimize branch divergence within warps.
- **PCIe transfers**: Unified memory avoids explicit copies but watch for page faults.

## Compilation Flags
```bash
nvcc -arch=sm_121 -O2 -lineinfo -Xptxas=-v kernel.cu -o kernel
```
- `-lineinfo`: Required for ncu profiling
- `-Xptxas=-v`: Shows register usage and spill count
- `-O3`: Aggressive optimization (may increase register pressure)

## Tensor Core Usage
```cpp
#include <cuda/barrier>
#include <cuda/std/utility>
// Use tcgen05 instructions for Blackwell tensor cores
// Or use cuBLAS for GEMM: cublasGemmEx with CUDA_R_16BF
```

## MCP Tools
- `profile_ncu`: Per-kernel metrics (occupancy, stall reasons, memory throughput)
- `dump_sass`: Verify compiler-generated instructions
- `dump_ptx`: Check PTX intermediate representation
- `memcheck`: Detect memory errors
- `benchmark_kernel`: Multi-run timing

## Reference Files
- CUDA Labs: `learning-plans/cuda-blackwell-labs/`
- MCP Server: `mcp_servers/cuda_profiling/server.py`
- NVIDIA CUDA MCP: `nvidia-cuda-docs` (hosted MCP server)

