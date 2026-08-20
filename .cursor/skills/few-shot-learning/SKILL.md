# Few-Shot Learning

## Description

Learning from a handful of labeled examples through meta-learning, prompt tuning, and data augmentation.

## When to use

You have only a few labeled examples per class and need strong generalization.

## Key concepts

- **k-shot, N-way**: few examples and many classes.
- **Prototypical / matching networks**: compare embeddings to class prototypes.
- **In-context learning**: prompt LLMs with examples.
- **Augmentation and self-supervised pretraining**: generate more signal from few labels.

## Code pattern

```python
import torch
import torch.nn.functional as F

# Prototypical network: compute class prototypes and classify by distance
prototypes = torch.stack([support[labels == c].mean(0) for c in classes])
logits = -torch.cdist(query, prototypes)
```

## Tuning notes

- Pretrain on a related large dataset before few-shot adaptation.
- Metric scaling and temperature affect performance.
- Use data augmentation and prompt engineering when labels are scarce.

## Verification

1. Train a prototypical network on Omniglot or miniImageNet.
2. Evaluate 5-way 1-shot and 5-way 5-shot accuracy.
3. Compare with a fine-tuned baseline using the same shots.

## References

- https://arxiv.org/abs/2402.03017
- https://github.com/orobix/Prototypical-Networks-for-Few-shot-Learning-PyTorch
- https://arxiv.org/abs/1703.05175
- https://huggingface.co/docs/transformers/tasks/prompting
