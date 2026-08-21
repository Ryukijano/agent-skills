# AI for Geology

## Description

Use ML and remote sensing to map lithology, assess mineral prospectivity, run geophysical inversions, and analyze drill-core and geologic data.

## When to use

You are working with geologic, geophysical, geochemical, or remote-sensing data and want to map lithology, structures, or mineral potential.

## Usage

- Classify lithology and structural units from multispectral/hyperspectral imagery and DEMs.
- Integrate geologic, geochemical, and geophysical layers for mineral prospectivity mapping.
- Build ML surrogates for fast magnetic, gravity, and electromagnetic geophysical inversion.
- Log drill-core images, detect fractures, and estimate mineral abundance from photos and XRF scans.

## Steps

1. Co-register geology, geophysics, geochemistry, and remote-sensing rasters to a common CRS and resolution.
2. Build a lithology/alteration classifier from satellite or airborne imagery and validate with field observations.
3. Generate multi-source evidential layers and rank mineral prospectivity with a weighted or ML-based model.
4. Train a neural operator or surrogate for geophysical inversion and compare predicted fields to forward models.
5. Process drill-core imagery and XRF data to log lithology, detect fractures, and estimate mineral abundance.
6. Produce GIS-ready maps and integrate them into exploration targeting and geologic interpretation workflows.

## Code pattern

```python
import rasterio
import geopandas as gpd
from sklearn.ensemble import RandomForestClassifier

# Stack of geology, geophysics, and remote-sensing layers
with rasterio.open("geology_stack.tif") as src:
    X = src.read().reshape(src.count, -1).T

gdf = gpd.read_file("training_labels.gpkg")
y = gdf["lithology"].values

clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
clf.fit(X, y)
```

## Tuning notes

- Co-register all raster and vector layers to a common CRS and resolution.
- Use stratified or spatial cross-validation; geology data are often spatially autocorrelated.
- Incorporate physical or geologic constraints to keep predictions geologically consistent.
- Balance rare lithology/mineral classes and quantify uncertainty.

## Verification

1. Train a lithology classifier on a multispectral stack and report per-class F1 and overall accuracy.
2. Compare mineral prospectivity scores to known deposits and generate a ROC curve.
3. Run a geophysical inversion surrogate and compare predicted fields to forward models.

## References

- https://doi.org/10.1016/j.earscirev.2024.104941
- https://doi.org/10.3390/min16060584
- https://doi.org/10.1515/geo-2025-0765
- https://doi.org/10.1007/s10712-025-09904-9
