# AI for Particle Physics

## Description

ML for collider event classification, jet tagging, fast detector simulation, neutrino event reconstruction, and new-physics searches.

## When to use

You are classifying high-energy physics events, accelerating detector simulation, or searching for rare signals in collider or neutrino data.

## Key concepts

- **Jet tagging and event classification**: CNNs, graph networks, and transformers on point clouds.
- **Fast simulation**: generative models for calorimeter showers and detector response.
- **Anomaly detection**: model-agnostic searches for new physics.
- **Lorentz and SE(3) equivariance**: respecting spacetime symmetries in architectures.

## Code pattern

```python
import torch
import torch.nn as nn

class ParticleNet(nn.Module):
    def __init__(self, in_dim=3, out_dim=2):
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv1d(in_dim, 64, 1), nn.ReLU(), nn.AdaptiveAvgPool1d(1)
        )
        self.head = nn.Linear(64, out_dim)

    def forward(self, x):
        return self.head(self.encoder(x).squeeze(-1))
```

## Tuning notes

- Handle pile-up, detector noise, and variable multiplicities with masking.
- Use equivariant or permutation-invariant architectures for particle clouds.
- Calibrate confidence and significance estimates for discovery claims.

## Verification

1. Train a top-quark jet tagger and compare to a rule-based baseline.
2. Generate fast calorimeter showers and compare shower shapes to Geant4.
3. Run an anomaly-detection search on a public collider dataset.

## References

- https://arxiv.org/abs/1912.08245
- https://arxiv.org/abs/2102.02770
- https://arxiv.org/abs/2112.03769
- https://doi.org/10.1140/epjs/s11734-024-01364-3
