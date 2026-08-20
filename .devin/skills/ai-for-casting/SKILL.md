# AI for Casting

## Description

Machine learning for sand, investment, die, and continuous casting: defect prediction, mold filling, solidification, microstructure, and process optimization.

## When to use

You are producing cast metal components and need to predict porosity, hot tearing, or shrinkage, optimize gating and risering, build digital twins of solidification, or improve energy and material efficiency in foundries.

## Key concepts

- **Casting defects**: porosity, shrinkage, hot tearing, cold shuts, inclusions, and surface defects.
- **Solidification modeling**: thermal history, dendrite arm spacing, phase fraction, and microstructure.
- **Process parameters**: pouring temperature, mold temperature, pouring rate, cooling rate, and alloy composition.
- **ICME and digital twins**: coupling thermodynamic, macro/micro-scale simulation with data-driven models.
- **High-pressure and continuous casting**: cycle time, die wear, and real-time quality control.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Classify defect risk from casting parameters and alloy composition
X = df[["pour_temp_C", "mold_temp_C", "pour_time_s", "cooling_rate_C_s", "Si_pct", "Cu_pct"]]
y = df["defect_present"]
model = RandomForestClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Casting data are sparse and imbalanced; use rare-event metrics and balanced resampling.
- Multi-scale effects require features from both macro process and microstructure models.
- Defect labels are often post-process and delayed; incorporate defect type and location.
- Validate on physical castings, not only simulation, because turbulence and oxide effects are hard to model.

## Verification

1. Predict hot tearing or porosity from process data and compare to radiography or cut-up results.
2. Optimize a gating or riser design with a surrogate and verify improved yield.
3. Build a digital twin that synchronizes simulated and measured temperatures.

## References

- https://doi.org/10.1007/s43939-026-00685-5
- https://www.mdpi.com/2076-3417/12/7/3264
- https://doi.org/10.24425/amm.2024.151428
- https://www.nature.com/articles/s41524-025-01524-6
- https://doi.org/10.2320/matertrans.mt-la2022038
