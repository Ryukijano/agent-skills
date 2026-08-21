# AI for Six Sigma

## Description

Augments DMAIC projects with defect prediction, statistical process control, and designed-experiment optimization.

## When to use

You are running a Six Sigma or Lean Six Sigma project and want to speed up DMAIC with machine learning for pattern detection, prediction, and prescriptive action.

## Usage

- **DMAIC augmentation**: support Define, Measure, Analyze, Improve, Control with data-driven methods.
- **Statistical process control (SPC)**: control charts, process capability (Cp/Cpk), and drift monitoring.
- **Defect prediction**: classify or regress defect risk from process parameters.
- **Design of experiments (DOE)**: optimize factor settings with fewer experimental runs.
- **XAI for Six Sigma**: use SHAP and LIME for interpretable cause prioritization.

## Steps

1. Define the problem, CTQ, and project scope with stakeholders.
2. Measure process performance and collect historical defect and parameter data.
3. Analyze data with SPC, capability analysis, and ML defect-prediction models such as Random Forest or CART.
4. Improve by optimizing process settings and piloting changes.
5. Control with monitoring dashboards and retrain models as conditions change.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict defect probability during the Analyze/Improve phase
X = df[["feed_rate", "spindle_speed", "coolant_flow", "ambient_temp"]]
y = df["defective"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Use phase-appropriate models and metrics; control charts need stability, not just accuracy.
- Avoid data leakage from future inspections into the Measure/Analyze data.
- Combine statistical rigor with ML; validate predictions against designed experiments.

## Verification

1. Build a defect-prediction model and compare precision/recall to the current SPC rules.
2. Compute Cpk before and after an improvement and confirm it meets the target.
3. Use SHAP values to rank root causes and validate with a fishbone session.

## References

- https://doi.org/10.1109/tem.2023.3335237
- https://doi.org/10.1109/tem.2023.3324542
- https://doi.org/10.1109/tem.2025.3634836
- https://doi.org/10.1109/access.2021.3103931
- https://www.isixsigma.com/artificial-intelligence/how-ai-can-be-used-in-the-dmaic-process/
