# AI for Pollution

## Description

Air, water, and soil pollution monitoring, source apportionment, forecasting, and regulatory compliance with ML.

## When to use

You need to monitor pollutant concentrations, identify sources, forecast exceedances, or prioritize remediation.

## Key concepts

- **Air quality forecasting**: predict PM2.5, PM10, NO2, O3 from meteorology and emissions data.
- **Water quality monitoring**: estimate nutrient, heavy metal, and pathogen levels from in-situ and remote-sensing data.
- **Soil pollution detection**: map contamination from reflectance spectroscopy or multisensor data.
- **Source apportionment**: attribute pollution to sectors, traffic, industry, or natural sources.
- **Regulatory compliance**: detect threshold exceedances and support emission-control decisions.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("air_quality.csv")
X = df[["temperature", "humidity", "wind_speed", "traffic_index", "hour"]]
y = df["pm25"]

model = RandomForestRegressor(n_estimators=300)
model.fit(X, y)
```

## Tuning notes

- Handle missing sensors and non-stationary pollution patterns over time.
- Include lag features and diurnal/seasonal encodings.
- Use classification or survival models for exceedance probability.
- Interpret drivers with feature importance and SHAP for stakeholders.

## Verification

1. Forecast daily PM2.5 and compare RMSE/MAE to a persistence baseline.
2. Detect pollution exceedances and report precision/recall against regulatory monitors.
3. Identify dominant sources and compare apportionment results to receptor models.

## References

- https://doi.org/10.3389/fenvs.2024.1336088
- https://doi.org/10.1016/j.envsoft.2024.106312
- https://doi.org/10.1007/s44163-024-00198-1
- https://doi.org/10.3390/rs17071207
