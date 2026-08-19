# Causal Inference and Discovery for Science

## Description

Do-calculus, causal discovery, structural causal models, transportability, and mediation for observational and experimental data.

## When to use

You want to go beyond correlation and identify causal effects in scientific data.

## Key concepts

- **Causal graphs**: DAGs, d-separation, back-door criterion.
- **Do-calculus**: rules for identifying causal effects from observational data.
- **Causal discovery**: PC, FCI, GES, NOTEARS, DAG-GNN.
- **Transportability**: transfer causal findings across settings.
- **Mediation analysis**: direct/indirect effects.

## Code pattern

```python
import dowhy
from dowhy import CausalModel

model = CausalModel(
    data=df,
    treatment='treatment',
    outcome='outcome',
    common_causes=['age', 'sex']
)
identified = model.identify_effect()
estimate = model.estimate_effect(identified, method_name='backdoor.linear_regression')
```

For causal discovery:

```python
from g castle import PC
pc = PC()
pred_dag = pc.fit(data).adjacency_matrix_
```

## Tuning notes

- Strong causal claims need domain knowledge and/or randomized experiments.
- Use sensitivity analysis (e.g., DoWhy refute) to test robustness.
- High-dimensional causal discovery can be unstable; validate with domain experts.

## Verification

1. Recover a known DAG from synthetic data with PC/NOTEARS.
2. Estimate an ATE on a dataset with a known ground-truth intervention.
3. Run DoWhy refutation tests and report placebo/random-common-cause outcomes.

## References

- https://www.pywhy.org/dowhy/
- https://causalml.org/
- https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf
- https://doi.org/10.1007/s41060-016-0038-6
