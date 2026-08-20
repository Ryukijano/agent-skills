# Topological Data Analysis (TDA) for ML

## Description

Persistent homology, Ripser, GUDHI, Mapper, and topological deep learning for shape-aware scientific ML.

## When to use

You want to extract robust, shape-driven features from complex, high-dimensional, or noisy scientific data.

## Key concepts

- **Persistent homology**: track birth/death of connected components, loops, voids across scales.
- **Persistence diagrams/barcodes**: compact topological descriptors.
- **Ripser/GUDHI**: fast C++ persistent homology libraries.
- **Mapper**: simplicial complex summarizing data shape.
- **Topological deep learning**: integrate persistence diagrams into neural networks.

## Code pattern

```python
import ripser
import gudhi

# Compute persistent homology with Ripser
diagrams = ripser.ripser(data, maxdim=2)['dgms']
```

## Tuning notes

- Choose distance metric carefully (Euclidean, Wasserstein, bottleneck).
- Subsample large datasets for Ripser.
- Vectorize persistence diagrams (e.g., persistence images, Betti curves) for ML.

## Verification

1. Compute persistence diagrams for a torus and a sphere and show they differ.
2. Use persistence images as features in a classifier.
3. Compare Mapper output to UMAP for a small dataset.

## References

- https://ripser.scikit-tda.org/
- https://gudhi.inria.fr/
- https://www.jmlr.org/papers/volume22/20-325/20-325.pdf
- https://github.com/scikit-tda
