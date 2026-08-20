# AI for Generative Engineering

## Description

Diffusion, VAE, and generative inverse design for engineering concepts, constraint-aware generation, and performance-conditioned shape and material synthesis.

## When to use

You are exploring novel engineering designs (shapes, structures, materials, or processes) and want to generate or complete candidates that satisfy performance and manufacturing constraints.

## Key concepts

- **Generative inverse design**: learn a distribution over design parameters conditioned on target performance.
- **Constraint-aware generation**: embed physics, safety, or feasibility constraints into the generative process (e.g., negative-data training, repair loops).
- **Diffusion and flow matching for design**: denoising and conditional diffusion for continuous or structured design spaces.
- **Multi-objective and topology optimization**: generate Pareto-optimal designs and structures.

## Code pattern

```python
import torch

# Simple constrained repair loop for generated designs
def repair(design, simulator, target, max_iter=20, lr=0.01):
    for _ in range(max_iter):
        pred = simulator(design)
        loss = ((pred - target) ** 2).mean()
        if loss < 0.01:
            break
        design = design - lr * torch.autograd.grad(loss, design)[0]
    return design
```

## Tuning notes

- Train separate feasibility classifiers to reject physically impossible designs.
- Use surrogate simulators to amortize expensive FE/CFD evaluations.
- Balance novelty with distributional similarity to avoid unrealistic extrapolations.
- Validate generated designs with the full simulator or physical tests.

## Verification

1. Generate 100 structural/aerodynamic candidates and check what fraction satisfy constraints.
2. Compare a generative inverse-design pipeline to a gradient-based inverse-design baseline.
3. Plot the Pareto front of generated designs across performance and manufacturability.

## References

- https://arxiv.org/abs/2412.13281
- https://arxiv.org/abs/2306.15166
- https://arxiv.org/abs/2309.02040
- https://arxiv.org/abs/2406.09143
