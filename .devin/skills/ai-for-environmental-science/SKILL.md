# AI for Environmental Science

## Description

Remote sensing, land-cover mapping, ecosystem service assessment, and integrated modeling for environmental monitoring and analysis.

## When to use

You are analyzing environmental systems using satellite, in-situ, or model data and need classification, regression, or change detection.

## Key concepts

- **Land-use/land-cover mapping**: classify satellite or drone imagery into thematic classes.
- **Ecosystem monitoring**: track vegetation condition, water bodies, snow/ice, and urban expansion.
- **Environmental fate and exposure**: predict pollutant transport and ecological risk.
- **Integrated assessment models**: couple physical, ecological, and socio-economic data.
- **Remote sensing time series**: use multi-temporal indices to detect anomalies and trends.

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
