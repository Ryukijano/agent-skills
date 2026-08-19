---
name: cooperative-groups-gb10
description: >-
  Use Cooperative Groups on GB10 (sm_121): thread_block_tile, grid_group, this_grid(),
  and cudaLaunchCooperativeKernel for single-pass multi-block reductions and other
  cross-block cooperative algorithms.
---

# Cooperative Groups on GB10 DGX Spark

## Overview

Cooperative Groups (CG) let you define, partition, and synchronize groups of threads explicitly, from warps up to the entire grid. On GB10 you can use `cg::this_grid()` together with `cudaLaunchCooperativeKernel` to run algorithms that span all blocks without returning to the host.

## Essential headers and namespace

```cpp
#include <cooperative_groups.h>
#include <cooperative_groups/reduce.h>
namespace cg = cooperative_groups;
```

## Grid-level cooperative launch

A cooperative kernel must be launched with `cudaLaunchCooperativeKernel`. The device must report `prop.cooperativeLaunch == true`.

```cpp
extern "C" __global__ void reduceSinglePass(const float* in, float* out, unsigned int n) {
    cg::thread_block block = cg::this_thread_block();
    cg::grid_group   grid  = cg::this_grid();

    extern __shared__ float sdata[];
    sdata[block.thread_rank()] = 0.0f;

    for (unsigned int i = grid.thread_rank(); i < n; i += grid.size()) {
        sdata[block.thread_rank()] += in[i];
    }
    cg::sync(block);

    // Warp-level reduce
    cg::thread_block_tile<32> tile32 = cg::tiled_partition<32>(block);
    sdata[block.thread_rank()] = cg::reduce(tile32, sdata[block.thread_rank()], cg::plus<float>());
    cg::sync(block);

    // Final block partial
    if (block.thread_rank() == 0) {
        float sum = 0.0f;
        for (int i = 0; i < block.size(); i += 32) sum += sdata[i];
        out[blockIdx.x] = sum;
    }
    cg::sync(grid);

    // Serial combine by thread 0 of the grid
    if (grid.thread_rank() == 0) {
        float total = 0.0f;
        for (int b = 0; b < gridDim.x; ++b) total += out[b];
        out[0] = total;
    }
}
```

## Host launch

```cpp
int numBlocks;
cudaOccupancyMaxActiveBlocksPerMultiprocessor(&numBlocks, reduceSinglePass, threads, smemBytes);
numBlocks *= prop.multiProcessorCount;

void* args[] = { (void*)&d_in, (void*)&d_out, (void*)&n };
dim3 block(threads, 1, 1);
dim3 grid(numBlocks, 1, 1);
cudaLaunchCooperativeKernel((void*)reduceSinglePass, grid, block, args, smemBytes, nullptr);
```

## Common pitfalls

- `cg::this_grid()` is only available in kernels launched via `cudaLaunchCooperativeKernel`.
- Do not mix `__syncthreads()` and `cg::sync(block)` for the same group in inconsistent ways; pick one style per kernel.
- The final grid-level serial combine is O(numBlocks); keep `numBlocks` modest or use a second reduction pass if `numBlocks` is huge.

## Reference

- `cuda-blackwell-labs/projects/34_cooperative_groups_reduction/`
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cooperative-groups
- https://github.com/NVIDIA/cuda-samples/tree/master/cpp/2_Concepts_and_Techniques/reductionMultiBlockCG
