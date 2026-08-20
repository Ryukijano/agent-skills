# AI for Nuclear Engineering and Fusion

## Description

Machine learning for reactor design, plasma control, material degradation, and fusion ignition prediction.

## When to use

You are modeling nuclear systems, plasma behavior, or fusion experiments.

## Key concepts

- **Surrogate models for expensive simulations**: replace neutronics or MHD solvers.
- **Disruption prediction**: forecast and avoid plasma disruptions in tokamaks.
- **Material degradation**: thermal stress, radiation damage, fatigue.
- **Reinforcement learning for control**: shape and trajectory optimization.

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
- https://www.osti.gov/biblio/2589559
- https://fusion.gat.com/
