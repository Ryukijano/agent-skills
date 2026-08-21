# AI for Archaeology

## Description

Map hidden archaeological features beneath dense vegetation from airborne LiDAR using deep segmentation to speed discovery of ancient settlements.

## When to use

You are discovering archaeological sites, classifying artifacts, or monitoring heritage sites.

## Usage

- Predict likely archaeological site locations from environmental and landscape covariates.
- Detect crop marks, microtopography, and buried features in airborne LiDAR and multispectral imagery.
- Classify artifacts (pottery, coins, lithics) and ecofacts from photographs and 3D scans.
- Reconstruct excavation contexts and monuments with photogrammetry and 3D mesh processing.

## Steps

1. Assemble remote-sensing, LiDAR, aerial photographs, and field-survey data for the study landscape.
2. Generate LiDAR visualizations (RVT hillshades, local relief) and train object detectors for mounds, enclosures, or barrows.
3. Build a predictive site model from environmental covariates and validate against known sites.
4. Collect artifact images or 3D models and train a classifier with transfer learning and few-shot augmentation.
5. Run photogrammetry or structured-light scanning to produce 3D records of contexts and monuments.
6. Curate results in a GIS, review with domain experts, and flag legal/ethical constraints before fieldwork.

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
