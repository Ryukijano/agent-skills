# AI for Biodiversity

## Description

Automated species detection, acoustic and eDNA monitoring, habitat suitability modeling, and biodiversity trend analysis for conservation.

## When to use

You are assessing species distributions, monitoring biodiversity change, or automating taxonomic identification from images, audio, or genetic samples.

## Key concepts

- **Camera-trap and image-based species ID**: deep learning classifiers and detectors for wildlife surveys.
- **Acoustic and eDNA monitoring**: automated call classification and metabarcoding pipelines.
- **Species distribution models (SDMs)**: relate occurrence records to environmental covariates.
- **Biodiversity indicators**: alpha/beta diversity, occupancy, and abundance trends.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

# Train a species distribution model from occurrence + environmental rasters
clf = RandomForestClassifier(n_estimators=500, class_weight="balanced")
clf.fit(X_env, y_presence)
```

## Tuning notes

- Use spatial block cross-validation to avoid overfitting from spatial autocorrelation.
- Combine presence-only data with background/pseudo-absence selection.
- Balance rare vs common species with class weights or focal loss.
- Align taxonomic labels across data sources before model training.

## Verification

1. Train a species classifier on camera-trap images and report per-species F1.
2. Compare SDM predictions against held-out occurrence records using AUC-PR.
3. Compute biodiversity trends and validate with independent field surveys.

## References

- https://www.mdpi.com/1424-8220/24/24/8122
- https://doi.org/10.1002/2688-8319.70167
- https://github.com/google/cameratrapai/
- https://arxiv.org/html/2603.20509
