# AI for Volcanology

## Description

Machine learning for eruption forecasting, volcanic seismicity classification, and hazard assessment.

## When to use

You are analyzing volcano seismic and infrasound data to detect unrest or forecast eruptions.

## Key concepts

- **Volcano-seismic event classes**: VT, LP, VLP, tremor, explosion quakes.
- **Unsupervised anomaly detection**: identify precursory signals in continuous data.
- **Eruption forecasting**: time-to-eruption models from multi-sensor time series.
- **Multi-sensor fusion**: seismic, deformation, gas, thermal, and satellite data.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Anomaly detection on feature vectors extracted from seismic streams
clf = IsolationForest(contamination=0.05)
clf.fit(event_features)
outliers = clf.predict(event_features)
```

## Tuning notes

- Classifiers must generalize across volcanoes; use transfer learning cautiously.
- Unsupervised methods can reveal unknown precursors but need careful validation.
- Combine with physical models and expert interpretation.

## Verification

1. Classify a small labeled set of volcanic events.
2. Run anomaly detection before a known eruption and inspect lead time.
3. Compare an ML forecast to a physics-based baseline.

## References

- https://arxiv.org/abs/2603.17855
- https://doi.org/10.1029/2024gl108631
- https://doi.org/10.1007/978-3-031-15432-4
- https://github.com/darren-tpk/voiss-net
