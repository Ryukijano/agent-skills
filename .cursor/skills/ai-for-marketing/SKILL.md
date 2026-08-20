# AI for Marketing

## Description

Customer segmentation, personalization, propensity modeling, marketing-mix attribution, and generative AI for content and campaigns.

## When to use

You need to target customers more precisely, personalize messages, allocate marketing budget, or measure campaign effectiveness.

## Key concepts

- **Customer segmentation**: RFM, clustering, and behavioral segmentation to identify actionable personas.
- **Propensity and uplift modeling**: predict likelihood to buy or respond to a treatment; target those most persuadable.
- **Marketing attribution**: assign credit across touchpoints using rule-based, data-driven, or causal methods.
- **Generative AI for creative**: LLMs and diffusion models for copy, images, and dynamic creative assembly.

## Code pattern

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# RFM-style customer segmentation
X = df[["recency_days", "frequency", "monetary_value"]]
X_scaled = StandardScaler().fit_transform(X)
clusters = KMeans(n_clusters=4, random_state=42, n_init="auto").fit_predict(X_scaled)
df["segment"] = clusters
```

## Tuning notes

- Segmentations are only useful if they are stable and lead to differentiated actions.
- Uplift models need randomized holdouts to validate true incremental impact.
- Use causal or doubly robust estimators for attribution, especially with sequential data.

## Verification

1. Compare a clustering-based segment to a rule-based baseline in an A/B test.
2. Build an uplift model and estimate incremental lift on a holdout set.
3. Evaluate a generative copy pipeline for relevance and brand safety.

## References

- https://www.bcg.com/publications/2024/blueprint-for-ai-powered-marketing
- https://doi.org/10.1016/j.jbusres.2023.114254
- https://faculty.washington.edu/hemay/Personalization_Review.pdf
- https://doi.org/10.63125/x3e0dx27
