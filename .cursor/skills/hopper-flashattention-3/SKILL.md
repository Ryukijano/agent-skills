# FlashAttention-3 on Hopper

## Description

FlashAttention-3 warp specialization, WGMMA/TMA pipelining, and FP8 block quantization on H100/H200.

## When to use

You need the fastest attention implementation on H100/H200, especially for long-context prefill and training.

## Key concepts

- **Asynchronous WGMMA + TMA** to overlap Q/K/V loads with the GEMM and softmax.
- **Producer/consumer warp groups**: one warp group handles TMA loads, the other executes WGMMA and softmax.
- **Online softmax**: running max and sum are tracked so the final P·V can be fused with the softmax.
- **FP8 block quantization**: Q/K/V are quantized to FP8 with incoherent processing to maintain accuracy.

## Code pattern

The upstream `flash-attention` repo provides `flash_attn_func` and `flash_attn_varlen_func`:

```python
from flash_attn import flash_attn_func
out = flash_attn_func(q, k, v, causal=False)
```

For profiling, set `FLASH_ATTENTION_TRITON_HOPPER` env to test the Triton path.

## Tuning notes

- FlashAttention-3 is Hopper-optimized; on Ada/Ampere it falls back to FlashAttention-2.
- Use `head_dim` 64/128 for best FP8 throughput; 256 may regress.
- For decode-heavy workloads, consider FlashAttention-2 or paged variants (FlashInfer) instead.

## Verification

1. Run `pytest tests/test_flash_attn.py -k "test_flash_attn_fp8"` on H100 if available.
2. Benchmark vs PyTorch SDPA and vs FlashAttention-2.
3. Check Nsight Compute: `sm__pipe_tensor_cycles_active` should be high during the kernel.

## References

- https://tridao.me/publications/flash3/flash3.pdf
- https://tridao.me/blog/2024/flash3/
- https://github.com/Dao-AILab/flash-attention
- https://github.com/Dao-AILab/flash-attention/blob/main/AI/SM90_BLOCK_SIZE_TUNING.md
