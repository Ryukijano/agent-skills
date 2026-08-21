# AI for Planetary Science

## Description

Use machine learning to classify planetary terrain, detect craters, retrieve atmospheres, and characterize exoplanets from spacecraft and telescope data.

## When to use

You are analyzing spacecraft imagery, spectra, altimetry, or exoplanet light curves for Solar System or exoplanet science.

## Usage

- Segment terrain, craters, and geologic units from orbital imagery and digital elevation models.
- Unmix hyperspectral cubes to map endmember compositions and surface mineralogy.
- Retrieve atmospheric properties from exoplanet transmission and emission spectra.
- Emulate radiative-transfer and interior models to accelerate mission data analysis.

## Steps

1. Co-register and map-project orbital imagery, spectra, or altimetry for the target body.
2. Train a terrain or crater segmentation model on georeferenced, human-labeled regions.
3. Build a spectral unmixing or atmospheric retrieval surrogate validated against physics models.
4. Compare predictions to in-situ spectra or published geologic maps.
5. Integrate the model into a mission pipeline for target prioritization and downlink planning.

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
- https://doi.org/10.5194/epsc-dps2025-1467
