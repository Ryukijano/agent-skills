# Machine Learning for Topology Optimization

## Description

SIMP, neural reparameterization, generative topology optimization, physics-informed neural networks, and learned resolution-free solvers for structural design.

## When to use

You need to distribute material inside a design domain to minimize compliance (or another objective) under load, boundary, and volume constraints.

## Key concepts

- **SIMP**: Solid Isotropic Material with Penalization for density-based topology optimization.
- **Neural reparameterization**: using an NN (e.g., CNN, implicit field) to represent density or signed distance.
- **Solver-in-the-loop**: training a generative model with an FE/physics oracle.
- **Physics-informed neural networks (PINNs)**: embedding PDE constraints directly in the loss.
- **Resolution-free models**: predict topologies at arbitrary grid sizes and aspect ratios.

## Code pattern

```python
import torch

# Learned topology generator conditioned on boundary conditions
class TopologyNet(torch.nn.Module):
    def __init__(self, cond_dim, grid_size):
        super().__init__()
        self.mlp = torch.nn.Sequential(
            torch.nn.Linear(cond_dim, 256), torch.nn.ReLU(),
            torch.nn.Linear(256, grid_size * grid_size), torch.nn.Sigmoid()
        )

    def forward(self, cond):
        return self.mlp(cond).view(-1, 1, grid_size, grid_size)

cond = torch.tensor([[load_x, load_y, fix_x, fix_y, volfrac]])
model = TopologyNet(cond_dim=5, grid_size=64)
rho = model(cond)  # density field (0 = void, 1 = solid)
```

## Tuning notes

- Penalization power $p$ in SIMP typically starts around 3 and is gradually increased.
- Filter densities to avoid checkerboarding and ensure mesh independence.
- For learned methods, ground-truth data from conventional TO is often required.
- Validate compliance and volume fraction error against FE analysis.

## Verification

1. Run SIMP on a cantilever beam and visualize the optimized density field.
2. Train a neural surrogate and compare its compliance prediction to FEA.
3. Evaluate a generative topology model on out-of-distribution loads and aspect ratios.

## References

- https://arxiv.org/abs/2210.10782
- https://arxiv.org/abs/2407.13954
- https://arxiv.org/abs/2510.23667
- https://arxiv.org/abs/2502.13174
- https://arxiv.org/abs/2209.05098
