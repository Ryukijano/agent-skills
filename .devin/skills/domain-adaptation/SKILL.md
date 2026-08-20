# Domain Adaptation

## Description

Transfer knowledge from a labeled source domain to an unlabeled or partially labeled target domain.

## When to use

You have labeled data in one domain but need to deploy in a different but related domain.

## Key concepts

- **Covariate shift vs concept drift**: input or label distribution differences.
- **Feature alignment**: minimize distribution distance (MMD, adversarial).
- **Self-training / pseudo-labeling**: label target data with a source model.
- **Domain randomization**: train on diverse synthetic domains.

## Code pattern

```python
import torch
import torch.nn as nn

# Adversarial domain adaptation: gradient reversal on domain classifier
class GradientReversalFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, x, alpha):
        ctx.alpha = alpha
        return x.view_as(x)

    @staticmethod
    def backward(ctx, grad_output):
        return -ctx.alpha * grad_output, None
```

## Tuning notes

- Match feature extractors across domains before the classifier.
- Pseudo-label quality matters; use confident predictions and iterative refinement.
- Consider domain-specific batch normalization.

## Verification

1. Train a source model on MNIST and adapt to USPS or SVHN.
2. Compare target accuracy of source-only, fine-tuning, and adversarial adaptation.
3. Visualize source and target feature distributions before/after alignment.

## References

- https://arxiv.org/abs/2302.02627
- https://github.com/thuml/Xlearn
- https://arxiv.org/abs/1505.07818
- https://adapt.readthedocs.io/
