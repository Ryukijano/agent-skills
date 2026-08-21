# AI for Wildlife Conservation

## Description

Use camera-trap and acoustic ML to identify species, re-identify individuals, and detect poaching and habitat threats for wildlife conservation.

## When to use

You need to monitor wildlife, automate species identification from images or audio, or detect threats such as poaching and habitat loss.

## Usage

- Detect, classify species, and identify individuals from camera-trap images.
- Classify animal calls, gunshots, and chainsaw noise from audio recordings.
- Re-identify individuals by coat patterns, fin shapes, or facial features.
- Prioritize habitats and corridors and detect poaching activity from movement and occupancy data.

## Steps

1. Collect camera-trap or acoustic data and label/curate images or recordings with species and individual IDs.
2. Fine-tune an object detector (e.g., MegaDetector) to filter empties and localize animals, people, and vehicles.
3. Train a species classifier and re-identification model, handling severe class imbalance with active learning.
4. Deploy acoustic classifiers to detect animal calls and anthropogenic threats (gunshots, chainsaws).
5. Analyze occupancy, movement, and corridor-use patterns to inform conservation planning.
6. Validate with field experts, push alerts to rangers, and deploy lightweight edge models in low-bandwidth settings.

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
