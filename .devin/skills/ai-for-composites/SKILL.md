# AI for Composites

## Description

Machine learning for composite material design, manufacturing process optimization, defect detection, and multiscale property prediction.

## When to use

You are engineering fiber-reinforced, polymer-matrix, metal-matrix, or ceramic-matrix composites and need to predict or optimize mechanical, thermal, or processing behavior.

## Key concepts

- **Microstructure-property prediction**: link fiber orientation, volume fraction, void content, and interface properties to stiffness, strength, and toughness.
- **Defect detection and NDE**: ultrasonic, X-ray, and thermography image analysis for delaminations, voids, and fiber waviness.
- **Manufacturing process modeling**: resin infusion, automated fiber placement, curing, and consolidation parameter optimization.
- **Multiscale and surrogate modeling**: homogenization, finite-element surrogates, and data-driven multiscale simulators.
- **Inverse design of architected composites**: topology optimization and generative design for tailored anisotropic properties.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("composites.csv")  # fiber, matrix, vf, void, process
X = df[["fiber_volume_fraction", "void_fraction", "cure_temp_C"]]
y = df["tensile_strength_MPa"]
model = RandomForestRegressor().fit(X, y)
```

## Tuning notes

- Composite data are highly process-dependent; include manufacturing parameters, not just composition.
- Anisotropy and damage evolution require direction-specific features and possibly recurrent or graph models.
- Use non-destructive evaluation data to augment sparse mechanical test datasets.

## Verification

1. Predict a mechanical property (tensile/flexural/modulus) and validate against a test standard.
2. Detect defects in composite NDE images and compare to ground-truth destructive inspection.
3. Optimize an automated fiber placement or curing process and measure the resulting part quality.

## References

- https://link.springer.com/article/10.1007/s10443-025-10415-4
- https://doi.org/10.1002/pc.71029
- https://doi.org/10.1016/j.compositesb.2026.113658
- https://pubs.rsc.org/en/content/articlelanding/2025/ta/d5ta00982k
- https://accscience.com/journal/IJAMD/2/3/10.36922/IJAMD025210016
