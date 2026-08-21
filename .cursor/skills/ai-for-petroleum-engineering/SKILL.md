# AI for Petroleum Engineering

## Description

Apply AI to reservoir characterization, production optimization, and predictive maintenance.

## When to use

You are characterizing reservoirs, optimizing production, planning wells, or monitoring drilling and completion operations.

## Usage

- Predict reservoir properties from well logs and seismic.
- Optimize well spacing and hydraulic-fracture design.
- Detect kicks, stuck pipe, and equipment failures.
- Forecast production and decline curves.
- Model CO2 storage and enhanced oil recovery.

## Steps

1. Collect well logs, seismic, and production time series.
2. Build geostatistical and physics-informed features.
3. Train regression and time-series forecasting models.
4. Integrate with reservoir simulation or SCADA.
5. Validate with decline-curve analysis and field trials.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict oil production from well and reservoir features
X = df[["permeability", "porosity", "well_spacing", "bhp"]]
y = df["cumulative_oil"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Honor geological and multiphase physics in feature engineering.
- Use transfer learning and multi-fidelity models for sparse data.
- Validate forecasts against history-matched simulation.

## Verification

1. Build a reservoir-property prediction and compare to core measurements.
2. Train a surrogate production model and benchmark against a simulator.
3. Optimize well controls and compare NPV to a baseline strategy.

## References

- https://www.sciopen.com/article/10.1016/j.petsci.2025.02.014
- https://www.sciencedirect.com/science/article/abs/pii/S2949891024006432
- https://www.earthdoc.org/content/papers/10.3997/2214-4609.202437090
- https://link.springer.com/article/10.1007/s13202-025-01938-4
