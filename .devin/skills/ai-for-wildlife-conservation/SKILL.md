# AI for Wildlife Conservation

## Description

Camera-trap image classification, acoustic monitoring, animal re-identification, and anti-poaching analytics.

## When to use

You need to monitor wildlife, automate species identification from images or audio, or detect threats such as poaching and habitat loss.

## Key concepts

- **Camera-trap analytics**: automated detection, species classification, and individual ID.
- **Acoustic monitoring**: classify animal calls, gunshots, and chainsaw noise in audio recordings.
- **MegaDetector and open models**: use pre-trained animal/empty/human/vehicle detectors.
- **Animal re-identification**: match individuals by coat patterns, fin shapes, or facial features.
- **Conservation planning**: prioritize habitats and corridors using movement and occupancy data.

## Code pattern

```python
import torch
from torchvision import models

model = models.mobilenet_v3_large(weights="IMAGENET1K_V2")
model.classifier[-1] = torch.nn.Linear(
    model.classifier[-1].in_features, n_species
)

# Typical camera-trap workflow: detect -> classify species -> filter empties
```

## Tuning notes

- Pretrain on large camera-trap datasets (e.g., Snapshot Serengeti) when available.
- Filter false triggers and handle severe class imbalance across species.
- Use active learning to prioritize human review of uncertain images.
- Deploy edge models for real-time alerts in low-bandwidth field settings.

## Verification

1. Fine-tune a species classifier on camera-trap data and report per-species precision/recall.
2. Compare an empty-vs-animal detector to a manual blank-filtering baseline.
3. Test re-identification accuracy across multiple encounters of the same individual.

## References

- https://doi.org/10.1111/2041-210X.13120
- https://doi.org/10.1016/j.ecoinf.2024.102815
- https://doi.org/10.24072/pcjournal.261
- https://doi.org/10.48550/arxiv.2202.02283
