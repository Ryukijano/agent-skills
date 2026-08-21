# AI for Poverty Alleviation

## Description

Use machine learning to map poverty, estimate consumption, target social transfers, and improve social protection in low-resource settings.

## When to use

You need to estimate economic well-being, target cash transfers, or map poverty at high spatial resolution where traditional survey data are sparse or outdated.

## Usage

- Combine satellite imagery, nighttime lights, and built-environment features with household surveys.
- Build proxy means testing scoring to identify eligible beneficiaries.
- Use mobile data such as call-detail records and airtime as proxies for income shocks.
- Monitor exclusion and inclusion errors across gender, ethnicity, and geography.

## Steps

1. Assemble household surveys, geospatial layers, and mobile or administrative data.
2. Train consumption or wealth prediction models with spatial or temporal cross-validation.
3. Use predictions to produce high-resolution poverty maps and rank households for targeting.
4. Measure targeting quality by exclusion/inclusion errors and coverage of the poorest quintile.
5. Audit for disparities and protect sensitive mobile/geospatial data.
6. Integrate with government or NGO targeting systems and update as conditions change.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

# Predict consumption expenditure from satellite and demographic features
X = df[["nighttime_lights", "road_density", "building_count", "vegetation_index", "hh_size"]]
y = df["consumption_per_capita"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = GradientBoostingRegressor(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Use cross-validation with spatial or temporal splits; poverty features are highly correlated across nearby villages.
- Down-weight nighttime lights where electrification is uneven; include daytime texture features.
- Validate targeting quality by exclusion/inclusion error, not just R2.
- Protect sensitive mobile and geospatial data with differential privacy or aggregation.

## Verification

1. Replicate a small-area poverty map and compare it to a recent census or survey estimate.
2. Train a PMT and measure how well it captures the poorest quintile in a holdout region.
3. Audit the model for disparities across protected groups before deployment.

## References

- https://www.science.org/doi/10.1126/science.aaf7894
- https://pubmed.ncbi.nlm.nih.gov/35914150/
- https://www.nature.com/articles/s41586-022-05422-504484-9
- https://doi.org/10.1257/aer.20221650
- https://arxiv.org/abs/2202.00109
