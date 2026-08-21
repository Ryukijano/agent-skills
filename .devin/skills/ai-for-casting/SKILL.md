# AI for Casting

## Description

Use AI and digital twins to predict casting defects, microstructure and mechanical properties and optimize gating and solidification in foundries.

## When to use

You are producing cast metal components and need to predict porosity, hot tearing, or shrinkage, optimize gating and risering, build digital twins of solidification, or improve energy and material efficiency in foundries.

## Usage

- **Predict defects**: forecast porosity, shrinkage, hot tearing, and cold shuts from process data.
- **Model microstructure**: predict SDAS, grain size, and phase fractions from thermal history.
- **Simulate solidification**: use FEA, cellular automata, or phase-field methods.
- **Optimize gating and risering**: reduce scrap and improve yield with data-driven design.
- **Build digital twins**: synchronize foundry sensors with virtual models in real time.

## Steps

1. Collect geometry, alloy composition, mold, and process data for historical castings.
2. Run casting simulations and label defects and microstructure from inspection and testing.
3. Train ML models to predict defect probability and microstructure metrics.
4. Optimize gating, risering, and process settings with surrogate or physics-informed models.
5. Validate predictions with physical castings and NDT or mechanical tests.
6. Deploy a digital twin that updates from foundry sensors and predicts part quality.

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
