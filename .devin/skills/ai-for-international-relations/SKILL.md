# AI for International Relations

## Description

Conflict forecasting, event data analysis, crisis early warning, treaty and negotiation text mining, and geopolitical risk modeling.

## When to use

You are studying conflict, diplomacy, trade, sanctions, or global governance and want to forecast events, extract information from open-source reports, or model geopolitical networks.

## Key concepts

- **Event data and CAMEO/Phoenix**: code actor-action-target triples from news and reports.
- **Conflict forecasting**: predict civil unrest, armed conflict, and fatalities at country or grid level.
- **Crisis early warning**: combine event counts, economic indicators, and social media for alerts.
- **Treaty and negotiation text mining**: analyze agreements, UN speeches, and diplomatic cables.
- **Geopolitical network and spatial models**: capture alliances, trade dependencies, and neighborhood effects.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import TimeSeriesSplit

# Country-month conflict risk classifier from event and structural features
X = df[["past_fatalities", "event_count", "neighbor_conflict", "gdp_growth"]]
y = df["conflict_onset"]

cv = TimeSeriesSplit(n_splits=5)
for train_idx, test_idx in cv.split(X):
    model = RandomForestClassifier(class_weight="balanced", random_state=42)
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    print(model.score(X.iloc[test_idx], y.iloc[test_idx]))
```

## Tuning notes

- Conflict is rare; use class weights, cost-sensitive learning, and proper rare-event metrics.
- Respect temporal ordering with time-series cross-validation.
- Spatial autocorrelation and diffusion must be modeled explicitly, not ignored.
- Geopolitical models raise ethical and policy stakes; prioritize interpretability and caution.

## Verification

1. Backtest a conflict-forecasting model on out-of-sample country-months.
2. Compare your model to a strong baseline such as a random or lag-only model.
3. Evaluate with proper rare-event metrics (precision-recall, Brier score, CRPS).

## References

- https://doi.org/10.1093/jeea/jvac025
- https://www.cambridge.org/core/journals/data-and-policy/article/promise-of-machine-learning-in-violent-conflict-forecasting/40D559ADA18FF7308915B08956B4E8F3
- https://doi.org/10.3389/frai.2022.893875
- https://par.nsf.gov/servlets/purl/10376284
