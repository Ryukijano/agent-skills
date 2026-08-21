# AI for Cosmology

## Description

Emulate nonlinear structure formation and CMB observables to infer cosmological parameters 50x faster than full N-body simulations.

## When to use

You are analyzing cosmic microwave background maps, galaxy surveys, weak-lensing convergence, or 21-cm tomography.

## Usage

- Emulate matter power spectra and N-body simulations with Gaussian processes or neural nets.
- Compress weak-lensing, galaxy, and 21-cm maps into informative summary statistics.
- Run simulation-based inference for cosmological parameters.
- Accelerate expensive Boltzmann and radiative-transfer codes.

## Steps

1. Generate a training set of cosmological parameters and high-fidelity observables from simulations.
2. Train an emulator for the power spectrum, peak counts, or full-field maps.
3. Validate the emulator outside the training range and propagate uncertainties into posteriors.
4. Use the emulator in a neural posterior-estimation or MCMC pipeline.
5. Compare inferred parameter constraints against two-point-statistics baselines.

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
