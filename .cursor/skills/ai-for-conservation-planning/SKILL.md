# AI for Conservation Planning

## Description

Spatial prioritization, protected-area design, systematic conservation planning, and trade-off analysis using optimization and ML.

## When to use

You must decide where to protect, restore, or manage land/sea to meet biodiversity targets under budget and equity constraints.

## Key concepts

- **Systematic conservation planning (SCP)**: cost-effective selection of actions and areas (Marxan, Zonation).
- **AI-driven prioritization**: reinforcement learning for spatial conservation (CAPTAIN).
- **Trade-offs**: biodiversity, carbon, water, and livelihood objectives.
- **Connectivity and climate adaptation**: corridor design and climate-smart prioritization.

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
- https://doi.org/10.1101/2025.01.06.631540
- https://www.ijcai.org/proceedings/2025/1086.pdf
