# AI for Computer Graphics

## Description

Use AI for Computer Graphics to synthesize photorealistic images, reconstruct geometry and estimate materials.

## When to use

You are synthesizing or editing photorealistic images, reconstructing scenes from observations, or integrating learned components into a traditional rendering pipeline.


## Usage


- **Neural radiance fields (NeRF)**: Implicit 3D scene representations via MLPs and volume rendering.
- **3D Gaussian splatting**: Explicit point-based scene representation with fast rasterization.
- **Differentiable rendering**: Propagate gradients through light transport for inverse rendering.
- **Material and lighting estimation**: Recover reflectance, illumination, and geometry from images.
- **Generative image synthesis**: Diffusion and GAN-based texture/material generation.

## Steps

1. Collect and prepare multi-view images, scene geometry and lighting data.
2. Synthesize or editing photorealistic images.
3. Reconstruct scenes from observations.
4. Integrate learned components into a traditional rendering pipeline.
5. Validate by fiting a small NeRF to a synthetic multi-view cube and render novel views.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import torch
import torch.nn as nn


class NeRFMLP(nn.Module):
    def __init__(self, pos_dim=3, hidden=256):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(pos_dim, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, hidden),
            nn.ReLU(),
            nn.Linear(hidden, 4)  # RGB + density
        )

    def forward(self, x):
        return self.net(x)
```


## Tuning notes

- Combine positional encoding for high-frequency details.
- Use coarse plus fine sampling for efficient ray marching.
- Differentiable rendering is expensive; use efficient samplers and cache radiance fields.
- Validate synthesized views against held-out camera poses.


## Verification

1. Fit a small NeRF to a synthetic multi-view cube and render novel views.
2. Compare PSNR and SSIM of rendered views to ground truth.
3. Estimate a simple BRDF from flash/no-flash image pairs.

## References

- https://arxiv.org/abs/2111.05849
- https://arxiv.org/abs/2504.01402
- https://arxiv.org/abs/2501.13104
- https://doi.org/10.48550/arxiv.2402.00028
