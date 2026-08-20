# AI for Thermal Design

## Description

ML surrogates for electronics cooling, data-center thermal control, heat-sink and package thermal co-design, and CFD emulation.

## When to use

You are designing heat sinks, cold plates, 3D/2.5D packages, or data-center cooling and need fast thermal predictions for optimization.

## Key concepts

- **Surrogate thermal modeling**: neural networks and Fourier neural operators replace expensive CFD simulations.
- **Data-center cooling control**: reinforcement learning and MPC optimize fan speed, set points, and workload placement.
- **Package and heat-sink design**: ML predicts junction temperature, hot spots, and thermal resistance from geometry.
- **Physics-informed neural networks (PINNs)**: embed heat-equation constraints for reliable extrapolation.

## Code pattern

```python
import torch
import torch.nn as nn

# Simple surrogate mapping package geometry to maximum temperature
model = nn.Sequential(nn.Linear(64, 128), nn.ReLU(), nn.Linear(128, 1))
T_max = model(geometry_features)
```

## Tuning notes

- Use high-fidelity CFD/FEM data for training and validate on unseen operating conditions.
- Enforce boundary conditions and conservation laws with PINNs or hybrid loss terms.
- Co-optimize with mechanical stress and reliability constraints for 3D packages.

## Verification

1. Train a surrogate to predict a heat-sink or cold-plate temperature field and compare to CFD with less than 5% error.
2. Run an RL cooling controller in a data-center simulator and show energy reduction.
3. Optimize a chip-package thermal design and verify junction temperature with FEM.

## References

- https://doi.org/10.1063/5.0206287
- https://doi.org/10.1145/3708890
- https://doi.org/10.1109/eptc62800.2024.10909871
- https://arxiv.org/abs/2103.11177
