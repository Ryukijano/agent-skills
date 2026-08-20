# High-Performance Python

## Description

Numba, Cython, pybind11, vectorization, and profiling for Python code that rivals C/Fortran speed.

## When to use

Your Python ML/scientific code is too slow and you want to keep (most of) the Python ecosystem while approaching compiled-language speed.

## Key concepts

- **Numba**: JIT compilation of NumPy-aware Python functions via LLVM.
- **Cython**: static compilation with optional type annotations and C/C++ interop.
- **pybind11**: lightweight header-only bindings for C++ extensions.
- **Vectorization and memory layout**: contiguous arrays, row/column-major order.
- **Profiling**: cProfile, line_profiler, py-spy, and profilers to find hotspots.

## Code pattern

```python
from numba import njit, prange
import numpy as np

@njit(parallel=True)
def sum_rows(a):
    m, n = a.shape
    out = np.empty(m)
    for i in prange(m):
        out[i] = a[i, :].sum()
    return out
```

## Tuning notes

- Numba works best with numerical NumPy/loops; avoid object types and unsupported Python features.
- Cython pays off when you need C-level structs, typed memoryviews, or static binding.
- Cache Numba-compiled functions with `cache=True` and profile before optimizing.

## Verification

1. Benchmark a hotspot before and after Numba/Cython/pypbind11.
2. Verify numerical output matches the pure-Python reference implementation.
3. Profile memory and cache behavior; ensure array layout is contiguous.

## References

- https://numba.pydata.org/
- https://cython.org/
- https://www.github.com/pybind/pybind11
- https://github.com/numba/numba
