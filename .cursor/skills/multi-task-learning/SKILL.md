# Multi-Task Learning

## Description

Shared representations, hard and soft parameter sharing, MTL architectures (MMoE, PLE, MTAN), and gradient balancing.

## When to use

You have several related prediction or control tasks and want a single model that shares computation, improves generalization, or reduces inference cost.

## Key concepts

- **Hard vs. soft parameter sharing**: shared trunk with task-specific heads, or cross-stitch/MMoE-style gates.
- **Multi-gate mixture of experts (MMoE) and PLE**: route examples through task-specific or shared experts.
- **Attention-based sharing (MTAN)**: learn task-specific attention masks over a shared network.
- **Gradient balancing**: GradNorm, uncertainty weighting, PCGrad, CAGrad, IMTL reduce negative transfer.
- **Negative transfer**: sharing can hurt some tasks; diagnose with per-task gradients.

## Code pattern

```python
import torch
import torch.nn as nn

class MultiTaskNet(nn.Module):
    def __init__(self, input_dim, task_dims):
        super().__init__()
        self.shared = nn.Sequential(nn.Linear(input_dim, 256), nn.ReLU())
        self.heads = nn.ModuleList([nn.Linear(256, d) for d in task_dims])

    def forward(self, x):
        h = self.shared(x)
        return [head(h) for head in self.heads]
```

## Tuning notes

- Group tasks with related inputs and labels; unrelated tasks cause negative transfer.
- Start with equal task weights and switch to GradNorm or PCGrad if one task dominates.
- Match head capacities to task difficulty; some tasks need deeper task-specific layers.
- Use LibMTL for fair benchmarking of architectures and weighting strategies.

## Verification

1. Train single-task baselines and compare per-task metrics to the multi-task model.
2. Measure gradient conflict via cosine similarity of task gradients.
3. Ablate sharing depth and task-weighting strategy on a fixed suite of tasks.

## References

- https://arxiv.org/abs/2404.18961
- https://github.com/median-research-group/LibMTL
- https://libmtl.readthedocs.io/en/latest/
- https://arxiv.org/abs/1801.06704
- https://www.jmlr.org/papers/v24/22-0347.html
