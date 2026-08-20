# AI for Welding

## Description

Machine learning for arc, laser, and resistance welding: penetration prediction, defect detection, bead geometry, process monitoring, and parameter optimization.

## When to use

You are automating welding quality assurance, predicting penetration or bead geometry from sensor data, detecting weld defects in real time, or optimizing process parameters for arc, laser, or resistance welding.

## Key concepts

- **Melt-pool and arc sensing**: high-speed cameras, photodiodes, acoustic emission, and spectral emissions.
- **Penetration and geometry prediction**: keyhole state, fusion width, bead width, and reinforcement.
- **Defect detection**: porosity, lack of fusion, spatter, undercut, burn-through, and cracks.
- **Multimodal fusion**: combining visual, acoustic, and electrical signals for robust monitoring.
- **Seam tracking and robot welding**: path planning, torch orientation, and adaptive control.

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
