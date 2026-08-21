# AI for Dairy

## Description

Monitor dairy cattle health, reproduction, and behavior with computer vision and wearables.

## When to use

You are monitoring individual dairy cows to detect mastitis, lameness, oestrus, or metabolic disorders, or to forecast milk yield and body condition.

## Usage

- Detect mastitis, lameness, and heat with AiHerd or smaXtec.
- Track feeding, rumination, and activity with bolus/IMU sensors.
- Monitor body condition and mobility from cameras.
- Predict calving and metabolic disorders.
- Generate to-do lists and treatment alerts.

## Steps

1. Install cameras, wearables, or bolus sensors in the barn.
2. Collect and label health, behavior, and production records.
3. Train detection and prediction models.
4. Deploy dashboards and alert systems.
5. Validate against veterinarian diagnoses and production metrics.

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
