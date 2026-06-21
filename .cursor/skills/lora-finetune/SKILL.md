---
name: lora-finetune
description: LoRA (Low-Rank Adaptation) fine-tuning for vision transformers including DINOv2, ViT, and similar architectures. Use when adapting frozen pretrained models to new domains, configuring LoRA rank/alpha, or debugging LoRA training instability.
---

## LoRA Fine-Tuning for Vision Transformers

### Overview

LoRA injects low-rank trainable matrices into frozen pretrained weights:
```
W' = W + α/r * B @ A
```
where `W` is frozen, `A` (r×d) and `B` (d×r) are trainable, `r` is rank, `α` is scaling.

### Recommended hyperparameters

| Parameter | Conservative | Standard | Aggressive |
|-----------|-------------|----------|------------|
| rank (r) | 4 | 8 | 16 |
| alpha (α) | 8 | 16 | 32 |
| dropout | 0.1 | 0.05 | 0.0 |
| target_modules | qkv, proj | qkv, proj, fc1, fc2 | all linear |
| start_block | 6 (last 6) | 3 (last 9) | 0 (all) |
| LoRA LR | 1e-4 | 1e-3 | 5e-3 |
| Base LR | 1e-4 | 2e-4 | 5e-4 |

### Critical configuration tips

1. **Preserve low-level features**: Freeze blocks 0-2 by setting `start_block=3`
2. **Scale alpha with rank**: Use `alpha = 2 * rank` as a rule of thumb
3. **Separate LR groups**: LoRA matrices need higher LR than base (which is frozen anyway)
4. **Gradient clipping**: Always use `max_norm=1.0` — LoRA gradients can be unstable
5. **Warmup**: Use 5-10% of total steps for linear warmup

### DINOv2 LoRA injection

```python
from lora import inject_lora_into_dinov2, get_lora_params

# Load pretrained DINOv2
encoder = torch.hub.load('facebookresearch/dinov2', 'dinov2_vitb14')

# Inject LoRA
inject_lora_into_dinov2(
    encoder,
    r=8,
    alpha=16,
    dropout=0.05,
    target_modules=['qkv', 'proj', 'fc1', 'fc2'],
    start_block=3,
    end_block=None,  # None = until last block
)

# Get LoRA params for optimizer
lora_params = get_lora_params(encoder)
optimizer = torch.optim.AdamW(lora_params, lr=1e-4)
```

### Debugging LoRA training

1. **Loss not decreasing**: Check that LoRA params are actually trainable with `requires_grad=True`
2. **Gradient explosion**: Reduce LoRA LR by 10x, increase gradient clipping
3. **No adaptation**: Increase rank or add more target modules
4. **Forgetting pretrained features**: Reduce rank, increase alpha, or freeze more blocks
5. **Memory still high**: LoRA should use ~same memory as frozen; check for accidental unfreezing

### Progressive unfreezing (ExPLoRA-style)

```python
# Schedule: progressively unfreeze encoder blocks during training
unfreeze_schedule = [
    {'epoch': 0,  'num_blocks': 0},   # fully frozen
    {'epoch': 5,  'num_blocks': 2},   # last 2 blocks
    {'epoch': 10, 'num_blocks': 4},   # last 4 blocks
    {'epoch': 15, 'num_blocks': 12},  # all blocks
]
```

### L2-SP regularization

Anchor fine-tuned weights to pretrained values to prevent catastrophic forgetting:
```python
def l2sp_loss(model, pretrained_sd):
    loss = 0
    for name, param in model.encoder.state_dict().items():
        if name in pretrained_sd:
            loss += ((param - pretrained_sd[name]) ** 2).sum()
    return loss

# Add to total loss: loss += l2sp_weight * l2sp_loss(model, pretrained_sd)
```
