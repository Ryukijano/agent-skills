# Optimal Transport for ML

## Description

Wasserstein distance, Sinkhorn algorithm, sliced Wasserstein, and applications to generative modeling and domain adaptation.

## When to use

You need to compare or align probability distributions with geometry-aware metrics.

## Key concepts

- **Monge-Kantorovich**: optimal transport problem.
- **Wasserstein distance**: metric with cost grounded in sample space.
- **Entropic regularization**: Sinkhorn algorithm for fast approximate OT.
- **Sliced Wasserstein**: 1D projections for computational tractability.
- **Applications**: WGAN, domain adaptation, Bayesian inference.

## Code pattern

```python
import ot

# Wasserstein distance with Sinkhorn
M = ot.dist(x, y)
W = ot.sinkhorn2(a, b, M, reg=0.1)
```

## Tuning notes

- Sinkhorn regularization trades accuracy for speed; too small = slow, too large = blur.
- Sliced Wasserstein is cheaper but has different geometry.
- Use cost function matched to data (e.g., Euclidean for images).

## Verification

1. Compute Wasserstein distance between two 1D distributions and compare to closed form.
2. Train a WGAN or domain adaptation model with OT loss.
3. Compare Sinkhorn convergence for different regularization values.

## References

- https://pythonot.github.io/
- http://cermics.enpc.fr/~jourdain/OT/polyOT.pdf
- https://math.columbia.edu/~mnutz/docs/EOT_lecture_notes.pdf
- https://arxiv.org/pdf/2311.05134
