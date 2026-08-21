# AI for Refugees

## Description

Use machine learning to forecast displacement, map refugee camps, and allocate humanitarian resources.

## When to use

You need to anticipate refugee or asylum-seeker arrivals, map camp infrastructure, or allocate resources before displacement peaks.

## Usage

- Forecast cross-border flows from violence, governance, economic, and environmental indicators.
- Detect shelters, service points, and population density in satellite/VHR imagery.
- Estimate destination-country distribution with gravity and network models.
- Run counterfactual scenario analysis for conflict or drought shocks.

## Steps

1. Collect origin-country stressors, displacement statistics, and camp imagery.
2. Train panel models with origin, destination, and time fixed effects.
3. Build a camp-mapping or shelter-detection pipeline from VHR imagery.
4. Validate out-of-sample across crisis periods and geographic regions.
5. Run scenario forecasts and share uncertainty with policymakers.
6. Integrate with UNHCR or humanitarian planning workflows.

## Code pattern

```python
import pandas as pd
from sklearn.linear_model import ElasticNet

# Forecast asylum-seeker arrivals from origin-country stressors
X = df[["conflict_intensity", "food_price_index", "governance_index", "distance_km", "border_open"]]
y = df["asylum_seekers"]

model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X, y)
```

## Tuning notes

- Use panel-data models with origin, destination, and time fixed effects.
- Handle structural breaks and zero-inflation; many origin-destination pairs have no arrivals.
- Validate out-of-sample across different crisis periods, not just random rows.
- Be transparent about assumptions and uncertainty in forecasts used for policy.

## Verification

1. Build a 12-month displacement forecast for a set of fragile countries and compare to UNHCR planning figures.
2. Detect tents or built structures in a VHR refugee-camp image and compare to manual counts.
3. Evaluate destination-choice model with rank-based metrics on a heldout year.

## References

- https://www.cambridge.org/core/journals/data-and-policy/article/developing-ai-predictive-migration-tools-to-enhance-humanitarian-support-the-case-of-eumigratool/54E3FF814CD44FF426272335AFDD76AE
- https://ojs.aaai.org/index.php/AAAI/article/view/26846
- https://drc.ngo/en/pages/foresight-displacement-forecasts/
- https://www.microsoft.com/en-us/research/publication/mapping-refugee-camps-with-ai-a-benchmark-dataset-and-baseline-models-for-humanitarian-applications/
- https://doi.org/10.1287/opre.2021.0534
