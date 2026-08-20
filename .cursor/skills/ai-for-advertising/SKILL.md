# AI for Advertising

## Description

Ad creative generation, media buying optimization, dynamic creative optimization, and predictive performance modeling.

## When to use

You are building ad campaigns across search, social, display, and video; generating and selecting creatives; or optimizing budget allocation.

## Key concepts

- **Dynamic creative optimization (DCO)**: assemble and test copy, image, and video variants.
- **Predictive creative performance**: CTR/CVR models trained on historical A/B tests.
- **Audience and contextual targeting**: lookalikes, retargeting, and contextual signals.
- **Attribution and incrementality**: multi-touch, geo-experiments, and causal lift.
- **Brand safety and compliance**: ad policies, disclosures, and responsible AI.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Predict ad CTR from creative and audience features
X = pd.get_dummies(df[["headline", "image_tag", "audience_segment"]], drop_first=True)
y = df["ctr"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
print("R2:", model.score(X_test, y_test))
```

## Tuning notes

- Use structured creative features so models generalize across variants.
- Run adaptive or Thompson-sampling experiments to discover top creatives.
- Protect against leakage and data snooping in campaign history.
- Balance short-term conversions with long-term brand effects.

## Verification

1. Train a CTR predictor and evaluate rank correlation on held-out creatives.
2. Run a DCO experiment and report lift over a static ad.
3. Measure incremental lift with a geo or randomized holdout.

## References

- https://arxiv.org/html/2607.23696v1
- https://dl.acm.org/doi/10.1145/3442381.3449909
- https://dl.acm.org/doi/10.1145/3340531.3412720
- https://www.iab.com/wp-content/uploads/2025/01/IAB_GenerativeAIPlaybook_January_26.pdf
