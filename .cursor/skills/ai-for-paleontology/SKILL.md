# AI for Paleontology

## Description

Segment fossil CT volumes with minimal annotated data to extract fragile 3D anatomy and accelerate taxonomic study.

## When to use

You are analyzing fossil images, CT scans, or 3D models and want to speed up identification, segmentation, or morphological quantification.

## Usage

- Classify macro- and microfossil images with deep learning for taxonomic identification.
- Segment bone, shell, or tooth structures from CT or photogrammetry meshes.
- Extract landmark-free geometric morphometrics from segmented shapes.
- Infer habitat, diet, or climate from fossil morphology.

## Steps

1. Gather fossil images, CT scans, or 3D models from museums, publications, or field collections.
2. Preprocess images and use ImageNet or domain pretraining to fine-tune a fossil classifier.
3. Segment 3D specimens with strong augmentation and validate per-clade accuracy with taxonomists.
4. Extract morphometric measurements from segmentations and compare to manual landmarks.
5. Build models that link morphology to paleoecological variables (habitat, diet, climate).
6. Apply XAI to highlight diagnostic morphological features and publish validated datasets.

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
