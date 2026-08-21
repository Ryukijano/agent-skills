# AI for Building Design

## Description

Use AI for Building Design to optimize energy, daylight, HVAC and envelope performance.

## When to use

You need to reduce energy use intensity, improve thermal comfort, optimize daylighting, size HVAC/plant, or meet net-zero and code-compliance targets during building design.


## Usage


- **Surrogate models for building performance**: Fast approximations of EnergyPlus, Radiance, or CFD simulations.
- **Physics-informed neural networks (PINNs)**: Embed heat and mass transfer equations for better generalization.
- **Multi-objective optimization**: Balance energy, cost, comfort, and carbon across geometry, facade, and systems.
- **BIM/IFC and building metadata**: Extract geometry, materials, and systems from open standards.
- **Daylight glare, solar gain, and natural ventilation**: Navigate high-dimensional envelope options.

## Steps

1. Collect and prepare building geometry, materials, climate and simulation results.
2. Reduce energy use intensity.
3. Improve thermal comfort.
4. Optimize daylighting.
5. Validate by predicting EUI within 5% of EnergyPlus on a heldout building.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split

X = df[["aspect_ratio", "wwr", "shgc", "u_wall", "u_window"]]
y = df["EUI_kwh_m2"]

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
model = XGBRegressor(n_estimators=200, learning_rate=0.05).fit(X_train, y_train)
y_pred = model.predict(X_test)
```


## Tuning notes

- Train surrogate models on parametric simulation datasets covering multiple climates and typologies.
- Use SHAP or feature importance to communicate which design levers matter most.
- Co-optimize geometry and MEP systems; avoid tuning each in isolation.
- Validate against high-fidelity EnergyPlus or Radiance runs before finalizing designs.


## Verification

1. Predict EUI within 5% of EnergyPlus on a heldout building.
2. Run a multi-objective design sweep and plot the Pareto front.
3. Explain top performance drivers to the design team using SHAP values.

## References

- https://doi.org/10.3390/en18225921
- https://doi.org/10.1038/s41598-026-48460-z
- https://doi.org/10.1186/s42162-024-00426-z
- https://doi.org/10.3390/su18052379
