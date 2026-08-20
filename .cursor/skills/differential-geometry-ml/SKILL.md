# Differential Geometry for ML

## Description

Riemannian manifolds, geodesics, natural gradients, hyperbolic ML, and optimization on curved spaces.

## When to use

You are working with data or parameters that naturally live on curved spaces (spheres, manifolds, hierarchical graphs).

## Key concepts

- **Riemannian manifolds**: curved spaces with a metric.
- **Geodesics**: shortest paths on manifolds.
- **Natural gradient**: steepest descent with respect to Fisher metric.
- **Hyperbolic ML**: embed hierarchical data in hyperbolic space (Poincaré/Lorentz).
- **Stiefel/Grassmann**: optimization with orthogonality constraints.

## Code pattern

```python
import geoopt

# Hyperbolic manifold
manifold = geoopt.PoincareBall()
point = manifold.random(2, 3)
```

## Tuning notes

- Use manifold-aware optimizers (e.g., geoopt.RiemannianAdam).
- Hyperbolic space works well for tree-like/hierarchical data.
- Watch for numerical instabilities near the boundary of Poincaré ball.

## Verification

1. Embed a tree in Euclidean and hyperbolic space; compare distortion.
2. Train a classifier with hyperbolic embeddings.
3. Verify a Riemannian optimizer preserves constraints (e.g., orthogonality).

## References

- https://geoopt.readthedocs.io/
- https://arxiv.org/pdf/2207.07287
- https://optml.mit.edu/papers/sra_hosseini_chapter.pdf
- https://arxiv.org/html/2604.02969
