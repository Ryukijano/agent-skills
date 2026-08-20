# Spectral Methods and Graph Theory for ML

## Description

Graph Laplacian, spectral clustering, spectral GNNs, graph partitioning, and spectral sparsification.

## When to use

You are analyzing graphs or networks and want to use spectral tools.

## Key concepts

- **Graph Laplacian**: $L = D - A$ and normalized variants.
- **Spectral clustering**: use eigenvectors of Laplacian for clustering.
- **Spectral GNNs**: filters in graph frequency domain.
- **Graph partitioning**: ratio cut, normalized cut, Cheeger cut.

## Code pattern

```python
import scipy.sparse as sp
import scipy.sparse.linalg as sla

L = sp.csgraph.laplacian(adj, normed=True)
eigvals, eigvecs = sla.eigsh(L, k=10, which='SM')
```

## Tuning notes

- Normalized Laplacian often better for irregular graphs.
- Spectral clustering works well when clusters are well-separated.
- Spectral GNNs are less common than spatial GNNs but have theoretical appeal.

## Verification

1. Compute Laplacian eigenvectors and use for spectral clustering.
2. Compare spectral clustering to k-means on a graph dataset.
3. Implement a simple spectral graph filter and verify signal smoothing.

## References

- https://www.cs.yale.edu/homes/spielman/sagt/sagt.pdf
- https://arxiv.org/pdf/1608.04845
- https://proceedings.mlr.press/v162/wang22am.html
- https://link.springer.com/article/10.1007/s44163-024-00102-x
