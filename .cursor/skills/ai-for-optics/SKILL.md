# AI for Optics

## Description

Computational imaging, lens design, wavefront shaping, optical metrology, and inverse scattering with deep learning.

## When to use

You are reconstructing images from indirect optical measurements, designing phase masks, or calibrating complex optical systems.

## Key concepts

- **Inverse problems**: image reconstruction from undersampled or coded measurements.
- **Wave propagation**: Fourier optics, diffraction, and point-spread functions.
- **Coded apertures and phase masks**: jointly optimizing hardware and algorithms.
- **Phase retrieval**: recovering phase from intensity measurements.

## Code pattern

```python
import numpy as np
from scipy.signal import convolve2d

# Forward model: image convolved with a known PSF
psf = np.load("psf.npy")
measurement = convolve2d(gt_image, psf, mode="same", boundary="wrap")
# A learned deconvolution network would invert this
```

## Tuning notes

- Encode the physical forward model in the loss or network architecture.
- Use self-supervised or physics-informed training when paired ground truth is scarce.
- Validate on realistic noise, aberrations, and sensor nonlinearities.

## Verification

1. Train a phase-retrieval network and compare to Gerchberg-Saxton.
2. Learn a coded aperture for compressive spectral imaging.
3. Reconstruct a microscopy stack from diffraction patterns.

## References

- https://arxiv.org/abs/2210.16709
- https://arxiv.org/abs/2207.00164
- https://doi.org/10.1038/s41377-022-00714-x
- https://www.nature.com/articles/s41377-022-00743-6
