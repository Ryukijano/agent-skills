# AI for Poultry

## Description

Monitor poultry welfare, behavior, and health with computer vision and edge sensors.

## When to use

You are monitoring poultry flocks to detect disease, assess welfare, track behaviour, or manage feeding, ventilation, and stocking density.

## Usage

- Track feeding, drinking, and activity with computer vision.
- Detect coccidiosis and salmonellosis with Edge Impulse.
- Monitor environmental conditions (temperature, ammonia, light).
- Count and locate birds with UWB/IMU wearables.
- Assess gait, feather condition, and stress.

## Steps

1. Place cameras, wearables, or environmental sensors in the house.
2. Collect and label behavior and health outcomes.
3. Train edge-deployed classification and detection models.
4. Integrate with farm management software.
5. Validate against veterinary checks and welfare audits.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

X = df[["temp", "humidity", "stocking_density", "feed_consumption", "water_consumption"]]
y = df["high_mortality_risk"]

model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Handle heavy occlusion, variable lighting, and fast movement in dense flocks.
- Welfare assessments must align with recognised protocols (e.g., Welfare Quality).
- Generalise across breeds, housing systems, and seasonal conditions.
- Avoid welfare interventions that increase stress or conflict with regulatory standards.

## Verification

1. Detect sick or lame birds from video and compare to veterinary assessment.
2. Compare automated welfare scores to manual audit results.
3. Validate mortality or disease prediction on a held-out flock cycle.

## References

- https://doi.org/10.1016/j.japr.2025.100602
- https://pmc.ncbi.nlm.nih.gov/articles/PMC11700577/
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6770384/
- https://www.mdpi.com/2071-1050/12/4/1413
