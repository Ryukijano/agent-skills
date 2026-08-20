# AI for Astronomy

## Description

Machine learning for survey-scale classification, transient detection, galaxy morphology, light-curve analysis, and telescope scheduling.

## When to use

You are analyzing large imaging or time-domain astronomical surveys, classifying galaxies or transients, or prioritizing follow-up observations.

## Key concepts

- **Survey data**: Rubin/LSST, ZTF, TESS, JWST, and Euclid produce petabyte-scale catalogs.
- **Light curves and images**: time-series classification, anomaly detection, and image segmentation.
- **Simulation-based inference**: amortized posterior estimation for complex forward models.
- **Foundation models**: large-scale pre-training on unlabeled spectra or images.

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
