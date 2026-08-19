---
name: cooperative-groups-warp-tile-gb10
description: >-
  Use Cooperative Groups `cg::tiled_partition` and `cg::thread_block_tile` for warp-level reduction, scan, and matrix/vector operations on GB10.
---

# Cooperative Groups Warp-Tile Primitives on GB10

## Overview

`cg::tiled_partition<N>(block)` gives you a sub-warp (or full 32-thread warp) as a first-class group. You can use `cg::reduce`, `cg::scan`, and `cg::shfl` on it.

## Warp-level reduction

```cpp
#include <cooperative_groups.h>
#include <cooperative_groups/reduce.h>
namespace cg = cooperative_groups;

__global__ void warp_reduce(float* in, float* out, int n) {
    auto block = cg::this_thread_block();
    auto tile  = cg::tiled_partition<32>(block);
    int tid = blockIdx.x * blockDim.x + threadIdx.x;

    float v = (tid < n) ? in[tid] : 0.0f;
    float sum = cg::reduce(tile, v, cg::plus<float>());
    if (tile.thread_rank() == 0)
        out[blockIdx.x] = sum;
}
```

## Sub-warp tiles

```cpp
auto tile4 = cg::tiled_partition<4>(cg::this_thread_block());
// 4 threads act as a group; useful for 4-element vector ops
```

## Common operations

- `cg::shfl(tile, value, src_lane)` — broadcast
- `cg::reduce(tile, value, op)` — warp sum/min/max
- `cg::inclusive_scan(tile, value, op)` — prefix sum inside the warp

## Pitfalls

- `cg::reduce` requires all threads in the tile to call it with the same operation.
- Divergence inside a warp still kills performance; keep all threads participating.
- `tiled_partition` size must divide the warp size (32) evenly: 1, 2, 4, 8, 16, 32.

## Reference

- `cuda-blackwell-labs/projects/34_cooperative_groups_reduction/`
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#warp-level-primitives

