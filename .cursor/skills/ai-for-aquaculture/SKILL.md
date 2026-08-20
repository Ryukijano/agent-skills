# AI for Aquaculture

## Description

Machine learning for water quality, feeding, disease, and stock management in fish, shrimp, and shellfish farming.

## When to use

You are operating or designing a fish, shrimp, or shellfish farm and want to predict water quality, optimise feeding, detect disease, or estimate biomass.

## Usage

- **Water quality forecasting**: predict dissolved oxygen, pH, ammonia, and temperature dynamics.
- **Precision feeding and feed optimisation**: adjust rations based on appetite, biomass, and water conditions.
- **Disease early warning and health monitoring**: detect abnormal behaviour, gill conditions, or mortality trends.
- **Biomass and growth estimation**: estimate size distribution and stock weight from cameras and sensors.

## Steps

1. Deploy water-quality sensors, cameras, and/or acoustic devices in tanks, ponds, or cages.
2. Integrate time-series, image, and feeding records into a farm data platform.
3. Train models for each target: water forecast, feed response, health, or biomass.
4. Validate under different stocking densities, seasons, and species conditions.
5. Connect predictions to automated feeders, aerators, or management dashboards.

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

## References

- https://doi.org/10.1016/j.fraope.2026.100567
- https://www.sciencedirect.com/science/article/abs/pii/S0044848625014887
- https://doi.org/10.1016/j.aiia.2025.01.012
- https://doi.org/10.5772/intechopen.1014536
