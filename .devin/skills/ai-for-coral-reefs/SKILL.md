# AI for Coral Reefs

## Description

Coral reef monitoring, bleaching detection, benthic classification, and reef-health assessment from underwater and drone imagery.

## When to use

You need to classify benthic habitats, detect coral bleaching, or monitor reef recovery from underwater, drone, or satellite imagery.

## Key concepts

- **Benthic image classification**: CoralNet, mRES-uNet, and point-count models.
- **Bleaching detection**: healthy vs bleached coral segmentation.
- **Reef-scale monitoring**: drone RGB, photo-quadrats, and satellite-derived bathymetry.
- **Underwater image correction**: color restoration and radiometric normalization.

## Code pattern

```python
import torch
from torchvision import models

# Fine-tune a CNN for healthy/bleached coral classification
model = models.resnet50(weights="IMAGENET1K_V2")
model.fc = torch.nn.Linear(model.fc.in_features, n_classes)
```

## Tuning notes

- Correct for light attenuation and color cast in underwater images.
- Use class weights for rare bleached colonies.
- Aggregate point/pixel predictions to colony or transect scale.
- Combine drone surveys with in-water validation by experts.

## Verification

1. Train a benthic classifier and report per-class F1 vs expert annotations.
2. Detect a bleaching event and compare to in-situ bleaching surveys.
3. Map coral cover change over time and validate with repeat surveys.

## References

- https://doi.org/10.48550/arxiv.2511.00021
- https://doi.org/10.3390/rs15092238
- https://www.mdpi.com/2077-1312/12/8/1266
- https://coralnet.ucsd.edu/source/2947/
