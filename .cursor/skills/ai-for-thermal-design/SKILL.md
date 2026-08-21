# AI for Thermal Design

## Description

Use machine learning to predict electronics cooling, control data-center thermal systems, and co-design heat sinks and packages.

## When to use

You are designing heat sinks, cold plates, 3D/2.5D packages, or data-center cooling and need fast thermal predictions for optimization.

## Usage

- Replace CFD simulations with neural networks and Fourier neural operator surrogates.
- Control data-center cooling with reinforcement learning and MPC.
- Predict junction temperature and hot spots from package and heat-sink geometry.
- Embed heat-equation constraints with physics-informed neural networks.

## Steps

1. Define the thermal scenario (package, heat sink, or data center) and collect CFD/FEM data.
2. Train a surrogate thermal model with high-fidelity training and validation splits.
3. Use the surrogate in an optimization loop for geometry or set points.
4. Enforce boundary conditions and conservation laws with PINNs or hybrid loss terms.
5. Validate predictions against CFD/FEM under unseen operating conditions.
6. Co-optimize with mechanical stress and reliability constraints.

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
