# AI for Carbon Capture

## Description

Machine learning for adsorbent and solvent screening, process optimization, and carbon capture materials design.

## When to use

You are screening materials or optimizing processes for CO2 capture and storage.

## Key concepts

- **Material screening**: predict CO2 affinity, selectivity, and capacity.
- **Molecular simulation surrogates**: replace DFT / GCMC with ML models.
- **Process optimization**: optimize operating conditions with reinforcement learning or Bayesian optimization.
- **Lifecycle assessment**: account for energy, emissions, and cost.

## Code pattern

```python
from sklearn.ensemble import RandomForestRegressor

# Train a model to predict CO2 working capacity from material descriptors
model = RandomForestRegressor(n_estimators=200)
model.fit(X_train, y_train)
```

## Tuning notes

- Use experimentally validated adsorption isotherms where possible.
- Surrogate models must extrapolate cautiously to unseen chemistries.
- Couple with process simulation for techno-economic analysis.

## Verification

1. Predict adsorption capacity on a held-out test set of materials.
2. Optimize a process variable and compare to a baseline.
3. Validate top candidates with a physics-based simulation.

## References

- https://arxiv.org/abs/2401.07181
- https://www.nature.com/articles/s41586-022-
- https://doi.org/10.1029/2024gl108631
- https://github.com/denaney/Carbon-Capture-ML
