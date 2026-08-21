# AI for Biofoundries

## Description

Combine robotic automation, LIMS, and active learning to run closed-loop Design-Build-Test-Learn campaigns at scale.

## When to use

You are running high-throughput synthetic biology experiments in a biofoundry, automating liquid handling, or closing the DBTL loop with predictive models.

## Usage

- **Robotic execution**: use liquid-handling robots, plate readers, and bioreactors to build and assay designs at scale.
- **DBTL automation**: run Design-Build-Test-Learn cycles with minimal human intervention.
- **Self-driving labs**: let active-learning agents propose and schedule the next experiments.
- **Workflow abstraction**: encode protocols as unit operations and reusable workflows in a LIMS/scheduler.
- **Surrogate/digital-twin modeling**: predict titers, yields, or activity from process parameters.
- **FAIR data capture**: link samples, designs, and results through metadata, barcodes, and programmable APIs.

## Steps

1. Define the workflow (e.g., strain construction, enzyme screening, medium optimization) and map unit operations.
2. Encode protocols for robotic liquid handling, incubation, and analytical instruments in a LIMS/scheduler.
3. Run an initial design-of-experiments or active-learning batch to generate a training set.
4. Train surrogate models from instrument outputs (titers, fluorescence, growth) and process features.
5. Use Bayesian optimization to propose the next physical constructs to build and test.
6. Analyze results, update the model, and scale the best-performing designs.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from skopt import gp_minimize
from skopt.space import Real, Integer

# Measured titers from previous DBTL cycle
df = pd.read_csv('biofoundry_results.csv')
X = df[['promoter_strength', 'rbs_strength', 'copy_number', 'induction']]
y = df['titer']

surrogate = RandomForestRegressor().fit(X, y)

space = [
    Real(0.0, 1.0, name='promoter_strength'),
    Real(0.0, 1.0, name='rbs_strength'),
    Integer(1, 10, name='copy_number'),
    Real(0.0, 1.0, name='induction'),
]

def objective(params):
    return -surrogate.predict([params])[0]

result = gp_minimize(objective, space, n_calls=20)
print('Next best design:', result.x)
```

## Tuning notes

- Integrate the robot API and LIMS for true closed-loop operation.
- Use constrained optimization to respect hardware and biology limits.
- Track batch and instrument effects as features.
- Keep human-in-the-loop for safety and protocol validation.
- Start with simple designs and incrementally add combinatorial complexity.

## Verification

1. Build a surrogate model of titer from historical biofoundry runs.
2. Run a Bayesian optimization loop and compare predicted vs measured titer.
3. Document a reproducible workflow from design to data using a LIMS/ELN.

## References

- https://ibiofoundry.illinois.edu/
- https://doi.org/10.1016/j.copbio.2025.103380
- https://doi.org/10.1016/j.copbio.2026.103503
- https://github.com/sblabkribb/biofoundry_workflows
- https://doi.org/10.3389/fsybi.2025.1630026
