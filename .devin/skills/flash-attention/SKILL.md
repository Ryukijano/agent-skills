---
name: flash-attention
description: >-
  2-4x faster attention with Flash Attention. Use when optimizing transformer
  training speed or reducing GPU memory for long sequences.
---

# Flash Attention

## Overview
Flash Attention computes exact attention with O(N) memory instead of O(N^2), 2-4x faster.

## Installation
```bash
pip install flash-attn --no-build-isolation
```

## Usage in PyTorch
```python
from flash_attn import flash_attn_func
# q, k, v: (batch, seqlen, nheads, headdim)
out = flash_attn_func(q, k, v, causal=True)
```

## Usage in HuggingFace
```python
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-8B",
    torch_dtype=torch.bfloat16,
    attn_implementation="flash_attention_2",
)
```

## Benefits
- 2-4x faster training for seq_len > 2K
- O(N) memory vs O(N^2) for standard attention
- Supports causal and bidirectional attention
- Works with bfloat16 and fp16

## Requirements
- CUDA 11.6+, Ampere GPU (A100, H100, L40S) or newer
- PyTorch 2.0+
- Linux only

## Alternatives
- PyTorch SDPA: torch.nn.functional.scaled_dot_product_attention (built-in, slower)
- xFormers: memory_efficient_attention (similar performance)
