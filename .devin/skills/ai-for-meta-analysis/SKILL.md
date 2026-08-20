# AI for Meta-Analysis

## Description

Machine learning and LLMs for automating literature search, screening, data extraction, effect-size estimation, and heterogeneity assessment in meta-analyses.

## When to use

You are conducting a meta-analysis or systematic review and want to automate or augment screening, extraction, effect estimation, or heterogeneity analysis.

## Usage

- **Automated literature search and screening**: classify and rank citations for inclusion.
- **Data extraction**: parse study characteristics, outcomes, and effect sizes from PDFs.
- **Statistical modeling**: estimate pooled effects, heterogeneity, and subgroup differences.
- **Network meta-analysis**: synthesize direct and indirect treatment comparisons.

## Steps

1. Register the protocol and define PICO/PECO and analysis plan.
2. Run a reproducible search and import citations into an AI-assisted screening tool.
3. Use ML or LLMs to extract study data with human verification.
4. Compute effect sizes and pooled estimates using appropriate models (fixed, random, Bayesian).
5. Assess risk of bias, heterogeneity, and sensitivity to study inclusion.

## Code pattern

```python
import pandas as pd
import numpy as np
from statsmodels.stats.meta_analysis import combine_effects

# Data frame with effect sizes and standard errors
effects = meta_df["effect_size"]
se = meta_df["se"]

combined = combine_effects(effects, se, method_re="ml")
print("Pooled effect:", combined.effect)
print("I-squared:", combined.i2)
```

## Tuning notes

- Use human-in-the-loop validation for screening and extraction decisions.
- Choose effect-size metrics and models appropriate to the data types.
- Assess publication bias with funnel plots and Egger tests.
- Document all automation choices and review for errors or hallucinations.

## Verification

1. Reproduce a published meta-analysis using extracted data and compare pooled estimates.
2. Compare LLM-extracted data to manually extracted data on a validation set.
3. Run leave-one-out and subgroup meta-analyses to assess robustness.

## References

- https://doi.org/10.1017/rsm.2025.10065
- https://arxiv.org/abs/2606.28363
- https://www.ncbi.nlm.nih.gov/pmc/articles/13035263
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
- https://link.springer.com/article/10.1007/s41669-024-00476-9
