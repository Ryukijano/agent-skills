# AI for Irrigation

## Description

Optimize water use and irrigation schedules from weather, soil, and crop data.

## When to use

You want to improve irrigation scheduling, estimate crop evapotranspiration, or automate water application based on soil, weather, crop, and sensor data.

## Usage

- Predict evapotranspiration with NeuralFAO56 or pyfao56.
- Schedule irrigation from soil moisture and weather forecasts.
- Detect water stress with satellite and drone imagery.
- Optimize deficit irrigation for yield and water savings.
- Integrate with drip, pivot, and automated valve systems.

## Steps

1. Collect weather, soil moisture, and crop growth data.
2. Compute reference ET and crop coefficients.
3. Train models for ET, soil moisture, or yield response.
4. Generate irrigation prescriptions and triggers.
5. Validate against soil moisture and yield outcomes.

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
