# AI for Constraint Programming

## Description

ML for constraint learning, search heuristics, model acquisition, and combining CP solvers with neural predictors.

## When to use

You are modeling and solving constraint satisfaction and optimization problems and want to learn constraints, heuristics, or entire models from data.

## Key concepts

- **Constraint learning**: infer constraints from examples of feasible/infeasible solutions.
- **Search heuristics**: learn variable and value ordering decisions for CP solvers.
- **Model acquisition**: synthesize optimization or CSP models from observations.
- **Lazy clause generation and CP-SAT**: combining CP and SAT-style reasoning with ML.

## Code pattern

```python
from ortools.sat.python import cp_model

# Small CP-SAT model learned/specified for a scheduling problem
model = cp_model.CpModel()
starts = [model.NewIntVar(0, 10, f"s{i}") for i in range(3)]
durations = [2, 3, 1]
ends = [model.NewIntVar(0, 15, f"e{i}") for i in range(3)]

for s, d, e in zip(starts, durations, ends):
    model.Add(e == s + d)

# No-overlap constraints
model.Add(ends[0] <= starts[1]).OnlyEnforceIf(model.NewBoolVar(""))

solver = cp_model.CpSolver()
status = solver.Solve(model)
print("Status:", status, "Makespan:", solver.ObjectiveValue())
```

## Tuning notes

- Use active learning when constraint examples are expensive to label.
- Combine learned constraints with expert-written constraints for safety.
- Benchmark learned heuristics against default CP solver strategies.

## Verification

1. Learn a set of constraints from feasible/infeasible examples and check solution feasibility.
2. Train a variable-ordering heuristic and compare search nodes to the default solver.
3. Acquire a CP model from data and validate it against an independent test set.

## References

- https://doi.org/10.1613/jair.1.19533
- https://jair.org/index.php/jair/article/download/19533/27252
- https://www.ijcai.org/proceedings/2018/0772.pdf
- https://www.ijcai.org/proceedings/2021/0610.pdf
- https://www.jair.org/index.php/jair/article/view/21207
