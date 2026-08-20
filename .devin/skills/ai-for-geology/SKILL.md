# AI for Geology

## Description

Geologic mapping, mineral prospectivity, geophysical inversion, drill-core imagery, and remote sensing with ML and deep learning.

## When to use

You are working with geologic, geophysical, geochemical, or remote-sensing data and want to map lithology, structures, or mineral potential.

## Key concepts

- **Geologic mapping**: supervised classification of lithology and structural units from multispectral/hyperspectral imagery and DEMs.
- **Mineral prospectivity mapping (MPM)**: integrate multi-source evidential layers to rank exploration targets.
- **Geophysical inversion**: ML surrogates and neural operators for fast magnetic, gravity, and EM inversion.
- **Drill-core imagery**: core logging, fracture detection, and mineral abundance from drill-core photos and XRF scans.
- **Remote sensing**: satellite and airborne data for alteration mapping and structural interpretation.

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
