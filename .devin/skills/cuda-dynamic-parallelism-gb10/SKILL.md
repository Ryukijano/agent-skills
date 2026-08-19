---
name: cuda-dynamic-parallelism-gb10
description: >-
  Use CUDA Dynamic Parallelism (CDP) on GB10: parent kernels that launch child kernels
  with <<< >>> inside device code, compiling with -rdc=true and linking -lcudadevrt.
---

# CUDA Dynamic Parallelism on GB10 DGX Spark

## Overview

CUDA Dynamic Parallelism (CDP) lets a kernel launch other kernels. This is useful when the parallelism of a sub-problem is not known until runtime or when each thread/block must spawn an independent parallel task.

## Compilation

You must compile with relocatable device code and link the device runtime:

```bash
nvcc -arch=sm_121a -O2 -std=c++17 -rdc=true cdp.cu -o cdp -lcudart -lcudadevrt
```

## Basic pattern: parent launches child

```cpp
// Child kernel
__global__ void row_sum_child(const float* row_in, float* row_out, int N) {
    extern __shared__ float sdata[];
    int tid = threadIdx.x;
    float sum = 0.0f;
    for (int i = tid; i < N; i += blockDim.x) sum += row_in[i];
    sdata[tid] = sum;
    __syncthreads();

    for (int offset = blockDim.x / 2; offset > 0; offset /= 2) {
        if (tid < offset) sdata[tid] += sdata[tid + offset];
        __syncthreads();
    }
    if (tid == 0) *row_out = sdata[0];
}

// Parent kernel: one block per row
__global__ void row_sum_parent(const float* A, float* sums, int rows, int cols) {
    int row = blockIdx.x;
    if (row >= rows) return;
    row_sum_child<<<1, 256, 256 * sizeof(float)>>>(A + row * cols, sums + row, cols);
}
```

## Host side

```cpp
row_sum_parent<<<rows, 1>>>(d_A, d_sums, rows, cols);
cudaDeviceSynchronize();  // waits for parent and all children
```

## Pitfalls

- Child kernels inherit the parent's stream and CUDA context.
- Each child launch has non-trivial overhead; do not use CDP for very fine-grained work.
- Recursive nesting depth is limited (default 24); query/adjust with `cudaLimitDevRuntimeSyncDepth` if needed.
- Memory allocations inside kernels (`cudaMalloc`/`cudaFree`) are legal but slow; prefer pre-allocated buffers.

## Verification

Use a simple synthetic input where the expected output is easy to compute. For the row-sum example, set `A[i][j] = i` so each row sum is `i * cols`.

## Reference

- `cuda-blackwell-labs/projects/36_cuda_dynamic_parallelism/`
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-dynamic-parallelism
