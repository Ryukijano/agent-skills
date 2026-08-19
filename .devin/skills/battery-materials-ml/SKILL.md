# Battery Materials and Energy Storage ML

## Description

GNNs, Gaussian processes, and high-throughput screening for battery materials, redox flow batteries, and carbon capture solvents.

## When to use

You are using ML to discover or optimize battery materials, electrolytes, or energy storage systems.

## Key concepts

- **GNNs for materials**: predict redox potentials, ionic conductivity, stability.
- **Gaussian process regression**: small-data screening with uncertainty.
- **High-throughput DFT**: train on computed properties, screen millions of candidates.
- **Carbon capture solvents**: ML for CO2 binding energy, viscosity, degradation.
- **Datasets**: Materials Project, OQMD, PubChem, battery-specific datasets.

## Code pattern

```python
from dgl import DGLGraph
import torch

# GNN predicting a battery property
model = GNN(in_feats=10, hidden_feats=64, n_tasks=1)
model = model.to('cuda')
```

## Tuning notes

- Use crystal graph convolutions (CGCNN, MEGNet, ALIGNN) for periodic structures.
- Transfer learning from Materials Project to battery datasets.
- Use uncertainty to guide expensive experiments.

## Verification

1. Train a GNN on a battery property and compare MAE to a random forest baseline.
2. Screen 10k candidates and verify top candidates with DFT/experiment.
3. Check model uncertainty correlates with prediction error.

## References

- https://pubs.acs.org/doi/full/10.1021/jacsau.5c00526
- https://www.frontiersin.org/journals/environmental-science/articles/10.3389/fenvs.2023.1204690/full
- https://materialsproject.org/
