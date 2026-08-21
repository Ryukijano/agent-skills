# AI for Higher Education

## Description

Use AI to improve access, success, retention, or operational decisions in colleges and universities.

## When to use

You are improving access, success, retention, or operational decisions in colleges and universities.

## Usage

- Integrate admissions, retention, and advising data.
- Build retention and completion risk models.
- Equitably triage outreach and advising.
- Monitor intervention impact.

## Steps

1. Integrate admissions, retention, and advising data.
2. Build retention and completion risk models.
3. Equitably triage outreach and advising.
4. Monitor intervention impact.
5. Audit for fairness across demographic subgroups and programs.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["hs_gpa", "first_gen", "credit_load", "campus_engagement"]]
y = df["retained_year_2"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Avoid high-stakes decisions based solely on predicted risk scores.
- Ensure compliance with FERPA, GDPR, and institutional IRB requirements.
- Audit predictions for subgroup disparities and validate longitudinally.

## Verification

1. Predict first-year retention and report AUC by demographic subgroup.
2. Build an equity-aware course or admissions recommender.
3. Evaluate whether advisor use of an early-alert system changes outcomes.

## References

- https://www.nature.com/articles/s41598-025-23116-6
- https://link.springer.com/article/10.1007/s10734-025-01509-w
- https://www.science.org/doi/10.1126/sciadv.adg9405
- https://arxiv.org/abs/2411.15348
