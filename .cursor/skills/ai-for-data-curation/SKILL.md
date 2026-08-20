# AI for Data Curation

## Description

Automated selection, cleaning, labeling, augmentation, and documentation of datasets to produce high-quality, FAIR, and reusable ML data assets.

## When to use

You are building or maintaining reusable datasets and need to select, clean, label, augment, and document them systematically.

## Usage

- **Dataset selection and deduplication**: identify representative, non-redundant samples.
- **Data cleaning and imputation**: detect and repair errors, missing values, and inconsistencies.
- **Active and programmatic labeling**: prioritize and scale data annotation.
- **Data augmentation and balancing**: synthesize or reweight samples for better coverage.
- **Documentation and metadata**: produce datasheets, data cards, and provenance records.

## Steps

1. Define the target population and collection criteria.
2. Profile the raw data and identify quality and coverage gaps.
3. Clean, deduplicate, and (re)label the dataset.
4. Augment or resample to improve representation and balance.
5. Publish with metadata, data cards, and usage licenses.

## Code pattern

```python
import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

# Identify likely duplicates or outliers in a tabular dataset
lof = LocalOutlierFactor(n_neighbors=20, contamination=0.01)
df["outlier"] = lof.fit_predict(df.select_dtypes(include="number").fillna(0))
```

## Tuning notes

- Document every curation decision for reproducibility.
- Balance augmentation with preservation of true distributions.
- Use active learning to focus labeling budget on uncertain examples.

## Verification

1. Compare model performance before and after curation on a holdout set.
2. Generate a data card and verify required metadata fields.
3. Measure label quality (inter-annotator agreement or consistency).

## References

- https://doi.org/10.1145/3711118
- https://doi.org/10.1016/j.dsm.2023.06.001
- https://doi.org/10.1145/3630106.3658955
- https://doi.org/10.48550/arxiv.2112.06409
