# Scientific Linear Algebra on GPU

## Description

Dense and sparse linear algebra with cuBLAS, cuSOLVER, cuSPARSE, cuDSS, MAGMA, and device-side cuSolverDx.

## When to use

You need to solve linear systems, factorize matrices, compute eigenvalues, or perform sparse matrix operations on GPU.

## Key concepts

- **cuBLAS**: GPU BLAS (Level 1/2/3) with Tensor Core paths.
- **cuSOLVER**: dense and sparse direct solvers, eigenvalue solvers. `cusolverDn` for dense, `cusolverRF` for refactorization.
- **cuDSS**: new direct sparse solver (replaces `cusolverSP`).
- **cuSPARSE**: SpMV, SpMM, sparse triangular solve, preconditioners.
- **MAGMA**: heterogeneous CPU+GPU LAPACK/ScaLAPACK routines.
- **cuSolverDx**: device-side factorizations for kernel fusion.

## Code pattern

```python
import cupy as cp

A = cp.random.randn(4096, 4096, dtype=cp.float64)
b = cp.random.randn(4096, dtype=cp.float64)
x = cp.linalg.solve(A, b)
```

For PyTorch:

```python
import torch
A = torch.randn(4096, 4096, device='cuda', dtype=torch.float64)
L, pivots = torch.linalg.lu_factor(A)
```

## Tuning notes

- cuBLAS uses Tensor Cores for FP32 (TF32) on Ampere+ and FP16/BF16.
- Large dense systems (>8K) often benefit from MAGMA's two-stage solvers.
- Sparse direct solvers (cuDSS, cuSolverRF) are best for many right-hand sides or refactorization.

## Verification

1. Solve a known linear system and check residual `||Ax - b||`.
2. Compare cuBLAS GEMM to PyTorch `torch.mm` and confirm speedup.
3. Check MAGMA installation with `python -m pip show magma-cuda` or a C test.

## References

- https://docs.nvidia.com/cuda/cublas/
- https://docs.nvidia.com/cuda/cusolver/
- https://docs.nvidia.com/cuda/cudss/
- https://developer.nvidia.com/magma
