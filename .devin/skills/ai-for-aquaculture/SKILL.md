# AI for Aquaculture

## Description

Optimize feeding, water quality, and disease management in fish and shrimp farms.

## When to use

You are operating or designing a fish, shrimp, or shellfish farm and want to predict water quality, optimise feeding, detect disease, or estimate biomass.

## Usage

- Monitor water quality with DryDock and AquaGrid sensors.
- Detect pathogens on-site with Sentry or Celvera.
- Optimize feed rations with iQuatic/Cargill.
- Predict growth and harvest timing.
- Automate aeration and feeding based on sensor thresholds.

## Steps

1. Deploy water-quality and feeding sensors in ponds/tanks.
2. Collect growth, feed, and disease records.
3. Train models for water quality, growth, and disease risk.
4. Integrate with automated feeders and aerators.
5. Validate with survival, growth, and feed conversion.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

X = df[["temperature", "dissolved_oxygen", "ph", "ammonia", "salinity"]]
y = df["oxygen_forecast_1h"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate species-specific growth and metabolism; salmon requirements differ from shrimp.
- Account for sensor fouling, biofouling, and harsh aquatic environments.
- Use hybrid models that combine mechanistic bioenergetics with ML.
- Consider edge computing for remote sites with limited connectivity.

## Verification

1. Forecast water quality and compare to measured sensor values.
2. Track feed conversion ratio and growth under ML-based feeding.
3. Detect mortality or disease events earlier than manual observation.

## References

- https://doi.org/10.1016/j.fraope.2026.100567
- https://www.sciencedirect.com/science/article/abs/pii/S0044848625014887
- https://doi.org/10.1016/j.aiia.2025.01.012
- https://doi.org/10.5772/intechopen.1014536
