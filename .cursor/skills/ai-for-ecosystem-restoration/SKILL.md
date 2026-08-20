# AI for Ecosystem Restoration

## Description

Monitoring rewilding, forest recovery, wetland restoration, and habitat reconstruction using remote sensing and biodiversity indicators.

## When to use

You need to measure restoration success, track rewilding progress, or prioritize interventions for degraded ecosystems.

## Key concepts

- **Restoration trajectories**: vegetation structure, species reassembly, and functional recovery.
- **Remote sensing indices**: NDVI, NDWI, LiDAR canopy structure, and multispectral time series.
- **Acoustic and camera-trap recovery metrics**: automated biodiversity indicators.
- **Treatment effectiveness**: compare restored, reference, and degraded sites.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor

# Predict restoration success from annual spectral indices + structure
model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X_indices, y_recovery_score)
```

## Tuning notes

- Define clear reference conditions and baselines across space and time.
- Use change-detection methods to separate climate from management effects.
- Combine structural (remote sensing) and faunal (sensor) recovery metrics.
- Apply site-level blocking to avoid pseudo-replication.

## Verification

1. Map restoration-induced canopy change with pre/post satellite imagery.
2. Compare acoustic-derived community recovery to reference sites.
3. Relate remote-sensing recovery scores to field-measured biodiversity.

## References

- https://doi.org/10.1371/journal.pone.0253148
- https://www.nature.com/articles/s41467-023-41693-w
- https://www.mdpi.com/2072-4292/18/2/346
- https://doi.org/10.5194/wbf2026-927
