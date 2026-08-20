# AI for Tenant Experience

## Description

Personalization, occupancy analytics, indoor environmental quality, and tenant engagement for workplace and residential environments.

## When to use

You want to improve tenant satisfaction, engagement, retention, and workplace productivity in commercial or residential buildings.

## Usage

- **Indoor environmental quality**: predict thermal, visual, acoustic, and air-quality satisfaction.
- **Personalization**: adjust lighting, temperature, and space recommendations.
- **Occupancy analytics**: understand space utilization and preferences.
- **Tenant apps and services**: AI chatbots, maintenance ticketing, and amenity booking.

## Steps

1. Collect post-occupancy evaluation, sensor, and app engagement data.
2. Link environmental conditions to satisfaction scores.
3. Train preference and satisfaction models (Random Forest, LSTM, attention).
4. Deploy personalization rules and feedback loops.
5. Track NPS, retention, and utilization KPIs.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict tenant satisfaction category
X = df[['temperature', 'light_level', 'noise', 'air_quality']]
y = df['satisfaction_label']
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Respect privacy and consent for occupant data.
- Use explainable models to avoid black-box comfort controls.
- Account for individual and seasonal preference variation.

## Verification

1. Predict satisfaction on a post-occupancy evaluation dataset.
2. A/B test personalized setpoints against default settings.
3. Correlate experience improvements with retention or NPS.

## References

- https://doi.org/10.1108/sasbe-03-2025-0161
- https://www.mdpi.com/1424-8220/18/5/1602
- https://www.mdpi.com/2071-1050/16/10/4258
- https://doi.org/10.1038/s41598-025-10086-y

## References

- https://doi.org/10.1108/sasbe-03-2025-0161
- https://www.mdpi.com/1424-8220/18/5/1602
- https://www.mdpi.com/2071-1050/16/10/4258
- https://doi.org/10.1038/s41598-025-10086-y
