# AI for Natural Hazards

## Description

Multi-hazard susceptibility mapping and early warning for landslides, floods, wildfires, and land subsidence with ML and remote sensing.

## When to use

You are mapping multi-hazard risk, forecasting imminent events, or designing early warning systems for landslides, floods, wildfires, or subsidence.

## Key concepts

- **Hazard susceptibility**: probabilistic mapping of where hazards may occur.
- **Multi-hazard assessment**: combined landslide, flood, wildfire, and subsidence modeling.
- **Early warning systems**: triggers, thresholds, and lead-time optimization.
- **Remote sensing and InSAR**: Sentinel-1/2, DEM, and ground deformation data.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Multi-hazard susceptibility from terrain, hydrology, and vegetation
clf = RandomForestClassifier(n_estimators=400, class_weight="balanced")
clf.fit(X_hazard, y_hazard_type)
```

## Tuning notes

- Treat hazards as multi-label when co-occurrence is possible.
- Use spatial cross-validation; susceptibility varies by region.
- Integrate physical-process models with ML for short-horizon forecasting.
- Calibrate warning thresholds with stakeholders and historical event data.

## Verification

1. Build landslide/flood/wildfire susceptibility maps and validate with AUC-ROC.
2. Compare an optimized RF to single-hazard baseline maps.
3. Test an early-warning trigger against past events and report lead time.

## References

- https://link.springer.com/article/10.1038/s41598-025-15381-2
- https://iopscience.iop.org/article/10.1088/1748-9326/ae5f7f/meta
- https://doi.org/10.1038/s41598-020-69233-2
- https://www.nature.com/articles/s41598-026-52139-w
