# cuTile Python on GB10 DGX Spark

## Overview

cuTile is the new tile-based programming model introduced in CUDA 13. It lets you write GPU kernels in Python by operating on tiles (small arrays) instead of individual threads, and it can target Blackwell Tensor Cores and TMA without explicit PTX.

## Installation

Create a venv and install the wheel with the bundled `tileiras` compiler:

```bash
python3 -m venv venv
source venv/bin/activate
pip install "cuda-tile[tileiras]>=1.5.0" cupy-cuda13x
```

Requirements:
- Driver 580+ (GB10 DGX Spark has 580.142)
- Python 3.10+
- `tileiras` 13.2+ (installed by `[tileiras]` extra)

## 1-D vector add

```python
import cupy as cp
import cuda.tile as ct

@ct.kernel
def vector_add(a, b, c, tile_size: ct.Constant[int]):
    pid = ct.bid(0)
    a_tile = ct.load(a, index=(pid,), shape=(tile_size,))
    b_tile = ct.load(b, index=(pid,), shape=(tile_size,))
    c_tile = a_tile + b_tile
    ct.store(c, index=(pid,), tile=c_tile)

n = 2**22
tile_size = 1024
a = cp.random.rand(n, dtype=cp.float32)
b = cp.random.rand(n, dtype=cp.float32)
c = cp.zeros_like(a)
grid = (ct.cdiv(n, tile_size), 1, 1)
ct.launch(cp.cuda.get_current_stream(), grid, vector_add, (a, b, c, tile_size))
```

## 2-D FP32 matrix multiplication

A tiled kernel uses `ct.mma` to accumulate matrix product tiles:

```python
@ct.kernel
def matmul(A, B, C, tm: ct.Constant[int], tn: ct.Constant[int], tk: ct.Constant[int]):
    M = A.shape[0]
    N = B.shape[1]
    bid_m = ct.bid(0) // ct.cdiv(N, tn)
    bid_n = ct.bid(0) % ct.cdiv(N, tn)
    acc = ct.full((tm, tn), 0, dtype=ct.float32)
    num_tiles_k = ct.num_tiles(A, axis=1, shape=(tm, tk))
    for k in range(num_tiles_k):
        a = ct.load(A, index=(bid_m, k), shape=(tm, tk)).astype(ct.float32)
        b = ct.load(B, index=(k, bid_n), shape=(tk, tn)).astype(ct.float32)
        acc = ct.mma(a, b, acc)
    ct.store(C, index=(bid_m, bid_n), tile=acc)
```

For a production matmul, use the upstream sample which adds 2-D block swizzling and `ct.tfloat32` for Tensor Core.

## Key environment notes

- The `tileiras` compiler bundled in the wheel is used automatically; you do **not** need `TRITON_PTXAS_PATH`.
- Kernels must be defined in a real `.py` file (not `python - <<'PY'` heredocs) because cuTile uses `inspect.getsource`.
- Large constants are passed through the argument tuple and annotated with `ct.Constant[int]`.

## Verification pattern

- Compare against `cp.matmul` or `A @ B` with a tolerance of `1e-3` when `ct.mma` uses TF32/Tensor Core.
- Report memory bandwidth (GB/s) for elementwise ops and TFLOPS for GEMM.

## Reference

- `cuda-blackwell-labs/projects/33_cutile_python/`
- https://docs.nvidia.com/cuda/cutile-python/
- https://github.com/NVIDIA/cutile-python
