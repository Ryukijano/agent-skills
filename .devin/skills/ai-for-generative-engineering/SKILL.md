# AI for Generative Engineering

## Description

Use diffusion, VAEs, and flow models to generate engineering designs that meet performance and manufacturing constraints.

## When to use

You are exploring novel engineering designs (shapes, structures, materials, or processes) and want to generate or complete candidates that satisfy performance and manufacturing constraints.

## Usage

- Generate design candidates conditioned on target performance with generative inverse design.
- Embed physics, safety, and feasibility constraints into the generative process.
- Apply diffusion and flow matching to continuous or structured design spaces.
- Produce Pareto-optimal designs across multiple objectives.

## Steps

1. Define the design space, performance targets, and constraints (physics, safety, manufacturability).
2. Train a generative model on existing designs and their performance labels.
3. Add feasibility classifiers or repair loops to reject physically impossible designs.
4. Generate a diverse set of candidates and evaluate with surrogate or full simulations.
5. Check constraint satisfaction and compute the Pareto front across objectives.
6. Validate top designs with high-fidelity FE/CFD and physical tests.

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
