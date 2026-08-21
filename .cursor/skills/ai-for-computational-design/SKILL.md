# AI for Computational Design

## Description

Use differentiable simulation, topology optimization, and CAD-aware generative models to co-design products and structures.

## When to use

You are designing buildings, products, mechanical parts, or architectural structures and need to integrate physical simulation, constraints, and AI-driven exploration into the design loop.

## Usage

- Combine neural networks with differentiable physics and geometry kernels.
- Run topology and shape optimization with SIMP, level-set, evolutionary, or gradient methods.
- Ensure procedural CAD and structural feasibility with solver-aided generative models.
- Explore multi-fidelity design spaces and interpolate shapes.

## Steps

1. Translate the design brief into geometry parameters, physics constraints, and objectives.
2. Build or wrap a differentiable surrogate or high-fidelity solver for the design.
3. Optimize topology or shape parameters with gradient or evolutionary search.
4. Add fabrication and assembly constraints early in the loop.
5. Validate optimized designs with high-fidelity FE/CFD and physical prototypes.
6. Generate production-ready CAD and run DRC or kernel checks.

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
