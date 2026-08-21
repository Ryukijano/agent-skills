# AI for Materials Synthesis

## Description

Use machine learning to predict synthesis recipes, plan routes, optimize process conditions, and drive self-driving laboratory workflows.

## When to use

You are predicting how to make a material, optimizing a synthesis recipe, or exploring process parameters.

## Usage

- Predict whether a target material can be synthesized and recommend feasible precursor sets.
- Plan retrosynthetic or reaction pathways using language or graph models trained on literature recipes.
- Optimize synthesis conditions (temperature, pressure, precursors, atmosphere) with Bayesian or active-learning methods.
- Operate self-driving laboratories that design, execute, and learn from synthesis experiments in closed loops.

## Steps

1. Define target material(s) and collect synthesis recipes, precursors, and process data from literature or databases.
2. Train a synthesizability or retrosynthesis model to propose candidate recipes and rank precursor sets.
3. Use Bayesian optimization or active learning to plan the most informative next experiments.
4. Execute planned syntheses manually or with robotic lab automation, and characterize products (XRD, XRF, etc.).
5. Update models with new outcomes and iterate until the target yield, purity, or property is achieved.
6. Validate the final recipe against a reaction database and reproduce it in independent runs.

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

- https://doi.org/10.1038/s41586-023-06197-z
- https://citrine.io/
- https://github.com/aspuru-guzik-group/chemos
- https://ax.dev/
