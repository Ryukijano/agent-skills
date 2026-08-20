# CUB Device-Wide Algorithms on GB10 DGX Spark

## Overview

CUB provides speed-of-light parallel primitives (`DeviceReduce`, `DeviceScan`, `DeviceRadixSort`, etc.) on the GPU. The CUDA 13.0 system install on the Spark does **not** include CUB/Thrust headers, so you usually fetch them through the `nvidia-cuda-cccl` PyPI wheel.

## Fetching headers

```bash
python3 -m venv venv
source venv/bin/activate
pip install nvidia-cuda-cccl==13.0.50
CCCL_INC=$(find venv/lib -path '*/cccl/cub/cub.cuh' -print -quit | sed 's|/cub/cub.cuh||')
```

In a Makefile:

```makefile
CCCL_INC = $(shell find $(VENV)/lib -path '*/cccl/cub/cub.cuh' -print -quit 2>/dev/null | sed 's|/cub/cub.cuh$$||')
NVCCFLAGS += -I"$(CCCL_INC)"
```

## Device reduce

```cpp
#include <cub/cub.cuh>

size_t temp_bytes = 0;
void* d_temp = nullptr;
cub::DeviceReduce::Sum(nullptr, temp_bytes, d_in, d_out, n);
cudaMalloc(&d_temp, temp_bytes);
cub::DeviceReduce::Sum(d_temp, temp_bytes, d_in, d_out, n);
```

## Device inclusive scan

```cpp
cudaFree(d_temp); d_temp = nullptr; temp_bytes = 0;
cub::DeviceScan::InclusiveSum(nullptr, temp_bytes, d_in, d_out, n);
cudaMalloc(&d_temp, temp_bytes);
cub::DeviceScan::InclusiveSum(d_temp, temp_bytes, d_in, d_out, n);
```

## Device radix sort

```cpp
cudaFree(d_temp); d_temp = nullptr; temp_bytes = 0;
cub::DeviceRadixSort::SortKeys(nullptr, temp_bytes, d_keys, d_out, n);
cudaMalloc(&d_temp, temp_bytes);
cub::DeviceRadixSort::SortKeys(d_temp, temp_bytes, d_keys, d_out, n);
```

## Important two-call pattern

Every CUB device-wide primitive follows the same pattern:

1. First call with `d_temp_storage == nullptr` writes the required temporary size to `temp_storage_bytes`.
2. Allocate that much device memory.
3. Second call performs the operation.

**Do not reuse a temporary buffer from a different primitive without re-querying the size.**

## Verification

- Reduce: compare to `std::accumulate`.
- Scan: walk the output and confirm each element is the cumulative sum.
- Sort: compare to a CPU `std::sort` of the same keys.

## Reference

- `cuda-blackwell-labs/projects/35_cub_algorithms/`
- https://nvlabs.github.io/cub/
- https://github.com/NVIDIA/cccl
