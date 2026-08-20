# AI for Computational Design

## Description

Differentiable simulation, topology optimization, CAD-aware generative models, and solver-in-the-loop co-design for architecture, products, and structures.

## When to use

You are designing buildings, products, mechanical parts, or architectural structures and need to integrate physical simulation, constraints, and AI-driven exploration into the design loop.

## Key concepts

- **Differentiable design**: combine neural networks with differentiable physics and geometry kernels.
- **Topology and shape optimization**: SIMP, level-set, evolutionary, and gradient-based methods.
- **Solver-aided generative models**: use geometric/physics solvers to ensure procedural CAD and structural feasibility.
- **Design-space exploration**: multi-fidelity surrogates and optimal-transport interpolation of shapes.

## Code pattern

```python
import torch

# Differentiate a simple surrogate simulator with respect to a design variable
def compliance_loss(design, solver, target_shape):
    shape = solver(design)
    return ((shape - target_shape) ** 2).mean()

design = torch.nn.Parameter(torch.zeros(16))
optimizer = torch.optim.Adam([design], lr=0.01)
for _ in range(100):
    optimizer.zero_grad()
    loss = compliance_loss(design, surrogate_solver, target)
    loss.backward()
    optimizer.step()
```

## Tuning notes

- Ensure the surrogate simulator is accurate enough in the target design region.
- Use mesh-independent representations when possible to avoid retraining for new topologies.
- Augment with fabrication and assembly constraints early in the loop.
- Validate optimized designs with high-fidelity FE/CFD and physical prototypes.

## Verification

1. Optimize a simple truss or shell structure and compare compliance to a baseline.
2. Generate a parametric CAD part from a design brief and verify it with a CAD kernel.
3. Run a multi-objective design sweep and identify the knee of the Pareto front.

## References

- https://arxiv.org/abs/2409.02606
- https://arxiv.org/abs/2511.17111
- https://arxiv.org/abs/2405.18075
- https://arxiv.org/abs/2502.09819
