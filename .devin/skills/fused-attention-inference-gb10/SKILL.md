---
name: fused-attention-inference-gb10
description: >-
  Build fused attention kernels for fast LLM inference on GB10. Covers online softmax, FlashAttention tiling, KV-cache slicing, and causal/left-padding masks.
---

# Fused Attention for Inference on GB10 DGX Spark

## Overview

FlashAttention-style fused attention is the main way to make LLM inference memory-bound instead of memory-proportional. It loads Q/K/V tiles once, computes attention in SRAM, and writes only the output.

## Algorithm

For a Q tile `(Br, d)` and K/V tiles `(Bc, d)`:

```cpp
m = -INFINITY
l = 0
acc = 0
for each KV tile:
    S = Q * K^T                 // (Br, Bc)
    m_new = max(m, max(S, axis=1))
    P = exp(S - m_new)          // online softmax
    l = l * exp(m - m_new) + sum(P, axis=1)
    m = m_new
    acc = P * V + acc
O = acc / l
```

## Inference-specific concerns

- **KV cache**: at decode step only one new Q token is computed, so `Q` is shape `(1, d)`.
- **Causal mask**: future tokens are masked; at decode time this is trivial.
- **Left padding / attention mask**: pass a mask tile or compute `S + mask` before softmax.
- **GQA**: K/V heads are shared by multiple Q heads; use `head_idx % kv_heads` for K/V.

## Verification

Reference: `torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True)`.

## Reference

- `cuda-blackwell-labs/projects/32_fused_kernels/`
- https://github.com/Dao-AILab/flash-attention

