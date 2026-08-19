---
name: cutile-fmha-attention-gb10
description: >-
  Implement fused multi-head attention (FMHA) with cuTile Python on GB10. Covers online softmax, causal masking, grouped-query attention (GQA) tiles, and FlashAttention-style tiling for inference.
---

# cuTile FMHA Attention on GB10 DGX Spark

## Overview

cuTile can express the full FlashAttention/FMHA kernel in Python: load Q/K/V tiles, compute `QK^T`, apply online softmax with running `m` and `l` statistics, and accumulate the weighted sum.

## Core algorithm

For each Q tile of shape `(TILE_M, TILE_D)`:

```python
m_i = ct.full((TILE_M, 1), -math.inf, dtype=ct.float32)
l_i = ct.full((TILE_M, 1), 0.0, dtype=ct.float32)
acc = ct.full((TILE_M, TILE_D), 0.0, dtype=ct.float32)

q = ct.load(Q, (batch_idx, head_idx, bid_x, 0), (1, 1, TILE_M, TILE_D))
q = q.reshape((TILE_M, TILE_D))

for j in range(num_k_tiles):
    k = ct.load(K, (batch_idx, head_idx, j, 0), (1, 1, TILE_N, TILE_D))
    k_t = ct.permute(k.reshape((TILE_N, TILE_D)), (1, 0))
    s = ct.mma(q, k_t, ct.zeros((TILE_M, TILE_N)))
    s = s * qk_scale
    if CAUSAL:
        # mask out future positions
        ...
    m_new = ct.max(ct.stack([m_i, ct.max(s, axis=1, keepdims=True)]), axis=0)
    p = ct.exp(s - m_new)  # online softmax rescaling
    l_i = l_i * ct.exp(m_i - m_new) + ct.sum(p, axis=1, keepdims=True)
    m_i = m_new
    v = ct.load(V, (batch_idx, head_idx, j, 0), (1, 1, TILE_N, TILE_D))
    acc = ct.mma(p, v.reshape((TILE_N, TILE_D)), acc)

ct.store(Out, (batch_idx, head_idx, bid_x, 0),
         (acc / l_i).reshape((1, 1, TILE_M, TILE_D)))
```

## Tuning notes

- `TILE_M = TILE_N = 64` and `TILE_D = 64` or `128` are good starts.
- Use `ct.exp2` (`x * INV_LOG_2`) instead of `ct.exp` where supported.
- Causal attention stops the inner loop at `min((bid_x+1)*TILE_M, k_seqlen) / TILE_N`.
- Grouped-query attention (GQA) divides `bid_y` by `H` to get `head_idx` and `off_kv_h`.

## Verification

Compare against a reference PyTorch implementation:

```python
ref = torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=causal)
```

## Reference

- `cuda-blackwell-labs/projects/32_fused_kernels/`
- https://developer.nvidia.com/blog/tuning-flash-attention-for-peak-performance-in-nvidia-cuda-tile/
- https://github.com/NVIDIA/cutile-python/blob/main/samples/AttentionFMHA.py

