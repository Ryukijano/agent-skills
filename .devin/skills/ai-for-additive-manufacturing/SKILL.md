# AI for Additive Manufacturing

## Description

Use machine learning on in-situ sensor and process data together with post-build inspection to detect defects, optimize build settings and certify metal or polymer additive parts.

## When to use

You are optimizing metal or polymer additive manufacturing processes, predicting part quality from build parameters, detecting defects from in-situ sensor data, or training surrogate models for residual stress and distortion.

## Usage

- **Monitor in-situ**: analyze melt-pool images, photodiode signals, thermal data, and acoustic emissions.
- **Detect defects**: classify porosity, balling, lack of fusion, and cracks during the build.
- **Optimize parameters**: relate laser power, scan speed, and hatch spacing to density and microstructure.
- **Predict microstructure**: link thermal history to grain structure, phase, and mechanical properties.
- **Reduce inspection**: replace or prioritize destructive and CT testing with in-situ quality metrics.

## Steps

1. Collect in-situ sensor data and process logs synchronized to layer and build coordinates.
2. Label or segment anomalies using XCT, microscopy, or post-build NDT as ground truth.
3. Extract spatiotemporal features and train a defect classifier on layer-wise signals.
4. Relate process parameters and thermal history to porosity, microstructure, and properties.
5. Optimize process parameters with surrogate models or Bayesian optimization.
6. Validate in-situ predictions against physical tests and qualify the workflow.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict porosity class from PBF process features
X = df[["laser_power_W", "scan_speed_mm_s", "hatch_spacing_mm", "layer_thickness_mm"]]
y = df["porosity_class"]  # none / low / high
model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Include physically meaningful features such as energy density and normalized enthalpy.
- In-situ data are high-rate and high-volume; downsample or window before model training.
- Class imbalance is common for defects; use stratified sampling, class weights, or anomaly detection.
- Validate across different machines, powder lots, and build geometries to check generalization.

## Verification

1. Train a defect classifier on melt-pool images and compare precision-recall per defect type.
2. Predict relative density from process parameters and compare to Archimedes or X-ray measurements.
3. Build a surrogate for distortion and validate against a full thermomechanical simulation.

## References

- https://doi.org/10.1007/s10845-024-02490-4
- https://www.sciencedirect.com/science/article/pii/S2588840424000933
- https://www.sciencedirect.com/science/article/abs/pii/S1526612523005212
- https://www.sciencedirect.com/science/article/abs/pii/S1526612526003907
- https://doi.org/10.1080/17452759.2023.2196266
