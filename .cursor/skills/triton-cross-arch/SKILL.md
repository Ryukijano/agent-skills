# Triton Cross-Architecture (Ampere/Hopper/Blackwell)

## Description

Writing and deploying Triton kernels across sm_80, sm_89, sm_90, sm_100, sm_120, and sm_121.

## When to use

You write custom Triton kernels that must run on A100, L40S, H100, B200, RTX 50-series, or DGX Spark.

## Key concepts

- **Compute capability targeting**: Triton derives `ptxas` target from `cc` arg or env.
- **`TRITON_PTXAS_PATH`**: point to CUDA 13.0+ `ptxas` for sm_121 support.
- **`TRITON_OVERRIDE_ARCH`**: usually leave unset. Setting `sm_90` on Blackwell can produce silent wrong results.
- **No `sm_120a`**: consumer Blackwell has no `a` variant; Triton fix (PR #9734) removed `a` for sm_120.
- **Unified memory on GB10**: Triton may mis-handle `cudaMallocManaged` regions; use explicit `cudaMalloc`.

## Code pattern

```python
import triton
import triton.language as tl

@triton.jit
def add_kernel(x_ptr, y_ptr, out_ptr, n, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < n
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    tl.store(out_ptr + offsets, x + y, mask=mask)
```

## Tuning notes

- `num_warps=4` is a good default; profile 2/4/8.
- `num_stages=3-4` for compute-bound GEMM; `2-3` for memory-bound.
- SMEM limits: 164 KB (A100), 228 KB (H100), 99 KB (sm_120/121), 228 KB (sm_100).

## Verification

1. Run the kernel on a small tensor and compare to PyTorch.
2. Clear Triton cache when switching architectures: `rm -rf ~/.triton/cache`.
3. On GB10: set `TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas` and `TORCH_CUDA_ARCH_LIST="12.1+PTX"`.

## References

- https://triton-lang.org/main/python-api/generated/triton.autotune.html
- https://github.com/triton-lang/triton/pull/9734
- https://github.com/triton-lang/triton/issues/10331
- https://github.com/triton-lang/kernels/blob/main/kernels/matmul.py
