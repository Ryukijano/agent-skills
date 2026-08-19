# Generative Models for Scientific Discovery

## Description

Diffusion, flow matching, score-based models, and normalizing flows for molecules, materials, and inverse design.

## When to use

You are generating molecules, materials, structures, or trajectories with diffusion/flow models.

## Key concepts

- **Diffusion models**: DDPM, score-based, EDM, MOFDiff, CDVAE.
- **Flow matching**: FlowMol, FlowER, Rectified Flow; deterministic ODEs, faster sampling.
- **Normalizing flows**: for continuous molecular/crystal generation.
- **Inverse design**: generate candidates with target properties.
- **Evaluation**: validity, uniqueness, novelty, property distribution matching.

## Code pattern

```python
import torch

# Diffusion model training loop
noise = torch.randn_like(x)
t = torch.rand(x.size(0), device='cuda')
noisy = alpha_t * x + sigma_t * noise
pred = model(noisy, t)
loss = F.mse_loss(pred, noise)
```

For flow matching:

```python
# Interpolate x0 (noise) and x1 (data)
t = torch.rand(b, 1, device='cuda')
xt = (1 - t) * x0 + t * x1
# velocity field v_t(x)
loss = F.mse_loss(model(xt, t), x1 - x0)
```

## Tuning notes

- Flow matching often trains more stably than diffusion and has fewer hyperparameters.
- E(3) equivariant diffusion for molecules preserves physical symmetries.
- For crystals, use periodic E(3)-equivariant flows (DiffCSP).

## Verification

1. Train a small diffusion/flow model and sample 1000 candidates.
2. Compute validity/uniqueness/novelty metrics.
3. Relax generated structures with a surrogate (MACE, CHGNet) and check stability.

## References

- https://doi.org/10.48550/arxiv.2404.19739
- https://github.com/jiaor17/DiffCSP
- https://github.com/microsoft/mattergen
- https://www.nature.com/articles/s43588-025-00924-4
