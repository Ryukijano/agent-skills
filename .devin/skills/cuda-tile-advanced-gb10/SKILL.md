# Advanced CUDA Tile / cuTile on GB10

## Description

cuTile Python/C++ advanced features: block-scaled `ct.mma_scaled`, Tile IR, persistent kernels, and Nsight Tile profiling.

## When to use

You are writing or optimizing tile-based GPU programs with cuTile Python/CUDA Tile, especially block-scaled FP8/FP4 or persistent matmul.

## Key concepts

- **`@ct.kernel`**: entry point; `ct.load`, `ct.store`, `ct.mma`, `ct.mma_scaled`.
- **`ct.mma_scaled`**: block-scaled MMA. Scale block sizes: 16/32 for FP4, 32 for FP8.
- **Tile IR**: virtual ISA; source ↔ Tile IR ↔ SASS correlation in Nsight Compute (future).
- **Persistent kernels**: fewer tile blocks process multiple output tiles.
- **Nsight Tile profiling**: Tile section in Nsight Compute 2026.1+.

## Code pattern

```python
import cuda.tile as ct
import torch

@ct.kernel
def scaled_matmul(A, A_s, B, B_s, C, Ks: int):
    # load tiles, compute scaled MMA
    a = ct.load(A, ...)
    a_s = ct.load(A_s, ...)
    b = ct.load(B, ...)
    b_s = ct.load(B_s, ...)
    acc = ct.mma_scaled(a, a_s, b, b_s, ct.zeros(...))
    ct.store(C, acc)
```

## Tuning notes

- cuTile Python currently supports Ampere, Ada, Blackwell (sm_100 and sm_120/121).
- Match scale tensor layout to expected TMA swizzle (e.g., `Swizzle32x4x4`).
- For persistent kernels, choose tile shapes that fit SMEM (99 KB on sm_121).

## Verification

1. Compile and run the cuTile `MatMul.py` sample.
2. Compare a cuTile FP8 matmul to `torch.matmul` with FP8 weights.
3. Profile with Nsight Compute and inspect the Tile section.

## References

- https://docs.nvidia.com/cuda/cutile-python/
- https://docs.nvidia.com/cuda/cutile-python/generated/cuda.tile.mma_scaled.html
- https://docs.nvidia.com/cuda/tile-ir/latest/
- https://developer.nvidia.com/blog/how-to-write-high-performance-matrix-multiply-in-nvidia-cuda-tile/
