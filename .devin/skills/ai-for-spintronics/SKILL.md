# AI for Spintronics

## Description

Use machine learning to discover magnetic materials, model skyrmions, and optimize spintronic devices such as MRAM.

## When to use

You are discovering spintronic materials, modeling magnetic textures such as skyrmions, or optimizing spin-orbit-torque MRAM devices.

## Usage

- Screen heavy-metal/ferromagnet stacks for high spin-orbit and spin-transfer torque efficiency.
- Predict stable skyrmion-host compounds and Dzyaloshinskii-Moriya interaction strength.
- Build surrogate models that map MRAM stack parameters to switching current, retention, and margins.
- Propose novel magnetic compounds with generative models for spintronic applications.

## Steps

1. Curate DFT, micromagnetic, and experimental data for candidate spintronic materials.
2. Train predictors for spin Hall conductivity, skyrmion stability, or MRAM switching.
3. Screen new materials or stack designs against fabrication and stability criteria.
4. Validate magnetic texture predictions with micromagnetic simulations.
5. Optimize an SOT-MRAM or skyrmion device and compare switching energy to a baseline.
6. Iterate with foundry constraints and experimental feedback.

## Code pattern

```python
from pymatgen.core import Composition
from sklearn.ensemble import GradientBoostingRegressor

# Train a surrogate for SOT efficiency from compositional descriptors
X = featurize_compositions(compositions)
model = GradientBoostingRegressor().fit(X, sot_efficiency)
```

## Tuning notes

- Include fabrication constraints and stability criteria (energy above hull) in screening.
- Use high-throughput DFT data as labels; augment with experimental measurements when available.
- Validate magnetic texture predictions with micromagnetic simulations (e.g., MuMax3).

## Verification

1. Train an ML model to predict spin Hall conductivity and rank candidate materials.
2. Predict stable skyrmion formation in a new compound and verify it with DFT/micromagnetic simulation.
3. Optimize an SOT-MRAM stack and compare switching energy to a baseline design.

## References

- https://doi.org/10.1038/s41524-025-01626-1
- https://www.nature.com/articles/s44306-024-00044-1
- https://pubs.rsc.org/en/content/articlelanding/2023/ce/d3ce00765k
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10019916/
