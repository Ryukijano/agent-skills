# AI for Forestry

## Description

Forest inventory, tree segmentation, biomass estimation, and species mapping from remote sensing and LiDAR.

## When to use

You are measuring, mapping, or monitoring forests using field plots, aerial/satellite imagery, or LiDAR point clouds.

## Key concepts

- **Forest inventory**: estimate tree counts, diameter, height, and volume.
- **Individual tree detection (ITD)**: segment crowns from CHM or point clouds.
- **LiDAR point clouds**: derive height, canopy density, intensity, and 3D structure metrics.
- **Above-ground biomass (AGB)**: regress structural metrics against field-measured biomass.
- **Species and disturbance mapping**: classify forest types, fire, insect, and harvest events.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# LiDAR/structural features per plot
X = features[["h_mean", "canopy_density", "intensity_mean", "chm_max"]]
y = field_measured_agb

rfr = RandomForestRegressor(n_estimators=300, random_state=42)
rfr.fit(X, y)
```

## Tuning notes

- Normalize and classify LiDAR point clouds; remove non-ground returns carefully.
- Use CHM-based or point-cloud deep learning (e.g., PointNet, Point Transformer) for ITD.
- Consider mixed-effects or hierarchical models to pool limited field plots.
- Validate against independent inventory plots and propagate uncertainty.

## Verification

1. Predict AGB from LiDAR features and report RMSE and R2 vs field plots.
2. Segment individual tree crowns and compare counts to field inventory.
3. Map forest disturbance and validate with aerial photo interpretation.

## References

- https://doi.org/10.1007/s40725-024-00234-4
- https://doi.org/10.1007/s40725-024-00223-7
- https://doi.org/10.3390/rs11111260
- https://doi.org/10.3390/electronics13204139
