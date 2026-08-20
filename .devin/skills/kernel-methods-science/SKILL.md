# Kernel Methods and RKHS for Scientific ML

## Description

RKHS, Gaussian processes, MMD, kernel mean embeddings, and kernel methods for PDEs.

## When to use

You want nonlinear methods with strong theoretical guarantees, or kernel-based inference on distributions.

## Key concepts

- **RKHS**: reproducing kernel Hilbert space.
- **Kernel trick**: replace dot products with kernel evaluations.
- **Gaussian processes**: Bayesian kernel regression.
- **MMD**: maximum mean discrepancy for two-sample testing and generative modeling.
- **Kernel mean embedding**: represent distributions in RKHS.

## Code pattern

```python
import gpytorch
import torch

class GP(gpytorch.models.ExactGPModel):
    pass

likelihood = gpytorch.likelihoods.GaussianLikelihood()
model = GP(train_x, train_y, likelihood).cuda()
```

## Tuning notes

- Choose kernel to match prior assumptions (RBF, Matérn, polynomial).
- Kernel hyperparameters can be learned by maximizing marginal likelihood.
- MMD is sensitive to kernel choice; use mixture or learned kernels.

## Verification

1. Train a GP regression and check negative log-likelihood.
2. Run an MMD two-sample test on two distributions.
3. Use kernel mean embedding to estimate a distribution property.

## References

- https://docs.gpytorch.ai/
- https://doi.org/10.1561/2200000060
- https://projecteuclid.org/journals/annals-of-statistics/volume-36/issue-3/Kernel-methods-in-machine-learning/10.1214/009053607000000677.pdf
- https://jmlr.csail.mit.edu/papers/v19/16-291.html
