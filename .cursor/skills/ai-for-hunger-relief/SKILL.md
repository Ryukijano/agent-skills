# AI for Hunger Relief

## Description

Use AI/ML to forecast food insecurity, monitor crops, and target emergency food assistance.

## When to use

You are building or improving early warning systems for famine, food-insecurity phase classification, or allocation of emergency food assistance.

## Usage

- Forecast Integrated Food Security Phase Classification (IPC) phases.
- Use NDVI/EVI, rainfall (CHIRPS), and temperature as crop-failure signals.
- Incorporate cereal prices, market access, and conflict events into short-term forecasts.
- Collect high-frequency food consumption and coping-strategy data via mobile surveys.

## Steps

1. Gather IPC, remote-sensing, market, conflict, and survey data for the target region.
2. Build a time-series or classification model for food-insecurity phase transitions.
3. Use time-based splits and avoid leakage from future market prices.
4. Calibrate probabilities to match donor and response budgets.
5. Combine model outputs with expert judgment and maintain human escalation paths.
6. Backtest against official IPC assessments and refine as shocks evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify food-insecurity phase from agro-climatic and market features
X = df[["ndvi_anomaly", "rainfall_deficit", "cereal_price_index", "conflict_events", "market_access"]]
y = df["ipc_phase"]

clf = RandomForestClassifier(class_weight="balanced", random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Treat class imbalance with class weights or resampling; famine events are rare but high cost.
- Use time-based splits and avoid leakage from future market prices.
- Combine model outputs with expert judgment; maintain human-in-the-loop escalation paths.
- Calibrate probabilities so thresholds match donor and response budgets.

## Verification

1. Build a 90-day-ahead IPC forecast and backtest against official IPC assessments.
2. Compare the model to a rainfall-only baseline in a drought-affected region.
3. Evaluate how early the system flags an emerging food crisis compared to standard triggers.

## References

- https://www.nature.com/articles/s43016-026-01400-6
- https://sfcs.fao.org/docs/devhlpelibraries/default-document-library/hlpe-fsn-ai-note.pdf
- https://www.mdpi.com/2077-0472/13/10/2037
- https://doi.org/10.1038/s43247-024-01698-9
