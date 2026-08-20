# AI for Operations Research

## Description

Optimization, MILP/CP, vehicle routing and scheduling, decision-focused learning, and learning-augmented heuristics.

## When to use

You need to make optimal or near-optimal decisions under constraints for routing, scheduling, resource allocation, or network design.

## Key concepts

- **Mathematical programming**: LP, MILP, and constraint programming for feasibility and optimality.
- **Combinatorial optimization augmented ML**: embed optimization oracles inside learning pipelines.
- **Learning for routing and scheduling**: GNNs and reinforcement learning to learn heuristics for TSP/VRP/job shop.
- **Decision-focused learning**: train models with losses that account for downstream optimization costs.

## Code pattern

```python
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")
x = solver.NumVar(0, 10, "x")
y = solver.NumVar(0, 10, "y")

solver.Add(2 * x + y <= 10)
solver.Maximize(3 * x + 4 * y)
status = solver.Solve()

print(solver.Objective().Value())
print(x.solution_value(), y.solution_value())
```

## Tuning notes

- Choose exact solvers when problem size permits; otherwise use metaheuristics or learned heuristics.
- In decision-focused learning, backpropagate through the optimization layer with care.
- Validate learned policies against strong OR baselines (e.g., LKH, CP-SAT).

## Verification

1. Solve a small MILP and compare the objective to a greedy baseline.
2. Train a learned heuristic for a routing problem and benchmark against a classical solver.
3. Implement decision-focused learning and show improvement over two-stage predict-then-optimize.

## References

- https://arxiv.org/abs/2601.10583
- https://arxiv.org/pdf/2507.00218
- https://ojmo.centre-mersenne.org/item/10.5802/ojmo.43.pdf
- https://link.springer.com/article/10.1007/s10994-026-07116-9
