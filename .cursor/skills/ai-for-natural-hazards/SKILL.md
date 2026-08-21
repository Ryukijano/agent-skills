# AI for Natural Hazards

## Description

Predict landslide and wildfire risk from satellite and sensor data to trigger early warnings and protect infrastructure.

## When to use

You are mapping multi-hazard risk, forecasting imminent events, or designing early warning systems for landslides, floods, wildfires, or subsidence.

## Usage

- Fuse terrain, hydrology, vegetation, and Sentinel-1/2 data.
- Model susceptibility for landslides, floods, wildfires, and subsidence.
- Calibrate warning thresholds with historical events.
- Build multi-hazard susceptibility maps.

## Steps

1. Fuse terrain, hydrology, vegetation, and Sentinel-1/2 data.
2. Model susceptibility for landslides, floods, wildfires, and subsidence.
3. Calibrate warning thresholds with historical events.
4. Build multi-hazard susceptibility maps.
5. Validate lead time and accuracy with stakeholders.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
