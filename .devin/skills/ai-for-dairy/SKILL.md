# AI for Dairy

## Description

Machine learning for health, fertility, behaviour, and production monitoring in dairy cattle and dairy farm decision support.

## When to use

You are monitoring individual dairy cows to detect mastitis, lameness, oestrus, or metabolic disorders, or to forecast milk yield and body condition.

## Usage

- **Mastitis and disease detection**: classify early health events from milk, sensor, or image data.
- **Reproductive management**: predict heat, calving, and optimal insemination timing.
- **Milk yield and body-condition scoring**: forecast production and body reserves.
- **Feeding and behaviour monitoring**: detect changes in rumination, activity, and feed intake.

## Steps

1. Collect animal-level data from milking systems, wearables, cameras, and farm records.
2. Engineer time-series and per-cow features (lactation stage, parity, days in milk).
3. Train classification or regression models for each target health or production outcome.
4. Validate with chronological splits and across multiple farms or breeds.
5. Deploy real-time alerts and integrate with herd management software.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

X = df[["milk_yield", "scc", "activity", "rumination", "days_in_milk"]]
y = df["mastitis_7d"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Dairy data are highly imbalanced; use class weights, resampling, or cost-sensitive learning.
- Account for lactation curve, parity, season, and herd management effects.
- Sensors and milking systems drift; monitor and recalibrate models routinely.
- Keep animal welfare and data privacy central to model design and deployment.

## Verification

1. Report early mastitis detection AUC on a temporally held-out herd.
2. Compare heat-detection recall to visual oestrus detection.
3. Validate milk-yield forecasts against actual test-day records.

## References

- https://www.mdpi.com/2077-0472/13/10/1858
- https://www.sciencedirect.com/science/article/pii/S0167587720309211
- https://www.mdpi.com/2076-2615/15/14/2033
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8747441/

## References

- https://www.mdpi.com/2077-0472/13/10/1858
- https://www.sciencedirect.com/science/article/pii/S0167587720309211
- https://www.mdpi.com/2076-2615/15/14/2033
- https://pmc.ncbi.nlm.nih.gov/articles/PMC8747441/
