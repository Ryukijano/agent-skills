# CDP Recursive Quicksort on GB10 DGX Spark

## Overview

CDP lets a kernel recursively spawn child kernels. Quicksort is the classic textbook example: each pass partitions the array and launches child kernels for the two sub-arrays.

## Pattern

```cpp
__global__ void quicksort_kernel(int* data, int left, int right, int depth) {
    if (right - left <= 32 || depth > MAX_DEPTH) {
        // fall back to local insertion sort
        return;
    }

    int pivot = partition(data, left, right);  // one block
    if (left < pivot - 1)
        quicksort_kernel<<<1, 128>>>(data, left, pivot - 1, depth + 1);
    if (pivot + 1 < right)
        quicksort_kernel<<<1, 128>>>(data, pivot + 1, right, depth + 1);
}
```

## Compilation

```bash
nvcc -arch=sm_121a -O2 -rdc=true quicksort.cu -o quicksort -lcudart -lcudadevrt
```

## Important limits

- Default max device runtime sync depth is 24; increase with:
  ```cpp
  cudaDeviceSetLimit(cudaLimitDevRuntimeSyncDepth, 32);
  ```
- Launching many tiny child kernels has overhead; use a leaf size cutoff (e.g. 32-128).
- Child kernels inherit the parent stream; `cudaDeviceSynchronize()` on the host waits for the whole tree.

## Reference

- `cuda-blackwell-labs/projects/36_cuda_dynamic_parallelism/`
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-dynamic-parallelism

