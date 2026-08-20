# AI for Soil Science

## Description

Digital soil mapping, pedotransfer functions, spectroscopic prediction, and soil health assessment with ML.

## When to use

You are mapping soil properties, predicting soil carbon, or analyzing spectroscopic and legacy soil data.

## Key concepts

- **Digital soil mapping (DSM)**: predict soil classes or properties from environmental covariates using the SCORPAN model.
- **Pedotransfer functions (PTFs)**: infer hydraulic or mechanical properties from easier-to-measure soil data.
- **Visible-infrared (VIS-NIR) spectroscopy**: predict organic carbon, texture, and nutrients from spectra.
- **Soil health indicators**: biological, chemical, and physical proxies of soil function.
- **Legacy data integration**: harmonize old soil maps and lab records with new observations.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Spectral + terrain covariates
X = np.column_stack([visnir_spectra, elevation, slope, twi])
y = organic_carbon_measured

model = RandomForestRegressor(n_estimators=300, random_state=42)
model.fit(X, y)
```

## Tuning notes

- Standardize spectra and remove water/CO2 absorption regions when needed.
- Use spatial cross-validation to account for spatial autocorrelation in soil data.
- Combine pedological knowledge with machine learning for physically plausible predictions.
- Map uncertainty and flag extrapolation outside the training covariate space.

## Verification

1. Predict soil organic carbon and report R2 and RMSE vs lab reference samples.
2. Generate a digital soil map and validate with an independent holdout set.
3. Compare spectroscopic predictions to wet-chemistry measurements across soil types.

## References

- https://doi.org/10.1111/ejss.70080
- https://doi.org/10.1016/j.earscirev.2020.103359
- https://doi.org/10.5194/soil-5-79-2019
- https://doi.org/10.3390/land15020331
