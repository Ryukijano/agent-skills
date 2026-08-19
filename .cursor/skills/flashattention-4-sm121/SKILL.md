# FlashAttention-4 on DGX Spark (SM121)

## Description

FlashAttention-4 consumer Blackwell support on sm_120/sm_121: paged KV, head_dim limits, FP8, and the CuTe DSL dispatch path.

## When to use

You are running vLLM/SGLang on a DGX Spark or RTX 50-series and want to use the FlashAttention-4 CuTe DSL backend for attention.

## Key concepts

- **sm_120/121 path**: uses SM80-style `mma.sync.m16n8k16` with cp.async, no WGMMA, no tcgen05, no TMEM.
- **SMEM budget**: 99 KB per block (vs 163 KB on SM80, 228 KB on Hopper).
- **TMA**: single-CTA only, no multicast.
- **Paged KV**: implemented with in-kernel page table resolution (PR #2348).
- **FP8 KV cache decode**: supported for e4m3/e5m2, ~1.6-1.9× at GQA ratio ≤4.
- **FA4 in vLLM**: opt-in via `--attention-backend FLASH_ATTN_4`; `enforce_eager=True` required.

## Code pattern

```bash
# vLLM with FA4 on SM120/SM121
vllm serve model --attention-backend FLASH_ATTN_4 --enforce-eager
```

If using the downstream bundle:

```python
import flash_attn_4
out, _ = flash_attn_4.flash_attn_func(q, k_paged, v_paged, page_table=page_table, causal=True)
```

## Tuning notes

- `head_dim` 64 and 128 are best; 256 works but uses smaller tiles.
- `head_dim > head_dim_v` is routed to non-TMA to avoid hangs.
- Clear Triton cache when switching between FA versions: `rm -rf ~/.triton/cache`.

## Verification

1. Run `flash_attn_varlen_func` with a small paged KV tensor and compare to a reference attention.
2. Check vLLM logs that `FLASH_ATTN_4` backend is active.
3. Benchmark throughput vs `FLASHINFER` and vs `TRITON_ATTN`.

## References

- https://github.com/Dao-AILab/flash-attention/pull/2634
- https://github.com/Dao-AILab/flash-attention/pull/2348
- https://huggingface.co/SecondNatureComputing/flash-attn-4-sm120
- https://github.com/vllm-project/vllm/pull/40110
