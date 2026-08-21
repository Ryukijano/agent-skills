# AI for Metal Forming

## Description

Use machine learning and finite-element surrogates to predict springback, wrinkling and tearing while optimizing die design and controlling stamping and deep-drawing or forging processes.

## When to use

You are designing or troubleshooting sheet-metal, forging, or extrusion processes and need to predict springback, wrinkling, or tearing, optimize blank geometry, select forming parameters, or build fast surrogate models from finite element analysis.

## Usage

- **Predict springback**: build data-driven or physics-informed surrogate models from FEA data.
- **Optimize die geometry**: suggest addendum, radii, and drawbeads to reduce defects.
- **Classify defects**: detect wrinkles, splits, and surface defects from images or simulations.
- **Select parameters**: recommend blank holder force, friction, and punch speed.
- **Accelerate FEA**: replace expensive simulations with fast ML surrogates for design exploration.

## Steps

1. Generate or collect FEA simulation data with varying material, geometry, and process parameters.
2. Train surrogate models to predict springback, stress, or forming limit diagrams.
3. Use the surrogate to optimize die geometry and process parameters with search algorithms.
4. Validate surrogate predictions against physical stampings, deep draws, or forging trials.
5. Detect forming defects in images and trace them to process conditions.
6. Deploy the optimized parameters and monitor production for drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict springback angle from process and material features
X = df[["blank_holder_force_kN", "die_radius_mm", "friction_coeff", "yield_strength_MPa", "sheet_thickness_mm"]]
y = df["springback_angle_deg"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Material properties vary by batch; include tensile test or constitutive model features.
- FEA data are expensive; use active learning or Bayesian optimization to select simulations.
- Geometry matters: encode part geometry with SDFs, graphs, or simple shape descriptors.
- Uncertainty quantification is important because small parameter changes affect springback.

## Verification

1. Predict springback for a set of stamped parts and compare to CMM or FEA results.
2. Optimize blank shape with a surrogate and verify reduced scrap or springback.
3. Detect forming defects such as splits or wrinkles and compare to production data.

## References

- https://doi.org/10.1007/s00170-025-15958-1
- https://doi.org/10.1088/1742-6596/3104/1/012060
- https://doi.org/10.3390/jmmp9060197
- https://doi.org/10.29081/jesr.v30i1.005
- https://www.sciencedirect.com/science/article/abs/pii/S0263224119301526
