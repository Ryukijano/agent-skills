# Random Matrix Theory for ML

## Description

Marchenko-Pastur, semicircle law, free probability, and spectral analysis of neural networks.

## When to use

You are analyzing the spectrum of large matrices (covariance, kernels, Hessians, NTKs) in ML.

## Key concepts

- **Marchenko-Pastur law**: limiting eigenvalue distribution of sample covariance matrices.
- **Semicircle law**: Wigner matrices.
- **Free probability**: non-commutative probability for large random matrices.
- **NTK spectrum**: random matrix approach to neural tangent kernel.

## Code pattern

```python
import numpy as np

# Sample covariance eigenvalues
X = np.random.randn(n, p) / np.sqrt(n)
S = X.T @ X
lam = np.linalg.eigvalsh(S)
```

## Tuning notes

- Compare empirical spectrum to theoretical predictions.
- Use Tracy-Widom laws for edge eigenvalues.
- Free probability helps analyze products/sums of random matrices.

## Verification

1. Generate a sample covariance matrix and compare histogram of eigenvalues to Marchenko-Pastur.
2. Compute NTK spectrum at init for a shallow network.
3. Use free probability to approximate eigenvalues of A+B.

## References

- https://doi.org/10.48550/arxiv.2109.09304
- https://proceedings.neurips.cc/paper/2020/file/572201a4497b0b9f02d4f279b09ec30d-Paper.pdf
- https://projecteuclid.org/journals/annals-of-applied-probability/volume-28/issue-2/A-random-matrix-approach-to-neural-networks/10.1214/17-AAP1328.full
- https://arxiv.org/abs/2001.06188
