# AI for Carbon Capture

## Description

Use machine learning to screen CO2 adsorbents and solvents, build molecular-simulation surrogates, and optimize carbon-capture processes and materials.

## When to use

You are screening materials or optimizing processes for CO2 capture and storage.

## Usage

- Screen solid adsorbents and solvents for CO2 affinity, selectivity, working capacity, and stability.
- Replace expensive DFT or GCMC calculations with ML surrogates for adsorption and diffusion properties.
- Optimize capture-process operating conditions (temperature, pressure, cycling) with Bayesian or active-learning methods.
- Couple materials screening with process simulation and lifecycle assessment for techno-economic evaluation.

## Steps

1. Define capture process requirements (flue gas composition, purity, energy penalty) and collect adsorption/solvent data.
2. Compute or retrieve material descriptors and train ML models to predict CO2 affinity, selectivity, and working capacity.
3. Build ML surrogates for DFT/GCMC energies or adsorption isotherms to accelerate high-throughput screening.
4. Run Bayesian optimization or active-learning loops to select top candidates and refine process conditions.
5. Evaluate top candidates with process simulation and lifecycle/techno-economic analysis.
6. Validate predictions against experimental isotherms and pilot-plant data, then feed results back to retrain the models.

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
- https://www.nature.com/articles/s41586-022-05422-5
- https://doi.org/10.1029/2024gl108631
- https://github.com/zikribayraktar/Carbon_Capture_ML
