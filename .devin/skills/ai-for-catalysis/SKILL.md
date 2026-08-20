# AI for Catalysis

## Description

Machine learning for catalyst discovery, reaction mechanism elucidation, activity and selectivity prediction, and catalytic process optimization.

## When to use

You are designing heterogeneous, homogeneous, or enzymatic catalysts and need to predict activity, selectivity, stability, or optimal reaction conditions from structure and data.

## Key concepts

- **Catalysis informatics**: structured datasets, reaction descriptors, and ML models for catalyst screening.
- **Adsorption-energy and scaling-relation models**: predict binding energies and use them as microkinetic inputs.
- **Reaction network exploration**: ML-guided discovery of elementary steps and kinetic rate laws.
- **Active learning and Bayesian optimization**: efficient experimental campaigns for catalyst synthesis and testing.
- **Single-atom, electrocatalyst, and photocatalyst design**: data-driven design for energy and sustainable chemistry.

## Code pattern

```python
import numpy as np
from sklearn.kernel_ridge import KernelRidge

# Surface and adsorbate descriptors -> adsorption energy
X = df[["d_band_center", "coordination", "adsorbate_fingerprint"]]
y = df["adsorption_energy_eV"]
model = KernelRidge(kernel="rbf").fit(X, y)
```

## Tuning notes

- Catalytic performance is highly sensitive to surface structure, support, and conditions; include adsorption-site and environmental features.
- Reaction data are often scattered across literature; harmonize units, substrates, and catalyst loadings.
- Pair ML models with microkinetic simulations to interpret predictions mechanistically.

## Verification

1. Predict adsorption or activation energies for a set of catalyst-adsorbate pairs and compare to DFT.
2. Optimize a catalyst composition or reaction condition using Bayesian optimization and validate experimentally.
3. Reproduce a microkinetic model from ML-predicted rate constants and compare to measured conversion/selectivity.

## References

- https://www.nature.com/articles/s41929-024-01150-3
- https://pubs.acs.org/doi/full/10.1021/acscatal.9b04186
- https://www.sciencedirect.com/science/article/pii/S2667325823003485
- https://www.nature.com/articles/s41929-022-00896-y
- https://pubs.rsc.org/en/content/articlelanding/2025/cc/d5cc05274b
