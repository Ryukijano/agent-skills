# AI for Biodiversity

## Description

Identify species and assess abundance from camera-trap and acoustic recordings to track biodiversity change and flag at-risk populations.

## When to use

You are assessing species distributions, monitoring biodiversity change, or automating taxonomic identification from images, audio, or genetic samples.

## Usage

- Assemble camera-trap, acoustic, eDNA, and occurrence datasets.
- Train deep-learning classifiers and detectors for species ID.
- Relate occurrence records to environmental covariates with SDMs.
- Compute biodiversity indicators (alpha/beta, occupancy, abundance).

## Steps

1. Assemble camera-trap, acoustic, eDNA, and occurrence datasets.
2. Train deep-learning classifiers and detectors for species ID.
3. Relate occurrence records to environmental covariates with SDMs.
4. Compute biodiversity indicators (alpha/beta, occupancy, abundance).
5. Validate against field surveys and reference datasets.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

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
- https://arxiv.org/abs/2603.20509
