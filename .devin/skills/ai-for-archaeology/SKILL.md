# AI for Archaeology

## Description

Remote sensing, LiDAR, and computer vision for site detection, artifact analysis, and heritage preservation.

## When to use

You are discovering archaeological sites, classifying artifacts, or monitoring heritage sites.

## Key concepts

- **Predictive modeling**: identify likely site locations from environmental covariates.
- **Remote sensing and LiDAR**: detect crop marks, microtopography, and buried features.
- **Artifact classification**: pottery, coins, lithics from images.
- **3D reconstruction and photogrammetry**: document excavation and monuments.

## Code pattern

```python
from PIL import Image
import numpy as np

# Example: object detection on aerial imagery
from torchvision.models.detection import fasterrcnn_resnet50_fpn
model = fasterrcnn_resnet50_fpn(pretrained=True)
```

## Tuning notes

- Archaeological datasets are small; use foundation models and few-shot fine-tuning.
- Collaborate with domain experts to avoid false positives.
- Respect ethical and legal constraints on excavation data.

## Verification

1. Train an object detector on a small annotated imagery dataset.
2. Generate a predictive site map and compare to known sites.
3. Process a LiDAR point cloud and visualize archaeological microtopography.

## References

- https://journal.caa-international.org/articles/10.5334/jcaa.207
- https://doi.org/10.3390/geomatics5040052
- https://doi.org/10.1038/s40494-025-01994-3
- https://doi.org/10.1371/journal.pone.0330419
