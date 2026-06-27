---
name: debug-training
description: Debug ML training failures including loss=NaN, CUDA OOM, DDP hangs, poor convergence, and wrong output shapes. Use when training crashes, loss diverges, or results are unexpected.
---

## Debug Training Failures

### By symptom

**Loss=NaN**: Check gradient norms, add `eps` to denominators, clamp logits, reduce LR 10x, use `torch.nan_to_num` as diagnostic.

**CUDA OOM**: Reduce batch_size 2x, enable `torch.autocast(bfloat16)`, `gradient_checkpointing_enable()`, `torch.cuda.empty_cache()`.

**DDP hang**: `NCCL_P2P_DISABLE=1`, `NCCL_DEBUG=INFO`, check all ranks same batch size, add `torch.distributed.barrier()`.

**Poor convergence**: Check LR schedule, verify params are changing, visualize data samples, check labels.

**Wrong shapes**: Add `assert x.shape == expected` at every reshape, print shapes at each layer.

### Diagnostic tools
```python
torch.cuda.memory_summary()
print(f"grad_norm: {clip_grad_norm_(model.parameters(), float('inf'))}")
```
