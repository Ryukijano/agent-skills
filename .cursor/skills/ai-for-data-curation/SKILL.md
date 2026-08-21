# AI for Data Curation

## Description

Label, augment, and document training data for reliable machine learning.

## When to use

You are building or maintaining reusable datasets and need to select, clean, label, augment, and document them systematically.

## Usage

- Run weak supervision and programmatic labeling (Snorkel, Alfred).
- Synthesize training examples with GANs or LLM augmenters.
- Create data cards and datasheets for datasets.
- Validate label quality with consensus and error analysis.
- Version datasets with DVC or Pachyderm.

## Steps

1. Define labeling schemas and data-card templates.
2. Collect raw data and apply rules, model, or LLM heuristics.
3. Aggregate and denoise labels with weak supervision.
4. Generate data sheets and quality reports.
5. Version and distribute curated datasets.

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
