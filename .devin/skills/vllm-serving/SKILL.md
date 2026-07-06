---
name: vllm-serving
description: >-
  High-throughput LLM serving with vLLM and PagedAttention. Use when deploying
  LLMs for inference, building APIs, or optimizing serving throughput.
---

# vLLM Serving

## Overview
vLLM provides high-throughput LLM serving with PagedAttention for efficient KV cache management.

## Quick Start
```python
from vllm import LLM, SamplingParams
llm = LLM(model="meta-llama/Llama-3.1-8B-Instruct", tensor_parallel_size=1)
sampling = SamplingParams(temperature=0.7, max_tokens=512)
outputs = llm.generate(["Hello, world!"], sampling)
```

## Server Mode
```bash
python -m vllm.entrypoints.openai.api_server --model meta-llama/Llama-3.1-8B-Instruct --port 8000
```

## Key Features
- PagedAttention: O(1) KV cache allocation
- Continuous batching: dynamic request scheduling
- Tensor parallelism: --tensor-parallel-size N
- Quantization: --quantization awq, gptq, bitsandbytes
- LoRA adapters: --enable-lora

## Performance Tuning
- --gpu-memory-utilization 0.9 (default 0.9)
- --max-model-len 32768 (context window)
- --batch-size for offline inference
- --swap-space 4 (CPU swap in GB)

## Common Issues
- OOM: reduce gpu-memory-utilization or max-model-len
- Slow first request: model loading, use --load-format auto
- Wrong outputs: check chat template, use --chat-template
