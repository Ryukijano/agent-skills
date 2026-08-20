# AI for Biofoundries

## Description

AI/ML-driven lab automation, robotic liquid handling, closed-loop DBTL, and self-driving laboratories for synthetic biology.

## When to use

You are running high-throughput synthetic biology experiments in a biofoundry, automating liquid handling, or closing the DBTL loop with predictive models.

## Key concepts

- **Biofoundry infrastructure**: robotic liquid handlers, plate readers, bioreactors, LIMS.
- **DBTL automation**: design, build, test, learn cycles executed with minimal human intervention.
- **Self-driving labs**: active learning + automation to select and run the next experiments.
- **Workflow abstraction**: unit operations, workflows, projects.
- **Digital twins**: models that simulate expected experimental outcomes.
- **Data standards**: metadata capture, FAIR principles, programmable APIs.

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
