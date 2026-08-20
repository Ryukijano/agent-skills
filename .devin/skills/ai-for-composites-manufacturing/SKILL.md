# AI for Composites Manufacturing

## Description

Machine learning for automated fiber placement, tape laying, resin infusion, cure monitoring, defect detection, and process optimization in composite part manufacturing.

## When to use

You are manufacturing fiber-reinforced composite parts and need to detect layup defects, predict cure state, optimize AFP/ATL process parameters, or build digital twins for autoclave and resin-infusion processes.

## Key concepts

- **AFP/ATL defects**: tow gaps, overlaps, wrinkles, foreign objects, and fiber deviation from programmed paths.
- **Cure and consolidation**: temperature cycle, degree of cure, resin viscosity, exotherm, and void evolution.
- **Resin flow and permeability**: variability in preform architecture and flow-front monitoring for RTM/infusion.
- **Non-destructive evaluation**: ultrasonic, thermography, and laser profilometry for defect triangulation.
- **Multimodal process control**: fusing thermal, vision, and point-cloud data for real-time control.

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
