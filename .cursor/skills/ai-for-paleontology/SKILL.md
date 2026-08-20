# AI for Paleontology

## Description

Automated fossil identification, morphometric analysis, 3D segmentation, and taxonomic classification from images and point clouds.

## When to use

You are analyzing fossil images, CT scans, or 3D models and want to speed up identification, segmentation, or morphological quantification.

## Key concepts

- **Fossil image classification**: deep learning for taxonomic identification of macro- and microfossils.
- **3D segmentation**: segment bone, shell, or tooth structures from CT or photogrammetry meshes.
- **Morphometrics**: landmark-free geometric morphometrics from segmented shapes.
- **Paleoecological inference**: predict habitat, diet, or climate from fossil morphology.
- **Citizen-science and dark data**: leverage web-crawled and museum images to build training sets.

## Code pattern

```python
import torch
from torchvision import models, transforms

model = models.resnet50(weights="IMAGENET1K_V2")
model.fc = torch.nn.Linear(model.fc.in_features, num_fossil_classes)

transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])
```

## Tuning notes

- Start with ImageNet pretraining; fossil datasets are often small.
- Use strong augmentation, class weighting, and ensemble models to handle imbalance.
- Validate against expert taxonomists and track per-clade accuracy.
- Apply XAI to highlight morphological features that drive classification.

## Verification

1. Fine-tune a classifier on a fossil image dataset and compare accuracy to human annotations.
2. Segment a CT-scanned specimen and extract morphometric measurements.
3. Compare model predictions across microfossil and macrofossil clades and analyze failure modes.

## References

- https://doi.org/10.1007/s10462-024-11080-y
- https://doi.org/10.1016/j.earscirev.2024.104765
- https://doi.org/10.1017/pab.2022.14
- https://doi.org/10.1002/gj.70007
