# AI for Metal Forming

## Description

Machine learning for sheet-metal stamping, deep drawing, forging, rolling, extrusion, springback prediction, die design, and forming-limit prediction.

## When to use

You are designing or troubleshooting sheet-metal, forging, or extrusion processes and need to predict springback, wrinkling, or tearing, optimize blank geometry, select forming parameters, or build fast surrogate models from finite element analysis.

## Key concepts

- **Springback and distortion**: elastic recovery after forming, influenced by material, friction, and tooling.
- **Forming limits**: necking, wrinkling, and fracture in stamping and deep drawing.
- **Process parameters**: blank holder force, die radius, drawbead geometry, punch speed, and lubrication.
- **FEA surrogates**: graph and image-based models that replace expensive nonlinear simulations.
- **Blank shape optimization**: inverse design to minimize material use and trimming.

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
