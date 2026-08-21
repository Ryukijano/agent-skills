# AI for Digital Health

## Description

Use AI to build or evaluate consumer-facing digital health tools, integrate wearable or sensor data, or conducting remote monitoring and digital-biomarker studies.

## When to use

You are building or evaluating consumer-facing digital health tools, integrating wearable or sensor data, or conducting remote monitoring and digital-biomarker studies.

## Usage

- Capture wearable, app, and sensor signals.
- Process PPG, accelerometry, sleep, and activity data.
- Extract digital biomarkers and EMA endpoints.
- Build remote monitoring dashboards and alerts.

## Steps

1. Capture wearable, app, and sensor signals.
2. Process PPG, accelerometry, sleep, and activity data.
3. Extract digital biomarkers and EMA endpoints.
4. Build remote monitoring dashboards and alerts.
5. Validate against clinical gold standards and reference devices.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import numpy as np
import pandas as pd
from scipy.signal import find_peaks

# Heart-rate peaks from a wearable PPG signal
peaks, _ = find_peaks(ppg_signal, distance=50)
hr = 60 * fs / np.diff(peaks)
```

## Tuning notes

- Validate against reference devices and clinical measurements; sensor placement and motion artifacts matter.
- Protect privacy of continuous, fine-grained behavioral and physiological data.
- Distinguish wellness claims from regulated medical-device claims.
- Use time-series cross-validation because wearables generate streaming, autocorrelated data.

## Verification

1. Extract a digital biomarker from wearable data and compare it to a clinical gold standard.
2. Build a remote-monitoring dashboard with anomaly alerts for a simulated cohort.
3. Assess class balance and subgroup calibration for a digital health risk model.

## References

- https://doi.org/10.1038/s41591-021-01614-0
- https://doi.org/10.1038/s41591-022-01981-2
- https://doi.org/10.1038/s41591-018-0307-0
- https://doi.org/10.1038/s41591-026-04229-5
