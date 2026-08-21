# AI for Optics

## Description

Use deep learning to reconstruct images, retrieve phase, design optical elements, and solve inverse scattering problems in computational imaging.

## When to use

You are reconstructing images from indirect optical measurements, designing phase masks, or calibrating complex optical systems.

## Usage

- Reconstruct images from undersampled, coded, or indirect optical measurements.
- Retrieve phase from intensity-only measurements in microscopy and astronomy.
- Co-design phase masks, coded apertures, and metalenses with reconstruction networks.
- Deconvolve images from measured point-spread functions and aberrations.

## Steps

1. Formulate the physical forward model (PSF, diffraction, or scattering operator).
2. Acquire paired measurements and ground truth, or use self-supervised/physics-informed training.
3. Train an inversion network or optimize an optical element end-to-end.
4. Validate on realistic noise, aberrations, and sensor nonlinearities.
5. Compare reconstruction quality to classical methods such as Gerchberg-Saxton or deconvolution.

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
