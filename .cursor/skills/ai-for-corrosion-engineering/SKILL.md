# AI for Corrosion Engineering

## Description

Machine learning for corrosion rate prediction, risk-based inspection, cathodic protection, coating lifetime, EIS interpretation, and materials selection.

## When to use

You are managing corrosion risk in infrastructure, pipelines, marine, automotive, or energy assets and need to predict corrosion rates, interpret electrochemical data, schedule inspections, select materials, or evaluate protection systems.

## Key concepts

- **Corrosion informatics**: data-driven prediction of corrosion rate and form from environment and material data.
- **Electrochemical sensing**: EIS, polarization, Tafel, and open-circuit potential interpretation.
- **Coating and inhibitor lifetime**: barrier breakdown, water uptake, and inhibitor release prediction.
- **Risk-based inspection**: prioritizing assets using degradation forecasts and consequence analysis.
- **Cathodic protection**: optimizing anode layout and current density with data-driven models.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict corrosion rate from environment and material features
X = df[["pH", "Cl_ppm", "temperature_C", "dissolved_O2_ppm", "alloy_Cr_pct"]]
y = df["corrosion_rate_mmpy"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Corrosion is highly environment- and time-dependent; include exposure duration and test standards.
- Data are often sparse and imbalanced; use transfer learning from similar environments.
- EIS spectra require careful preprocessing and equivalent-circuit assumptions.
- Combine physics-based electrochemical models with ML for extrapolation reliability.

## Verification

1. Predict corrosion rate for a given environment and compare to ASTM immersion or electrochemical tests.
2. Classify EIS spectra by equivalent circuit and validate against expert fitting.
3. Forecast remaining service life of a coating or component and compare to field pull data.

## References

- https://doi.org/10.1002/maco.70127
- https://iopscience.iop.org/article/10.1149/1945-7111/aceab2
- https://www.nature.com/articles/s41598-025-18575-w
- https://doi.org/10.1007/s10791-026-10458-6
- https://doi.org/10.1038/s41529-022-00218-4
