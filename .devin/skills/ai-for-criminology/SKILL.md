# AI for Criminology

## Description

Predictive policing, recidivism risk assessment, crime forecasting, criminal network analysis, and fairness-aware public safety research.

## When to use

You are analyzing crime patterns, assessing risk, or designing public-safety interventions and want to use data and models responsibly.

## Key concepts

- **Crime forecasting**: spatiotemporal models for hot spots and future incident counts.
- **Recidivism risk assessment**: predict reoffending to inform sentencing or rehabilitation.
- **Criminal network analysis**: detect co-offending, money-laundering, and gang structures.
- **Victimization and fear-of-crime mapping**: combine survey, sensor, and report data.
- **Fairness and accountability**: audit for racial and neighborhood bias in predictions and deployment.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Example: risk classification for a public-safety outcome (use with extreme care)
X = df[["age", "prior_offenses", "employment_status", "substance_use"]]
y = df["recidivated"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X_train, y_train)
```

## Tuning notes

- Predictive models can amplify historical biases; require fairness audits before deployment.
- Avoid feedback loops where predictions influence policing patterns and then future data.
- Use transparent, interpretable models in high-stakes criminal justice settings.
- Engage affected communities and legal stakeholders in model design and review.

## Verification

1. Evaluate a crime-forecasting model on held-out spatial and temporal data.
2. Audit a risk model for equalized odds across demographic groups.
3. Compare a model to a simple baseline and document any deployment trade-offs.

## References

- https://link.springer.com/article/10.1007/s10940-025-09629-3
- https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2021.587943/full
- https://doi.org/10.3390/computers15050325
- https://doi.org/10.3390/ijgi11070400
