# Signal and Image Processing on GPU

## Description

FFT, wavelets, filtering, compressed sensing, and tomography with cuFFT, RAPIDS, and GPU pipelines.

## When to use

You are processing large 1D/2D/3D signals or images on GPU.

## Key concepts

- **cuFFT**: 1D/2D/3D FFT, batched, multi-GPU up to 16 GPUs.
- **cuFFT callbacks**: pre/post-process inside FFT for DSP pipelines.
- **Wavelets**: PyWavelets, `cupy` wrapper, or custom CUDA.
- **Compressed sensing**: TV-regularized reconstruction, SART, filtered back-projection.
- **GPU image stacks**: RAPIDS cuCIM, `cupy`, `dask-cuda`.

## Code pattern

```python
import cupy as cp

x = cp.random.randn(1024, 1024, dtype=cp.float32)
X = cp.fft.fft2(x)
```

For tomography:

```python
# ASTRA or TomoPy on GPU
import astra
proj_id = astra.create_projector('cuda', ...)
```

## Tuning notes

- Batch FFTs for better occupancy; use `cufftXt` for multi-GPU 3D FFTs.
- Compressed-sensing reconstructions often use `cupy.linalg` for TV proximal steps.
- Use `float32` for speed; `float64` for accuracy-critical inverse problems.

## Verification

1. Compare `cupy.fft.fft2` to NumPy `np.fft.fft2` and confirm accuracy/speed.
2. Run a filtered back-projection on a test sinogram and compare to ground truth.
3. Profile with Nsight Systems to separate I/O from compute.

## References

- https://docs.nvidia.com/cuda/cufft/
- https://cupy.dev/
- https://rapids.ai/
- https://doi.org/10.1364/ao.378466
