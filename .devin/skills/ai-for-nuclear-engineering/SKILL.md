# AI for Nuclear Engineering and Fusion

## Description

Apply machine learning to build fast surrogates, predict plasma disruptions, model material degradation, and optimize control in nuclear and fusion systems.

## When to use

You are modeling nuclear systems, plasma behavior, or fusion experiments.

## Usage

- Train fast surrogate models to replace expensive neutronics or MHD simulations for design and optimization.
- Predict and avoid plasma disruptions in tokamaks from multi-diagnostic time-series data.
- Model thermal, radiation, and fatigue degradation of reactor and plasma-facing materials.
- Optimize plasma shape, scenario, and control trajectories with reinforcement learning or model predictive control.

## Steps

1. Assemble high-fidelity simulation or experimental data for the target nuclear/fusion problem (e.g., DIII-D, ITER scenarios).
2. Train a physics-informed or data-driven surrogate for neutronics, MHD, or thermomechanical response.
3. Build a disruption-prediction classifier using plasma diagnostics and validate warning time on historical disruptions.
4. Integrate degradation models for plasma-facing or structural materials and propagate uncertainty into lifetime forecasts.
5. Use reinforcement learning or Bayesian optimization to tune control policies and plasma scenarios.
6. Validate all ML predictions against physics simulators and experimental measurements, then embed approved models in control loops.

## Code pattern

```python
import jax
import jax.numpy as jnp

# Neural state-space model for plasma dynamics
from jax import random
params = model.init(random.PRNGKey(0), x, u)
predictions = model.apply(params, x, u)
```

## Tuning notes

- Safety-critical: validate predictions with physical simulators and experiments.
- Data is scarce; leverage physics-informed and multi-fidelity methods.
- UQ is essential for high-consequence decisions.

## Verification

1. Build a surrogate for a simple reactor physics model and compare to a high-fidelity run.
2. Train a disruption predictor on a public tokamak dataset.
3. Propagate uncertainty and compute safety margins.

## References

- https://www.nature.com/articles/s41467-025-63917-x
- https://iopscience.iop.org/article/10.1088/1741-4326/ade8fd
- https://doi.org/10.1126/science.adm8201
- https://fusion.gat.com/
