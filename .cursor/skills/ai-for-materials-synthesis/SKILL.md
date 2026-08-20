# AI for Materials Synthesis

## Description

Machine learning for synthesis route prediction, process optimization, and inverse design of materials.

## When to use

You are predicting how to make a material, optimizing a synthesis recipe, or exploring process parameters.

## Key concepts

- **Synthesisability prediction**: estimate whether a target compound can be made.
- **Retrosynthesis and reaction prediction**: plan synthesis pathways.
- **Process optimization**: Bayesian optimization of temperature, pressure, precursors.
- **Lab automation**: self-driving labs for closed-loop materials discovery.

## Code pattern

```python
from ax.service.ax_client import AxClient

# Optimize synthesis conditions
ax = AxClient()
ax.create_experiment(
    name="synthesis",
    parameters=[{"name": "temp", "type": "range", "bounds": [300.0, 800.0]}],
    objective_name="yield",
)
```

## Tuning notes

- Use literature-extracted reaction data and domain constraints.
- Bayesian optimization is useful when experiments are expensive.
- Validate predicted routes with chemists and lab experiments.

## Verification

1. Predict synthesis conditions for a set of known compounds.
2. Optimize a process using a few rounds of Bayesian optimization.
3. Cross-check a proposed route with a reaction database.

## References

- https://doi.org/10.1038/s41586-023-06197-2
- https://citrine.io/
- https://github.com/aspuru-guzik-group/chemos
- https://ax.dev/
