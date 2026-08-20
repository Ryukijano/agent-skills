# CUB Segmented Sort on GB10 DGX Spark

## Overview

`cub::DeviceSegmentedSort::SortKeys` (or `SortPairs`) sorts many non-overlapping subsequences in a single device-wide call.

## Usage

```cpp
#include <cub/cub.cuh>

int num_items = ...;
int num_segments = ...;
int* d_offsets;  // length num_segments + 1

size_t temp_bytes = 0;
cub::DeviceSegmentedSort::SortKeys(
    nullptr, temp_bytes,
    d_keys_in, d_keys_out,
    num_items, num_segments,
    d_offsets, d_offsets + 1);

cudaMalloc(&d_temp, temp_bytes);
cub::DeviceSegmentedSort::SortKeys(
    d_temp, temp_bytes,
    d_keys_in, d_keys_out,
    num_items, num_segments,
    d_offsets, d_offsets + 1);
```

## Offsets array

`d_offsets[i]` is the start of segment `i`, `d_offsets[i+1]` is its end. Consecutive segments can be back-to-back or have gaps.

## Verification

For each segment `[begin, end)`, sort the corresponding host slice with `std::sort` and compare.

## Inference use cases

- Sorting attention scores per head
- Top-k per sequence in a batch
- Bucket sorting in MoE routing

## Reference

- `cuda-blackwell-labs/projects/38_cub_advanced/`
- https://nvidia.github.io/cccl/cub/api/structcub_1_1_device_segmented_sort.html

