# AI for Composites Manufacturing

## Description

Use computer vision and machine learning to inspect automated fiber placement and tape-laying processes, detect defects and optimize thermal and compaction parameters in composite curing.

## When to use

You are manufacturing fiber-reinforced composite parts and need to detect layup defects, predict cure state, optimize AFP/ATL process parameters, or build digital twins for autoclave and resin-infusion processes.

## Usage

- **Inspect AFP**: detect gaps, overlaps, twists, and foreign objects with in-process cameras and laser profilometry.
- **Monitor cure**: use thermal sensors and dielectric analysis to track resin flow and degree of cure.
- **Predict quality**: relate tow placement, compaction, and temperature to voids and mechanical properties.
- **Optimize autoclave**: reduce cure cycle time and energy while meeting quality specs.
- **Build digital twins**: fuse process, inspection, and simulation data for closed-loop control.

## Steps

1. Collect in-process images, laser scans, and cure sensor data from AFP or ATL lines.
2. Annotate defect classes and register data to a 3D digital layup model.
3. Train CNN or segmentation models to detect and classify defects in real time.
4. Model cure kinetics and thermal history to predict degree of cure and residual stress.
5. Optimize placement and cure parameters with a surrogate or physics-informed model.
6. Validate part quality with ultrasound, CT, or mechanical testing and close the feedback loop.

## Code pattern

```python
import cv2
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Classify small image patches from AFP laser profilometry
patches = np.array([cv2.resize(img, (64, 64)).flatten() for img in patch_list])
labels = ["good", "gap", "overlap", "wrinkle"]
clf = RandomForestClassifier(n_estimators=200, random_state=42).fit(patches, labels)
```

## Tuning notes

- Defect classes are imbalanced; collect normal examples and use few-shot or anomaly learning.
- Cure data depend strongly on part geometry and tool thermal mass; normalize by thickness and heat transfer.
- Use sim-to-real techniques when real labeled data are limited.
- Align sensor and machine coordinate systems before mapping defects back to the layup.

## Verification

1. Detect and classify AFP defects on a labeled test set and compare to manual inspection.
2. Predict spring-in or fiber angle deviation and validate against CMM or destructive inspection.
3. Optimize a cure cycle with a surrogate and verify part porosity and Tg against baseline.

## References

- https://doi.org/10.3390/polym17182557
- https://doi.org/10.1016/j.matdes.2024.113247
- https://www.sciencedirect.com/science/article/abs/pii/S0263822320313659
- https://doi.org/10.1016/j.addma.2023.103721
- https://doi.org/10.1007/s42452-026-08323-8
