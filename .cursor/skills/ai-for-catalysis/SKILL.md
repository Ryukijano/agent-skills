# AI for Catalysis

## Description

Use catalysis informatics and active learning to discover catalysts, predict activity/selectivity, explore reaction networks, and optimize processes.

## When to use

You are designing heterogeneous, homogeneous, or enzymatic catalysts and need to predict activity, selectivity, stability, or optimal reaction conditions from structure and data.

## Usage

- Screen catalysts with structured datasets, reaction descriptors, and ML models.
- Predict adsorption energies and scaling relations as inputs to microkinetic simulations.
- Explore reaction networks and elementary steps with ML-guided search.
- Optimize catalyst synthesis and reaction conditions with active learning and Bayesian optimization.

## Steps

1. Curate catalyst-adsorbate datasets, harmonizing units, structures, and reaction conditions.
2. Compute or collect adsorption-energy, surface, and adsorbate descriptors for the target reaction.
3. Train ML models to predict activity, selectivity, or binding energy and validate against DFT.
4. Build microkinetic models using ML-predicted rate constants and compare to measured conversion/selectivity.
5. Use active learning or Bayesian optimization to choose the next catalyst composition or reaction condition.
6. Synthesize and test the selected catalysts, then feed results back to refine the models.

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
