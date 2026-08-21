# AI for Volcanology

## Description

Forecast eruption probability by fusing seismic, gas, and satellite data to issue early warnings at volcanoes like Whakaari.

## When to use

You are analyzing volcano seismic and infrasound data to detect unrest or forecast eruptions.

## Usage

- Classify volcano-seismic event types (VT, LP, VLP, tremor, explosion quakes) from continuous waveforms.
- Detect precursory anomalies and patterns in multi-sensor monitoring data before eruptions.
- Build time-to-eruption or eruption-probability models from seismic, deformation, gas, and thermal time series.
- Fuse seismic, infrasound, gas, thermal, and satellite observations into a unified hazard dashboard.

## Steps

1. Collect continuous seismic, infrasound, gas, deformation, and thermal observations for the target volcano.
2. Label or cluster volcanic events (VT, LP, VLP, tremor, explosion quakes) and train a classifier on waveform features.
3. Run unsupervised anomaly detection on long-duration monitoring streams to flag deviations from background behavior.
4. Train a time-to-eruption or probabilistic forecasting model using multi-sensor precursors and past eruption records.
5. Generate eruption-probability alerts and validate lead time against historical eruptions.
6. Combine forecasts with scenario-based hazard maps and observatory workflows for decision support.

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
