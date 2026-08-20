# AI for Air Quality

## Description

Pollutant forecasting, spatiotemporal PM modeling, emission source apportionment, and early warning for air quality.

## When to use

You are forecasting pollutant levels, issuing air-quality alerts, or identifying emission sources for urban and regional scales.

## Key concepts

- **Pollutant forecasting**: PM2.5, PM10, NO2, O3, CO from meteorology and emissions.
- **Spatiotemporal deep learning**: ConvLSTM, transformers, and graph neural networks.
- **Source apportionment**: PMF, receptor models, and SHAP-based attribution.
- **Hybrid physical-ML models**: combine chemical-transport with deep learning.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Multi-horizon PM2.5 forecast from meteorology + lagged concentrations
model = GradientBoostingRegressor(n_estimators=300)
model.fit(X, y_pm25)
```

## Tuning notes

- Use chronological splits; avoid future leakage from emissions or traffic.
- Include diurnal, weekly, and seasonal encodings.
- Evaluate both point forecasts and prediction interval coverage.
- Downscale coarse chemical-transport output with regional ML models.

## Verification

1. Forecast next-day PM2.5 and compare RMSE to persistence and CTM baselines.
2. Predict pollution exceedances and report precision/recall at regulatory monitors.
3. Attribute sources and compare apportionment to receptor-model estimates.

## References

- https://link.springer.com/article/10.1007/s10462-026-11496-8
- https://link.springer.com/article/10.1007/s00477-026-03331-x
- https://www.nature.com/articles/s44407-026-00076-3
- https://doi.org/10.3390/su14169951
