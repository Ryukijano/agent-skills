---
name: cub-reduce-by-key-gb10
description: >-
  Use CUB cub::DeviceReduce::ReduceByKey on GB10 for grouping and reducing contiguous key runs in device memory. Useful for batched embedding aggregation.
---

# CUB ReduceByKey on GB10 DGX Spark

## Overview

`cub::DeviceReduce::ReduceByKey` finds consecutive runs of equal keys and reduces their associated values. This is the device-wide primitive behind many "group by" operations in embedding and attention code.

## API signature (CCCL 3.x)

```cpp
#include <cub/cub.cuh>

cub::DeviceReduce::ReduceByKey(
    d_temp, temp_storage_bytes,
    d_keys, d_unique_out,
    d_values, d_sums,
    d_num_runs,
    cuda::std::plus<int>{},   // reduction op
    num_items                 // key/value count
);
```

## Two-call pattern

```cpp
size_t temp_bytes = 0;
cub::DeviceReduce::ReduceByKey(nullptr, temp_bytes, ...);
void* d_temp = nullptr;
cudaMalloc(&d_temp, temp_bytes);
cub::DeviceReduce::ReduceByKey(d_temp, temp_bytes, ...);
```

## Verification

Walk the sorted-by-key array on the CPU and sum each contiguous run; compare `d_unique_out`, `d_sums`, and `d_num_runs`.

## Reference

- `cuda-blackwell-labs/projects/38_cub_advanced/`
- https://nvlabs.github.io/cub/structcub_1_1_device_reduce.html

