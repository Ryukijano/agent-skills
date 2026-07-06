---
name: deepspeed-training
description: >-
  Distributed training with DeepSpeed ZeRO optimization. Train models up to 1T
  parameters with limited GPU memory. Use when training large models across
  multiple GPUs.
---

# DeepSpeed Training

## Overview
DeepSpeed ZeRO (Zero Redundancy Optimizer) partitions optimizer state, gradients, and parameters across GPUs.

## ZeRO Stages
- **Stage 1**: Partition optimizer state (4x memory reduction)
- **Stage 2**: Partition optimizer + gradients (8x reduction)
- **Stage 3**: Partition optimizer + gradients + params (N_gpu x reduction)

## Config
```json
{
  "zero_optimization": {
    "stage": 2,
    "offload_optimizer": { "device": "cpu" },
    "allgather_partitions": true
  },
  "bf16": { "enabled": true },
  "train_batch_size": "auto",
  "train_micro_batch_size_per_gpu": "auto"
}
```

## HuggingFace Integration
```python
from transformers import TrainingArguments, Trainer
args = TrainingArguments(
    "output_dir", deepspeed="ds_config.json",
    per_device_train_batch_size=8,
    bf16=True,
)
trainer = Trainer(model, args, train_dataset=ds)
trainer.train()
```

## When to Use
- Model doesn't fit on single GPU → ZeRO Stage 2/3
- Want larger batch sizes → ZeRO Stage 1/2
- CPU offloading for extreme memory savings
- Pipeline parallelism for very large models

## Tips
- Stage 2 is usually the best performance/memory tradeoff
- Use bf16, not fp16 (no gradient scaler needed)
- Set `gradient_checkpointing=True` for more memory savings
- `--offload_optimizer` helps but slows training ~30%
