# PyTorch Deployment on Blackwell

## Description

PyTorch nightly wheels, sm_100/sm_120 support, architecture detection, and common Blackwell-specific errors.

## When to use

You are installing or debugging PyTorch on B200/GB200 (sm_100) or RTX 50-series/DGX Spark (sm_120/sm_121).

## Key concepts

- **PyTorch 2.7+ with CUDA 12.8+** is required for Blackwell.
- **Nightly wheels**: `pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128`.
- **sm_100 vs sm_120**: datacenter vs consumer; binaries are not interchangeable.
- **No `sm_120a`**: consumer Blackwell has no `a` variant.
- **Common errors**: "sm_120 is not compatible" from old CUDA 12.1 binaries; DDP segfaults on sm_120; FP4 cast kernels missing.

## Code pattern

```bash
pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128
```

Check:

```python
import torch
print(torch.cuda.get_arch_list())
print(torch.cuda.get_device_properties(0))
```

## Tuning notes

- For `sm_120a` suffix stripping bug, set `TORCH_CUDA_ARCH_LIST="12.0a"`.
- `CUDA_FORCE_PTX_JIT=1` can test PTX compatibility.
- Use `torch.compile` with `max-autotune` for best Blackwell kernels.

## Verification

1. `torch.cuda.is_available()` and `get_arch_list()` show the target arch.
2. Run a small FP16 GEMM and compare to `torch._scaled_mm` with FP8.
3. Run `torch.compile` on a simple model and confirm it generates Triton/CuTeDSL kernels.

## References

- https://discuss.pytorch.org/t/pytorch-support-for-sm120/216099
- https://github.com/pytorch/pytorch/issues/172807
- https://discuss.pytorch.org/t/solved-rtx-5090-sm-120-training-segfault-ddp-was-the-cause/224584
- https://docs.nvidia.com/cuda/blackwell-compatibility-guide/
