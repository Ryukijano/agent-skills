# AI for Cosmology

## Description

ML for large-scale structure, weak lensing, CMB analysis, 21-cm cosmology, and cosmological parameter inference.

## When to use

You are analyzing cosmic microwave background maps, galaxy surveys, weak-lensing convergence, or 21-cm tomography.

## Key concepts

- **N-body surrogates**: fast approximations of dark-matter structure formation.
- **Summary statistics**: power spectra, bispectra, peak counts, and Minkowski functionals.
- **Simulation-based inference**: neural posterior estimation and likelihood-free methods.
- **Emulation and Gaussian processes**: replacing expensive Boltzmann and radiative-transfer codes.

## Code pattern

```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor

# Emulate a fast cosmological observable from parameters
params_train = np.load("cosmo_params_train.npy")
obs_train = np.load("power_spectrum_train.npy")
gp = GaussianProcessRegressor().fit(params_train, obs_train)
pred, sigma = gp.predict(params_test, return_std=True)
```

## Tuning notes

- Preserve physical symmetries (translation, rotation, scale) in architectures where relevant.
- Propagate uncertainties from emulators into posterior constraints.
- Validate emulators against high-fidelity simulations outside the training region.

## Verification

1. Emulate the matter power spectrum and compare to a Boltzmann code.
2. Train a weak-lensing map classifier or peak-count regressor.
3. Infer cosmological parameters with a neural posterior estimator.

## References

- https://doi.org/10.1088/1361-6633/acd2ea
- https://doi.org/10.3390/galaxies13050114
- https://arxiv.org/abs/2605.12877
- https://arxiv.org/abs/2605.10105
