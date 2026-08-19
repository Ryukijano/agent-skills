# AI Weather and Climate Forecasting on GPU

## Description

FourCastNet, GraphCast, Pangu-Weather, ClimaX, and ECMWF ai-models on GPU clusters.

## When to use

You are training or running data-driven weather/climate models on GPU.

## Key concepts

- **FourCastNet**: AFNO transformer, global week-long forecasts in <2 seconds.
- **GraphCast**: graph neural network, state-of-the-art deterministic 10-day forecasts.
- **Pangu-Weather**: 3D Earth-specific transformer.
- **ClimaX**: foundation model trained on CMIP6 + ERA5.
- **ECMWF ai-models**: unified inference interface.

## Code pattern

```python
from ai_models import run_model
run_model("fourcastnet", input_file="era5_20200101.grb", output="out.nc")
```

For training ClimaX:

```python
from climax import ClimaX
model = ClimaX(img_size=(32, 64), patch_size=2)
```

## Tuning notes

- These models are large but inference is cheap; optimize I/O (NetCDF/Zarr) and batch size.
- FourCastNet scales to thousands of GPUs for ensemble generation.
- Use `bfloat16` for training; keep normalization in FP32.

## Verification

1. Run a 10-day deterministic forecast and compare RMSE to IFS.
2. Run `ai-models` CLI on a single ERA5 time step.
3. Profile with Nsight Systems to find I/O vs compute time.

## References

- https://github.com/NVlabs/FourCastNet
- https://github.com/ecmwf-lab/ai-models
- https://github.com/google-deepmind/graphcast
- https://doi.org/10.1145/3592979.3593412
