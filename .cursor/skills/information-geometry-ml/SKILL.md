# Information Geometry for ML

## Description

Fisher information metric, natural gradient, alpha-connections, and geometry of probability distributions.

## When to use

You want to optimize or compare probability distributions in a geometrically meaningful way.

## Key concepts

- **Statistical manifold**: family of distributions parameterized by $	heta$.
- **Fisher information metric**: natural Riemannian metric on statistical manifolds.
- **Natural gradient**: $	ilde{
abla} = G^{-1}
abla$ where $G$ is Fisher information.
- **Alpha-connections**: Amari's dual connections; $lpha=\pm 1$ for e/m-flat manifolds.

## Code pattern

```python
import torch

# Natural gradient preconditioner (simplified)
F = compute_fisher_matrix(model, data)  # E[grad log p grad log p^T]
natural_grad = torch.linalg.solve(F + 1e-4*torch.eye(len(F)), grad)
```

## Tuning notes

- Fisher can be expensive; use Kronecker factored approximations (KFAC) or diagonal.
- Natural gradient is parameterization-invariant.
- Combine with trust-region methods for stability.

## Verification

1. Compare natural gradient vs Adam on a small logistic regression.
2. Compute Fisher information for a simple exponential family.
3. Show invariance under reparameterization of the natural gradient.

## References

- https://en.wikipedia.org/wiki/Information_Geometry
- https://www.jmlr.org/papers/volume21/17-678/17-678.pdf
- https://link.springer.com/article/10.1007/s41884-025-00187-y
- https://en.wikipedia.org/wiki/Fisher_information_metric
