# High-Dimensional Statistics for ML

## Description

Sparsity, LASSO, compressed sensing, concentration inequalities, and covariance estimation.

## When to use

You have many features relative to samples and need structured estimation.

## Key concepts

- **LASSO**: $\ell_1$-regularized regression for sparse coefficients.
- **Compressed sensing**: recover sparse signals from few measurements.
- **Concentration inequalities**: Hoeffding, Bernstein, matrix concentration.
- **Sparse covariance/precision**: graphical LASSO, inverse covariance estimation.

## Code pattern

```python
from sklearn.linear_model import Lasso
from sklearn.covariance import GraphicalLasso

lasso = Lasso(alpha=0.1).fit(X, y)
glasso = GraphicalLasso(alpha=0.1).fit(X)
```

## Tuning notes

- Cross-validate regularization strength.
- Check irrepresentable conditions for LASSO support recovery.
- Use knockoffs or stability selection for variable selection.

## Verification

1. Recover a sparse vector with LASSO and compare support.
2. Generate compressed sensing measurements and reconstruct a sparse signal.
3. Estimate a sparse inverse covariance and compare to true graph.

## References

- https://www.cs.cmu.edu/~pradeepr/paperz/LogDet.pdf
- https://statistics.berkeley.edu/sites/default/files/tech-reports/709.pdf
- https://www.jmlr.org/papers/volume11/yuan10b/yuan10b.pdf
- https://www.stat.berkeley.edu/~bickel/Rothman%20et%20al%202007-spice.pdf
