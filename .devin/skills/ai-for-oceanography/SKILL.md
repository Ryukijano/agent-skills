# AI for Oceanography

## Description

Use data-driven models to reconstruct ocean currents, detect mesoscale eddies, and forecast ocean state from satellite and in-situ observations.

## When to use

You are predicting ocean state, reconstructing currents, or detecting mesoscale features from satellite and in-situ data.

## Usage

- Reconstruct high-resolution surface currents by fusing sea surface height, temperature, and wind data.
- Detect and track mesoscale eddies in satellite altimetry and multi-modal ocean imagery.
- Build neural surrogates for ocean circulation and biogeochemical variables at nowcasting to seasonal lead times.
- Downscale and gap-fill satellite ocean fields using deep-learning super-resolution and data imputation.

## Steps

1. Ingest satellite altimetry, SST, wind, in-situ drifters, and model reanalysis for the target region.
2. Preprocess data (regrid, gap-fill, normalize) and derive dynamic variables such as SSH, EKE, and geostrophic currents.
3. Train a neural current-reconstruction model (e.g., U-Net, GESTNet) on matched SSH/SST/wind and drifter observations.
4. Run an eddy-detection model on the reconstructed fields and track eddy trajectories over time.
5. Validate current maps against independent drifter trajectories and eddy tracks against a reference catalog.
6. Deploy the workflow for operational nowcasting or downscale climate projections for ecosystem and shipping applications.

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
