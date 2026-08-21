# AI for Photonics

## Description

Use deep learning to inverse-design photonic devices, metasurfaces, and optical communication links while replacing expensive Maxwell solvers.

## When to use

You are designing photonic devices, metasurfaces, waveguides, or optimizing optical communication links.

## Usage

- Inverse-design metasurfaces, metalenses, and waveguides for target phase or spectral responses.
- Train neural surrogates to replace FDTD or finite-element simulations.
- Optimize optical-communication modulators, demultiplexers, and equalizers.
- Enforce fabrication constraints and minimum feature sizes during design.

## Steps

1. Define the target optical response and a parameterization of the geometry.
2. Build a forward surrogate by training on FDTD/FEM simulations or experimental data.
3. Validate the surrogate against full-wave solvers on held-out designs.
4. Run inverse design or topology optimization with fabrication constraints.
5. Fabricate and characterize the device, then feed results back to refine the surrogate.

## Code pattern

```python
import torch
import torch.nn as nn

# Surrogate mapping geometry parameters to transmission spectrum
class PhotonicSurrogate(nn.Module):
    def __init__(self, in_dim=10, out_dim=100):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 128), nn.ReLU(), nn.Linear(128, out_dim)
        )

    def forward(self, x):
        return self.net(x)
```

## Tuning notes

- Enforce fabrication and minimum-feature constraints.
- Use active learning when full-wave simulations are expensive.
- Validate surrogate predictions against FDTD or finite-element solvers.

## Verification

1. Train a surrogate for a waveguide or grating transmission spectrum.
2. Optimize a metasurface geometry for a target phase profile.
3. Compare a neural inverse design to a gradient-based topology baseline.

## References

- https://doi.org/10.1002/lpor.202100399
- https://doi.org/10.1088/1361-6633/abb4c7
- https://doi.org/10.1038/s41578-020-00260-1
- https://doi.org/10.1016/j.eng.2024.08.016
