# AI for Irrigation

## Description

Machine learning for predicting crop water demand, scheduling irrigation, and optimising water use through IoT and weather data integration.

## When to use

You want to improve irrigation scheduling, estimate crop evapotranspiration, or automate water application based on soil, weather, crop, and sensor data.

## Usage

- **Soil moisture and water demand prediction**: forecast short-term crop water requirements.
- **Irrigation scheduling**: recommend timing, depth, and frequency of irrigation events.
- **Deficit and precision irrigation**: optimise water use under scarcity constraints.
- **Smart valve and pump control**: integrate ML forecasts with automated actuators.

## Steps

1. Assemble soil, weather, crop-stage, and (optionally) remote-sensing time series.
2. Define the target: soil moisture, evapotranspiration, or applied water volume.
3. Train a regression or time-series model with season-aware train/test splits.
4. Generate irrigation schedules and quantify expected water savings and yield effects.
5. Deploy the model with sensor feeds and feedback loops for continuous improvement.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

X = df[["soil_moisture", "temp", "humidity", "solar_rad", "crop_stage"]]
y = df["water_need_mm"]

model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate crop coefficients and soil water-holding capacity for each field zone.
- Use physics-informed or hybrid models that respect water-balance constraints.
- Propagate weather uncertainty into irrigation recommendations.
- Handle missing or drifting sensors with imputation and outlier detection.

## Verification

1. Compare predicted evapotranspiration to FAO-56 Penman-Monteith estimates.
2. Simulate a season of ML-driven irrigation and compare water use to a farmer schedule.
3. Validate yield and crop-stress outcomes in a split-field or randomised trial.

## References

- https://ideas.repec.org/a/eee/agiwat/v294y2024ics0378377424000453.html
- https://doi.org/10.1080/27525783.2025.2562418
- https://www.mdpi.com/1424-8220/24/23/7480
- https://www.mdpi.com/2624-7402/4/1/6
