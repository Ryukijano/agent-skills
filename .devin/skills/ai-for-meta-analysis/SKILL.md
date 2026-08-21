# AI for Meta-Analysis

## Description

Automate systematic reviews and synthesize effect sizes across clinical and epidemiological studies.

## When to use

You are conducting a meta-analysis or systematic review and want to automate or augment screening, extraction, effect estimation, or heterogeneity analysis.

## Usage

- Screen citations with LLMs and Rayyan/AiReview.
- Extract study characteristics and outcomes with GPT-4 pipelines.
- Fit random-effects and Bayesian meta-analysis models.
- Assess heterogeneity, publication bias, and study quality.
- Update living systematic reviews continuously.

## Steps

1. Define the PICO question and search strategy.
2. Run automated screening and data extraction.
3. Appraise risk of bias and study quality.
4. Pool effect sizes with appropriate meta-analytic models.
5. Report forest plots, heterogeneity, and sensitivity.

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
