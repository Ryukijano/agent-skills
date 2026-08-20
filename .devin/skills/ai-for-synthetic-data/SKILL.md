# AI for Synthetic Data

## Description

Generative models, differential privacy, tabular/image/text synthesis, and utility-privacy evaluation for creating realistic synthetic datasets.

## When to use

You need to augment, privatize, or replace a real dataset with artificial samples for downstream ML, testing, or sharing while preserving privacy and utility.

## Key concepts

- **Tabular synthetic data**: GANs, VAEs, diffusion, copulas, and Bayesian networks for structured records.
- **Differential privacy (DP)**: formal privacy budgets (epsilon/delta) when training generative models.
- **LLM-driven text synthesis**: instruction-based generation for low-resource NLP.
- **Utility-privacy trade-off**: fidelity metrics, downstream task performance, and membership-inference audits.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Compare downstream utility on real vs synthetic data
X_real, y_real = real_df.drop("target", axis=1), real_df["target"]
X_syn, y_syn = synth_df.drop("target", axis=1), synth_df["target"]

real_model = RandomForestClassifier(random_state=42).fit(X_real, y_real)
syn_model = RandomForestClassifier(random_state=42).fit(X_syn, y_syn)

real_on_real = real_model.score(X_real, y_real)
syn_on_real = syn_model.score(X_real, y_real)
print("Utility gap:", real_on_real - syn_on_real)
```

## Tuning notes

- Preserve marginal and joint distributions; use propensity-score-based metrics for high-dimensional tables.
- Choose epsilon carefully: smaller values increase privacy but can destroy utility.
- Audit with membership-inference or attribute-inference attacks before release.
- Document the synthesis method and privacy assumptions for downstream users.

## Verification

1. Train a classifier on synthetic data and evaluate its test AUC on real held-out data.
2. Run a membership-inference attack against the synthetic release and report precision at fixed recall.
3. Compare histograms and conditional distributions of key variables between real and synthetic data.

## References

- https://arxiv.org/abs/2403.04190
- https://arxiv.org/html/2302.04062
- https://doi.org/10.48550/arxiv.2401.02524
- https://arxiv.org/html/2503.20846
