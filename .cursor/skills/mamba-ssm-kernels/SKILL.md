# Mamba State-Space Model Kernels on GPU

## Description

Mamba-2/3 SSD kernels, fused selective scan, CuTe/Triton/TileLang backends, and chunk scheduling.

## When to use

You are implementing or optimizing Mamba-style state-space models on GPU, especially for long-context or autoregressive inference.

## Key concepts

- **Mamba-2 SSD**: State-Space Duality; the five-kernel pipeline can be fused into one.
- **Selective scan**: linear-time recurrence with input-dependent state transitions.
- **Backends**: Triton (general), CuTe (`mamba3_step_fn`), TileLang (MIMO training).
- **Chunk scheduling**: chunk size impacts memory vs speed (e.g., static 128/256/512).

## Code pattern

```python
# PyTorch fused Mamba-2 SSD
from mamba_ssm import Mamba2
layer = Mamba2(d_model=1024, d_state=64, d_conv=4)
out = layer(x)
```

## Tuning notes

- Fused Triton SSD can be 1.5-2.5× faster than the unfused baseline.
- On Blackwell (sm_100), watch for `ptxas` register spilling; reduce `num_warps`.
- CuTe backend is best for low-latency autoregressive decode.

## Verification

1. Run `mamba2` forward and compare to a reference PyTorch selective scan.
2. Benchmark with different chunk sizes and plot latency vs memory.
3. On GB200, check for `ptxas C7907` and adjust autotune configs.

## References

- https://pytorch.org/blog/accelerating-mamba2-with-kernel-fusion/
- https://github.com/state-spaces/mamba
- https://github.com/state-spaces/mamba/issues/904
- https://arxiv.org/html/2604.10597v3
