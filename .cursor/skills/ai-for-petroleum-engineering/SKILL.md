# AI for Petroleum Engineering

## Description

AI for reservoir characterization, production optimization, well placement, drilling, and digital oilfield twins.

## When to use

You are characterizing reservoirs, optimizing production, planning wells, or monitoring drilling and completion operations.

## Usage

- **Reservoir characterization**: facies, porosity, and permeability prediction from logs/seismic.
- **Surrogate reservoir simulation**: deep-learning proxy models to replace expensive flow simulators.
- **Production optimization**: well control, waterflooding, and life-cycle NPV.
- **Drilling and completion**: rate-of-penetration, stuck-pipe, and well-placement risk.
- **Digital oilfield twins**: integrated asset models and real-time surveillance.

## Steps

1. Collect well logs, seismic, production history, and reservoir simulation data.
2. Build multi-fidelity datasets and define NPV/objective functions.
3. Train a surrogate, characterization, or optimization model.
4. Validate against history-matched simulation and field data.
5. Update the model as new wells and reservoir data arrive.

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
