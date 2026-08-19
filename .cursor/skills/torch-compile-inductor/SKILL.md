# torch.compile and Inductor for NVIDIA GPUs

## Description

PyTorch 2.7+ `torch.compile`, Inductor autotune, custom operators, CuTeDSL/Gluon backends, and debug.

## When to use

You want to accelerate PyTorch models on H100/Blackwell/L40S with `torch.compile` and need to tune or debug the generated kernels.

## Key concepts

- **Inductor modes**: `default`, `reduce-overhead` (CUDA Graphs), `max-autotune` (benchmarks kernels).
- **Backends**: ATen, Triton, CUTLASS, CuTeDSL, NVGEMM.
- **Custom operators**: `torch.library.custom_op`, `torch.library.register_kernel`.
- **Gluon / CuTeDSL**: explicit tile/warp/TMA programming as Inductor backends (experimental).
- **Blackwell template**: persistent matmul with TMA for Blackwell.

## Code pattern

```python
import torch

model = torch.compile(model, mode="max-autotune", fullgraph=False)

# Debug compile
import torch._inductor.config as cfg
cfg.debug = True
```

For a captured kernel source:

```python
src = torch.compiler.generate_kernel(fn, (x,))
```

## Tuning notes

- `max-autotune` can take minutes to compile but yields best throughput.
- Disable inductor for data-dependent shapes: `torch.compile(..., dynamic=False)`.
- For Blackwell, use CUDA 12.8+ nightly PyTorch wheels.

## Verification

1. Compare `torch.compile(model)` vs `model` on a benchmark batch.
2. Run `TORCH_COMPILE_DEBUG=1` and inspect generated Triton/C++ code.
3. Verify `torch.cuda.get_arch_list()` includes your target arch.

## References

- https://pytorch.org/docs/stable/generated/torch.compile.html
- https://github.com/pytorch/pytorch/pull/162916
- https://github.com/pytorch/pytorch/pull/180953
- https://github.com/pytorch/pytorch/issues/188212
