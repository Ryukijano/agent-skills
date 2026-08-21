# AI for Environmental Science

## Description

Use remote sensing and integrated modeling to map land cover, monitor ecosystems, and assess environmental change and risk.

## When to use

You are analyzing environmental systems using satellite, in-situ, or model data and need classification, regression, or change detection.

## Usage

- Map land use and land cover from satellite or drone imagery.
- Monitor vegetation, water bodies, snow/ice, and urban expansion over time.
- Predict pollutant transport and ecological exposure with integrated models.
- Detect anomalies and trends from multi-temporal remote-sensing indices.

## Steps

1. Collect satellite, in-situ, and model data; apply atmospheric correction, cloud masking, and spectral indices.
2. Build time-composited training datasets and define a land-cover or ecosystem-change classification scheme.
3. Train a classifier (e.g., Random Forest, U-Net) and validate with spatial cross-validation and a reference product.
4. Compute overall accuracy, kappa, and per-class F1; generate land-cover and change maps.
5. Run integrated assessment or pollutant-fate models and compare to observations.
6. Deploy the monitoring pipeline and update maps as new imagery becomes available.

## Code pattern

```python
import rioxarray
from sklearn.ensemble import RandomForestClassifier

# Sentinel/Landsat raster stack
rds = rioxarray.open_rasterio("satellite_stack.tif")
X = rds.stack(pixel=("y", "x")).T.values
y = land_cover_reference_values

clf = RandomForestClassifier(n_estimators=300, class_weight="balanced")
clf.fit(X, y)
```

## Tuning notes

- Apply atmospheric correction, cloud masking, and spectral indices (NDVI, NDWI).
- Composite images over time to reduce noise and missing data.
- Use spatial or block cross-validation because pixels are spatially correlated.
- Consider class hierarchy and label noise in land-cover products.

## Verification

1. Classify a satellite image and compare to a validated land-cover reference.
2. Compute overall accuracy, kappa, and per-class F1 scores.
3. Detect land-cover change between two time periods and validate with ground data.

## References

- https://doi.org/10.1016/j.scitotenv.2023.167705
- https://doi.org/10.1007/s44163-024-00198-1
- https://doi.org/10.3389/fenvs.2024.1336088
- https://doi.org/10.1016/j.envsoft.2024.106312
