# AI for Superconductors

## Description

Machine learning for superconductor discovery, critical temperature prediction, electron-phonon modeling, and materials screening.

## When to use

You are searching for new superconducting compounds or trying to predict $T_c$, critical fields, or electron-phonon coupling from crystal and electronic structure.

## Key concepts

- **Critical temperature prediction**: supervised models trained on the SuperCon database and DFT descriptors.
- **High-throughput screening**: ML filters for electron-phonon coupling, structural stability, and thermodynamic synthesizability.
- **Equivariant graph neural networks**: structure-aware models that respect crystal symmetries for superconducting properties.
- **AI-accelerated discovery pipelines**: combine generative models, interatomic potentials, and DFT to propose and validate candidates.
- **Unconventional and topological superconductivity**: data-driven searches for non-phonon pairing mechanisms and quantum materials.

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
