# AI for Conservation Planning

## Description

Use AI to decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.

## When to use

You must decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.

## Usage

- Compile species, cost, threat, and connectivity data.
- Model site irreplaceability and trade-offs.
- Run optimization (Marxan/Zonation/CAPTAIN) under budget.
- Generate prioritization maps for protection and restoration.

## Steps

1. Compile species, cost, threat, and connectivity data.
2. Model site irreplaceability and trade-offs.
3. Run optimization (Marxan/Zonation/CAPTAIN) under budget.
4. Generate prioritization maps for protection and restoration.
5. Stress-test priorities under climate and land-use scenarios.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

## Code pattern

```python
from sklearn.linear_model import LogisticRegression

# Predict site irreplaceability from species and cost features
irreplaceability = LogisticRegression(
    class_weight="balanced", max_iter=1000
).fit(X, y).predict_proba(X)[:, 1]
```

## Tuning notes

- Include acquisition/opportunity costs, threats, and connectivity constraints.
- Validate against complementarity and representation targets.
- Use scenario analysis to explore climate and land-use futures.
- Engage stakeholders to interpret trade-offs and ensure equity.

## Verification

1. Solve a small reserve-selection problem and compare cost to a greedy baseline.
2. Generate a 30x30 prioritization map and check target achievement.
3. Test robustness of priorities under climate-change scenarios.

## References

- https://doi.org/10.1016/j.tree.2024.12.002
- https://www.nature.com/articles/s41893-022-00851-6
- https://doi.org/10.1029/2025ef007560
- https://www.ijcai.org/proceedings/2025/1086.pdf
