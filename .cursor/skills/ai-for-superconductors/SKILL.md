# AI for Superconductors

## Description

Apply ML to discover superconductors, predict critical temperature and electron-phonon coupling, and screen candidates through DFT-integrated pipelines.

## When to use

You are searching for new superconducting compounds or trying to predict $T_c$, critical fields, or electron-phonon coupling from crystal and electronic structure.

## Usage

- Predict $T_c$ and electron-phonon properties from crystal structure and DFT descriptors.
- Screen large databases for electron-phonon coupling, stability, and synthesizability.
- Use equivariant graph neural networks that respect crystal symmetries for superconducting properties.
- Combine generative models, ML potentials, and DFT in an AI-accelerated discovery pipeline.

## Steps

1. Curate the SuperCon database or DFT-derived electron-phonon data and compute composition/structure descriptors.
2. Train a classifier or regression model to predict $T_c$ and rank candidates for further study.
3. Screen databases with ML filters for structural stability, electron-phonon coupling, and synthesizability.
4. Apply equivariant GNNs to refine predictions using crystal-symmetry-aware representations.
5. Use generative models and ML potentials to propose novel candidates and relax them with DFT.
6. Validate the most promising candidates experimentally and report both MAE and true-positive rates.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# Crystal-structure and composition features -> Tc
X = np.array([df["n_electrons"], df["avg_mass"], df["density"]]).T
y = df["Tc_K"]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Superconductivity is a rare property; handle extreme class imbalance with appropriate sampling and metrics.
- Use DFT-validated electron-phonon spectral functions as high-fidelity training targets when available.
- Report both true-negative rate and mean absolute error; high precision on positive candidates is essential.

## Verification

1. Predict $T_c$ on a held-out test set and report MAE versus DFT or experimental values.
2. Screen a large database for likely superconductors and validate top candidates with DFT.
3. Synthesize and measure a predicted candidate to confirm superconductivity.

## References

- https://doi.org/10.1007/s10948-026-07175-y
- https://doi.org/10.1038/s43246-021-00209-z
- https://link.springer.com/article/10.1038/s41524-026-01964-8
- https://ieeexplore.ieee.org/document/11017078
- https://openreview.net/pdf/2214f145d116ef5e783cb2e9e3899ed4ab18cd00.pdf
