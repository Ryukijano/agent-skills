# AI for Livestock

## Description

Machine learning for health, behaviour, welfare, grazing, and reproduction across cattle, pigs, sheep, goats, and other farm animals.

## When to use

You are monitoring livestock health, behaviour, or productivity across species and want data-driven insights for individual or herd management.

## Usage

- **Animal health and disease detection**: identify lameness, respiratory issues, and metabolic disorders.
- **Behaviour and welfare monitoring**: classify feeding, resting, rumination, social, and heat behaviours.
- **Grazing and pasture management**: estimate intake, forage availability, and animal distribution.
- **Reproduction and growth tracking**: predict calving, farrowing, weight gain, and market readiness.

## Steps

1. Choose sensors appropriate to the species and environment (wearables, cameras, microphones, scales).
2. Identify and track individual animals with RFID, computer vision, or biometrics.
3. Engineer features and train models per target health, behaviour, or production outcome.
4. Validate across farms, breeds, seasons, and production systems.
5. Deploy alerts and integrate with farm management software and veterinary workflows.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier

X = df[["activity", "feed_intake", "water_intake", "body_temp", "weight"]]
y = df["health_status"]

model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Maintain per-animal models while allowing herd-level aggregation.
- Address species differences, housing types, and climatic variation.
- Handle long-tailed health events and rare abnormal behaviours.
- Ensure welfare, ethical review, and data governance for animal data.

## Verification

1. Detect a target disease or condition and report AUC on a held-out group of animals.
2. Compare automated behaviour classification to expert-annotated video.
3. Test model transfer to a different breed or farm without full retraining.

## References

- https://www.sciencedirect.com/science/article/pii/S0168169920317099
- https://doi.org/10.5713/ab.25.0289
- https://doi.org/10.1016/j.aiia.2026.04.013
- https://www.mdpi.com/1424-8220/23/12/5732

## References

- https://www.sciencedirect.com/science/article/pii/S0168169920317099
- https://doi.org/10.5713/ab.25.0289
- https://doi.org/10.1016/j.aiia.2026.04.013
- https://www.mdpi.com/1424-8220/23/12/5732
