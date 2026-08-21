# AI for Constraint Programming

## Description

Use machine learning to learn constraints, heuristics, and models for constraint programming and CP-SAT solvers.

## When to use

You are modeling and solving constraint satisfaction and optimization problems and want to learn constraints, heuristics, or entire models from data.

## Usage

- Learn constraints from examples of feasible and infeasible solutions.
- Learn variable and value ordering heuristics for CP and CP-SAT solvers.
- Synthesize optimization or CSP models from observations of behavior.
- Combine lazy clause generation and CP-SAT with neural predictors.

## Steps

1. Gather labeled examples of feasible, infeasible, or optimal solutions for the target problem.
2. Train a constraint learner or heuristic predictor from the example set.
3. Combine learned constraints with expert-written constraints for safety.
4. Integrate the learned heuristic into a CP or CP-SAT solver and compare search nodes.
5. Acquire a candidate CP model from data and validate it on an independent test set.
6. Benchmark against default CP solver strategies and tune with active learning.

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
