# AI for Physics Simulation

## Description

Neural operators, surrogate models, and learned emulators for partial differential equations and physical systems.

## When to use

You want to speed up expensive physics simulations or learn emulators from data.

## Key concepts

- **Neural operators**: map between infinite-dimensional function spaces (FNO, DeepONet).
- **Surrogate models**: ML approximations of costly solvers.
- **Physics-informed neural networks (PINNs)**: embed PDE constraints in loss.
- **Digital twins**: online-learned models coupled to sensors.

## Code pattern

```python
from neuralop.models import FNO
import torch

model = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=1, out_channels=1)
x = torch.randn(1, 1, 64, 64)
y = model(x)
```

## Tuning notes

- Neural operators work best when training data covers a broad distribution of inputs.
- PINNs can be hard to train for multi-scale or high-frequency problems.
- Validate against a high-fidelity solver on out-of-distribution initial conditions.

## Verification

1. Train an FNO on a 2D Darcy flow dataset.
2. Compare FNO inference time to a classical PDE solver.
3. Test generalization to unseen parameter values and geometries.

## References

- https://github.com/neuraloperator/neuraloperator
- https://arxiv.org/abs/2010.08895
- https://arxiv.org/abs/2111.05512
- https://www.nature.com/articles/s41586-021-
