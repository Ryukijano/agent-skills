# Knowledge Distillation

## Overview
Transfer knowledge from a large teacher model to a smaller student model.

## Standard Distillation
```python
import torch.nn.functional as F

def distill_loss(student_logits, teacher_logits, labels, T=2.0, alpha=0.5):
    kd_loss = F.kl_div(
        F.log_softmax(student_logits / T, dim=-1),
        F.softmax(teacher_logits / T, dim=-1),
        reduction="batchmean",
    ) * (T * T)
    ce_loss = F.cross_entropy(student_logits, labels)
    return alpha * kd_loss + (1 - alpha) * ce_loss
```

## Approaches
- **Logit distillation**: Soft targets from teacher (classic)
- **Feature distillation**: Match intermediate representations
- **MiniLLM**: Reverse KL divergence for better generation
- **On-policy distillation**: Student generates, teacher scores

## Best Practices
- Temperature T=2-8 (higher = softer distributions)
- alpha=0.5 balances KD and CE losses
- Use teacher's top-k predictions, not full vocab
- Distill from multiple teachers for ensemble effect
- Student architecture: fewer layers, same hidden dim

## Results
- 70B → 7B with <2% accuracy loss (typical)
- 5-10x inference speedup
- 10x memory reduction
- Student can exceed teacher on specific tasks
