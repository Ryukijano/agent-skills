# AI for Wetlands

## Description

Wetland mapping, inundation dynamics, cover-type classification, and hydrological trend monitoring from satellite time series.

## When to use

You are mapping wetland extent, tracking seasonal inundation, classifying cover types, or detecting hydrological change.

## Key concepts

- **Wetland extent and dynamics**: MNDWI, NDWI, Sentinel-1/2 time series.
- **Cover-type classification**: open water, aquatic vegetation, turbid water, moist soil.
- **Flood-pulse monitoring**: intra- and inter-annual inundation patterns.
- **Global wetland models**: Swamp-AI, WetlandMapper, GEE-based workflows.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Classify wetland cover types from multispectral + SAR stack
clf = RandomForestClassifier(n_estimators=300)
clf.fit(X, y_cover)
```

## Tuning notes

- Combine optical and SAR to handle clouds and vegetation.
- Account for seasonal water-level fluctuations and phenology.
- Use high-tide/low-tide or wet/dry season composites for training.
- Validate against field surveys and airborne LiDAR where possible.

## Verification

1. Map wetland extent and compare to a global wetland product.
2. Classify cover types and report producer/user accuracies.
3. Generate an annual inundation time series and compare to gauged water levels.

## References

- https://www.nature.com/articles/s41598-026-39257-1
- https://doi.org/10.31223/x5jx93
- https://www.mdpi.com/2072-4292/14/23/6104
- https://www.sei.org/tools/wetsat-ml-wetlands-flooding-extent-and-trends-using-satellite-observations-and-machine-learning/
