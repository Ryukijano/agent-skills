# AI for Livestock

## Description

Track and predict health, behavior, and productivity across livestock.

## When to use

You are monitoring livestock health, behaviour, or productivity across species and want data-driven insights for individual or herd management.

## Usage

- Monitor behavior and posture with AnimalFormer and WERS.
- Detect lameness, heat, and calving with video and wearables.
- Track individual animals with RFID, UWB, and computer vision.
- Predict weight gain and feed conversion.
- Build farm-level decision support dashboards.

## Steps

1. Select species and target traits (health, behavior, production).
2. Install cameras, wearables, or RFID readers.
3. Collect and annotate phenotypes and events.
4. Train species-specific models.
5. Validate against farm records and expert scoring.

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
