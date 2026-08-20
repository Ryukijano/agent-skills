# AI for Oceanography

## Description

Data-driven ocean forecasting, current reconstruction, eddy detection, and marine ecosystem modeling.

## When to use

You are predicting ocean state, reconstructing currents, or detecting mesoscale features from satellite and in-situ data.

## Key concepts

- **Neural ocean models**: data-driven surrogates for ocean circulation.
- **Eddy detection**: identify and track mesoscale eddies in satellite altimetry.
- **Current reconstruction**: fuse sea-level, wind, and in-situ observations.
- **Nowcasting to seasonal forecasting**: lead-time-specific prediction tasks.

## Code pattern

```python
import xarray as xr
from scipy.ndimage import gaussian_filter

# Load sea-surface height and detect extrema as eddy candidates
ssh = xr.open_dataset("ssh.nc").ssh
candidates = detect_extrema(ssh, threshold=0.05)
```

## Tuning notes

- Incorporate physical constraints such as mass and momentum conservation.
- Satellite data is noisy and gappy; use data imputation and multi-sensor fusion.
- Validate against reanalysis products and mooring observations.

## Verification

1. Train a small neural network to forecast SSH at a point.
2. Detect and track eddies and compare to a manual catalog.
3. Reconstruct surface currents and compare to drifter trajectories.

## References

- https://sp.copernicus.org/articles/5-opsr/22/2025/
- https://doi.org/10.1029/2025jh000686
- https://os.copernicus.org/articles/21/1065/2025/
- https://xgcm.readthedocs.io/
