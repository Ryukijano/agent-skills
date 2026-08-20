# AI for Planetary Science

## Description

Machine learning for mission data analysis, terrain classification, crater detection, atmospheric retrievals, and exoplanet characterization.

## When to use

You are analyzing spacecraft imagery, spectra, altimetry, or exoplanet light curves for Solar System or exoplanet science.

## Key concepts

- **Orbital imagery**: segmentation and classification of terrain, craters, and geologic units.
- **Spectral unmixing**: decomposing hyperspectral cubes into endmember compositions.
- **Radiative transfer**: fast forward models and retrieval of atmospheric properties.
- **Interior and orbital models**: emulation of planet structure and radial-velocity signals.

## Code pattern

```python
import numpy as np
import rasterio
from sklearn.ensemble import RandomForestClassifier

with rasterio.open("mars_dem.tif") as src:
    dem = src.read(1)

# Terrain classification from DEM and derived slope
slope = np.gradient(dem)
X = np.stack([dem, slope], axis=-1).reshape(-1, 2)
clf = RandomForestClassifier(n_estimators=200).fit(X, labels)
```

## Tuning notes

- Use map-projected, co-registered data with consistent illumination.
- Handle rare geologic classes with stratified sampling.
- Validate against human-labeled geologic maps and in-situ spectra.

## Verification

1. Segment craters on the Moon or Mars and compare to reference catalogs.
2. Classify spectral units from a planetary hyperspectral cube.
3. Fit an exoplanet transmission spectrum with a neural surrogate.

## References

- https://doi.org/10.3847/25c2cfeb.aa328727
- https://arxiv.org/abs/2604.09152
- https://arxiv.org/abs/2310.17681
- https://ui.adsabs.harvard.edu/abs/2025epsc.conf.1467K/abstract
