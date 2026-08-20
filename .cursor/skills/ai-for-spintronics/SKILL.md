# AI for Spintronics

## Description

ML for magnetic material discovery, skyrmion and MRAM device modeling, spin-orbit torque optimization, and spin-wave logic.

## When to use

You are discovering spintronic materials, modeling magnetic textures such as skyrmions, or optimizing spin-orbit-torque MRAM devices.

## Key concepts

- **Spin-orbit torque (SOT) and spin-transfer torque (STT)**: ML screens heavy-metal/ferromagnet stacks for high charge-to-spin conversion.
- **Skyrmion materials**: classifiers predict stable skyrmion-host compounds and Dzyaloshinskii-Moriya interaction strength.
- **MRAM device modeling**: surrogate models map stack parameters to switching current, retention, and read/write margins.
- **Generative materials design**: GANs and diffusion models propose novel magnetic compounds for spintronic applications.

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
