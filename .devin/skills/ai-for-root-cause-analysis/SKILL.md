# AI for Root Cause Analysis

## Description

Knowledge graphs, causal discovery, graph neural networks, and SHAP-based diagnostics for identifying fault origins and propagations in complex systems.

## When to use

A quality, safety, or equipment failure has occurred and you need to trace it to the originating cause, not just its symptoms, across interacting processes and machines.

## Usage

- **5-Why and fishbone**: structured qualitative root-cause exploration.
- **Causal discovery**: learn causal graphs from time-series or tabular data (PC, GES, NOTEARS).
- **Knowledge graphs**: model equipment, materials, recipes, and fault propagation.
- **Graph neural networks**: propagate fault evidence and rank root-cause variables.
- **SHAP and counterfactuals**: attribute defect or failure to specific sensors and settings.

## Steps

1. Gather event logs, sensor data, and failure records for the incident window.
2. Build a knowledge graph of equipment, materials, and process dependencies.
3. Run causal discovery or train an attribution model to score suspect variables.
4. Cross-check the top candidates with domain experts and known incidents.
5. Document the validated root cause and prescribe corrective actions.

## Code pattern

```python
from shap import TreeExplainer
import xgboost as xgb

# Train a defect model and explain predictions
X = df.drop("defect", axis=1)
y = df["defect"]
model = xgb.XGBClassifier().fit(X, y)
explainer = TreeExplainer(model)
shap_values = explainer.shap_values(X.iloc[:100])
```

## Tuning notes

- Separate common-cause correlation from true causal links with interventional data or expert priors.
- Build knowledge graphs from P&IDs, asset hierarchies, and BOMs to ground reasoning.
- Validate root-cause rankings against known historical incidents and domain expertise.

## Verification

1. Identify the root cause of a historical defect and compare the AI ranking to the manual RCA.
2. Build a causal graph and verify a key edge with a controlled experiment or do-calculus.
3. Use SHAP to show that the top feature is actionable, not just a downstream symptom.

## References

- https://doi.org/10.1109/jsen.2025.3649083
- https://doi.org/10.1109/raai67517.2025.11423096
- https://scholarcommons.sc.edu/cgi/viewcontent.cgi?article=1633&context=aii_fac_pub
- https://dl.acm.org/doi/10.1016/j.engappai.2025.110152
- https://www.sciencedirect.com/science/article/abs/pii/S147403462600100X
