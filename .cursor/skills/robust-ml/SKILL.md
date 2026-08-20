# Robust Machine Learning

## Description

Adversarial robustness, distribution shift, out-of-distribution detection, and reliable model performance.

## When to use

Your model must perform reliably under adversarial attacks, distribution shift, or noisy inputs.

## Key concepts

- **Adversarial training**: augment training with adversarial examples.
- **Robust optimization**: minimize worst-case loss.
- **Out-of-distribution (OOD) detection**: identify inputs far from training data.
- **Certified defenses**: provable robustness bounds.

## Code pattern

```python
import torch
import torch.nn as nn
import torch.optim as optim

# Fast gradient sign method (FGSM) for adversarial training
x_adv = x + epsilon * torch.sign(x.grad)
```

## Tuning notes

- Adversarial training improves robustness at the cost of clean accuracy.
- OOD detection should be calibrated on a representative out-distribution.
- Certified methods are expensive; use for small or safety-critical models.

## Verification

1. Run a simple FGSM or PGD attack on a trained image classifier.
2. Evaluate accuracy on a distribution-shifted test set.
3. Implement an OOD detector and compute AUROC on in/out data.

## References

- https://arxiv.org/abs/2408.06132
- https://madrylab.mit.edu/
- https://github.com/MadryLab/robustness
- https://arxiv.org/abs/2106.03098
