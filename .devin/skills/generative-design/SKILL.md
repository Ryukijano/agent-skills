# AI-Driven Generative Design

## Description

Deep generative models (VAEs, GANs, diffusion) for engineering design synthesis, constraint-aware generation, Pareto-front exploration, and design automation.

## When to use

You want to automatically explore, synthesize, or optimize mechanical/product designs subject to performance, manufacturing, and aesthetic constraints.

## Key concepts

- **Generative design**: algorithms that generate candidate designs from requirements and constraints.
- **Conditional generative models**: VAEs, GANs, diffusion models conditioned on design specs.
- **Pareto-front exploration**: sampling the trade-off between competing objectives (weight, stiffness, cost).
- **Constraint handling**: geometry, physics, and manufacturability constraints embedded in generation or filtering.
- **Design representations**: voxels, B-reps, parametric CAD, point clouds, and latent fields.

## Code pattern

```python
import torch
import torch.nn as nn

# Conditional VAE for a simple design latent space
class CVAE(nn.Module):
    def __init__(self, input_dim, cond_dim, latent_dim):
        super().__init__()
        self.encoder = nn.Sequential(nn.Linear(input_dim + cond_dim, 256), nn.ReLU())
        self.fc_mu = nn.Linear(256, latent_dim)
        self.fc_logvar = nn.Linear(256, latent_dim)
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim + cond_dim, 256), nn.ReLU(),
            nn.Linear(256, input_dim)
        )

    def reparameterize(self, mu, logvar):
        std = torch.exp(0.5 * logvar)
        eps = torch.randn_like(std)
        return mu + eps * std

    def forward(self, x, c):
        h = self.encoder(torch.cat([x, c], dim=-1))
        z = self.reparameterize(self.fc_mu(h), self.fc_logvar(h))
        return self.decoder(torch.cat([z, c], dim=-1))

# Generate new design candidates conditioned on stiffness target
cvae = CVAE(input_dim=128, cond_dim=8, latent_dim=16)
condition = torch.randn(10, 8)          # e.g. target stiffness, volume fraction
latent = torch.randn(10, 16)
designs = cvae.decoder(torch.cat([latent, condition], dim=-1))
```

## Tuning notes

- Condition vectors should encode meaningful physical or semantic design requirements.
- Use simulation-in-the-loop oracles to filter physically invalid generations.
- Balance diversity and quality with temperature, truncation, or latent-space interpolation.
- Validate generated designs with FEA/CFD or a learned surrogate before fabrication.

## Verification

1. Train a conditional generative model on a small design dataset and sample 100 candidates.
2. Evaluate constraint satisfaction and performance of generated designs against a simulator.
3. Produce a Pareto-front plot of two competing objectives (e.g., weight vs. stiffness).

## References

- https://arxiv.org/abs/2110.10863
- https://doi.org/10.1115/1.4053859
- https://doi.org/10.48550/arxiv.2502.02628
- https://arxiv.org/abs/2302.02913
- https://www.autodesk.com/solutions/generative-design
