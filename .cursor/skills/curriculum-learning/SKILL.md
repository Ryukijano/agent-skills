# Curriculum Learning

## Description

Order training examples from easy to hard to improve convergence and generalization.

## When to use

You want to speed up training or improve generalization by presenting examples in a meaningful order.

## Key concepts

- **Difficulty score**: loss, length, noise, or expert-defined difficulty.
- **Pacing functions**: control how fast the curriculum mixes hard examples.
- **Self-paced learning**: the curriculum is derived from the model's own loss.
- **Transfer curricula**: reuse difficulty metrics from a related task.

## Code pattern

```python
def curriculum_sampler(epoch, dataset, difficulties):
    # Increase the threshold for including harder examples over time
    threshold = min(1.0, epoch / 10)
    indices = [i for i, d in enumerate(difficulties) if d <= threshold]
    return torch.utils.data.Subset(dataset, indices)
```

## Tuning notes

- Define difficulty carefully; a bad curriculum can hurt.
- Combine with standard shuffling to avoid overfitting to easy data.
- Monitor whether hard examples improve final metrics, not just speed.

## Verification

1. Train a model with and without a curriculum on the same data.
2. Define a difficulty measure and plot its correlation with loss.
3. Compare final test accuracy and convergence time.

## References

- https://arxiv.org/abs/2004.11101
- https://huggingface.co/docs/transformers/training
- https://github.com/terryum/curriculum_learning
- https://arxiv.org/abs/1806.06044
