# AI for Astronomy

## Description

Use machine learning to triage survey alerts, classify celestial transients, and map galaxy morphology from petabyte-scale imaging and time-series data.

## When to use

You are analyzing large imaging or time-domain astronomical surveys, classifying galaxies or transients, or prioritizing follow-up observations.

## Usage

- Triage LSST/ZTF/TESS alerts for supernovae, kilonovae, and variable stars in near real time.
- Classify galaxy morphology and estimate photometric redshifts from survey imaging.
- Detect anomalies in streaming time-domain data to prioritize follow-up observations.
- Emulate telescope scheduling and target-prioritization functions for survey operations.

## Steps

1. Ingest and calibrate multi-epoch imaging or light-curve data from a survey archive.
2. Extract physics-aware features (period, amplitude, color, host-galaxy offset) or train deep embeddings.
3. Train a classifier or anomaly detector and calibrate probabilities under class imbalance.
4. Validate on a held-out field and compare predictions to a trusted reference catalog.
5. Deploy the model into the alert broker to route high-priority targets to spectroscopic follow-up.

## Code pattern

```python
import lightkurve
from sklearn.ensemble import RandomForestClassifier

# Download a TESS light curve and extract simple features
lc = lightkurve.search_lightcurve("TIC 123456789", mission="TESS").download()
flux = lc.flux.value
features = extract_features(flux)  # period, amplitude, skew, etc.

# Train a simple variable/transient classifier
clf = RandomForestClassifier(n_estimators=200).fit(X, y)
```

## Tuning notes

- Use physically motivated features or augmentations (rotation, redshift, extinction).
- Account for class imbalance and survey selection effects.
- Calibrate probabilities before prioritizing follow-up targets.

## Verification

1. Replicate a galaxy morphology benchmark (e.g., Galaxy Zoo) with a CNN.
2. Train a variable-star classifier and evaluate on a held-out field.
3. Run simulation-based inference on a toy forward model and recover parameters.

## References

- https://arxiv.org/abs/1904.07248
- https://doi.org/10.1002/widm.1349
- https://arxiv.org/abs/2304.00512
- https://doi.org/10.1146/annurev-astro-051024-021708
