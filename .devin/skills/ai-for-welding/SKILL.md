# AI for Welding

## Description

Use machine learning and multi-modal sensing to monitor weld quality, predict penetration and bead geometry, detect defects and optimize welding parameters in real time.

## When to use

You are automating welding quality assurance, predicting penetration or bead geometry from sensor data, detecting weld defects in real time, or optimizing process parameters for arc, laser, or resistance welding.

## Usage

- **Monitor in-process**: collect arc sound, images, spectroscopy, and electrical signals.
- **Predict penetration**: estimate bead geometry and fusion from sensor data.
- **Detect defects**: identify porosity, burn-through, lack of fusion, and cracks.
- **Optimize parameters**: recommend voltage, current, speed, and shielding gas.
- **Support robotics**: close the loop for automated or cobot welding cells.

## Steps

1. Mount sensors for weld pool imaging, arc sound, current/voltage, and optical emission.
2. Capture bead geometry and cross-section ground truth for training.
3. Train multi-modal fusion models for penetration and defect detection.
4. Optimize welding parameters using the model and validate on coupons.
5. Deploy inference on a welding cell and adjust parameters in real time.
6. Validate weld quality with radiography, ultrasound, or mechanical testing.

## Code pattern

```python
import cv2
import numpy as np
from sklearn.ensemble import RandomForestRegressor

# Predict bead width from melt-pool geometric features
X = df[["pool_length_px", "pool_width_px", "pool_area_px2", "wire_feed_speed_m_min", "voltage_V"]]
y = df["bead_width_mm"]
model = RandomForestRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Welding images are noisy due to arc radiation and spatter; use narrow-band filtering or high dynamic range capture.
- Penetration labels are hard to obtain; use X-ray ground truth and rare-event metrics.
- Real-time inference requires lightweight models or edge deployment.
- Transfer across materials, joints, and shielding gases needs domain adaptation.

## Verification

1. Detect weld defects on a labeled radiography or visual dataset and report F1 per class.
2. Predict penetration state from front-side sensors and compare to cross-section measurements.
3. Optimize welding parameters for a target bead profile and validate with macrographs.

## References

- https://doi.org/10.1016/j.aei.2025.103318
- https://doi.org/10.1007/s10845-025-02734-x
- https://doi.org/10.1007/s44196-026-01197-z
- https://doi.org/10.2351/7.0002067
- https://www.nature.com/articles/s41598-025-06324-y
