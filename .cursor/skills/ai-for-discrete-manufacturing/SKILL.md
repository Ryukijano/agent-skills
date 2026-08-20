# AI for Discrete Manufacturing

## Description

Machine learning for assembly, machining, electronics, and automotive part production: process planning, scheduling, robotic assembly, and work-in-progress tracking.

## When to use

You are making distinct parts or assembling them, and need to schedule jobs, allocate resources, plan process routes, or coordinate robotic work cells.

## Usage

- **Integrated process planning and scheduling (IPPS)**: combine operation sequencing and machine allocation.
- **Job-shop and flexible job-shop scheduling**: minimize makespan, tardiness, or energy use.
- **Robotic assembly and pick-and-place**: sequence and motion planning for SCARA, cobots, and gantries.
- **Work-in-progress tracking**: trace parts through operations using MES and RFID/barcode data.
- **Learning heuristics**: GNN/RL dispatching rules for dynamic shop floors.

## Steps

1. Collect job, machine, route, and WIP data from the MES or ERP.
2. Engineer features for operations, setups, due dates, and resource availability.
3. Build an optimization or learning-based scheduler for routing and sequencing.
4. Validate schedules with a discrete-event simulator against baseline rules.
5. Deploy to the shop floor and measure makespan, tardiness, and throughput.

## Code pattern

```python
from ortools.sat.python import cp_model

# Simple flexible job-shop model
model = cp_model.CpModel()
start = {(j, o): model.NewIntVar(0, horizon, f"s_{j}_{o}") for j, o in jobs_ops}
machine = {(j, o): model.NewIntVarFromDomain(domains[j, o], f"m_{j}_{o}") for j, o in jobs_ops}
model.AddNoOverlap(intervals)
solver = cp_model.CpSolver()
solver.Solve(model)
```

## Tuning notes

- Use chronological or route-constrained data splits to avoid future-information leakage.
- Balance throughput, due-date performance, and energy in the objective.
- Validate schedules with a discrete-event simulator before deployment.

## Verification

1. Solve a small job-shop and compare makespan to a greedy priority rule.
2. Train a learned dispatching policy and benchmark against shortest-processing-time.
3. Track a part through a simulated line and verify WIP accuracy against MES events.

## References

- https://doi.org/10.48550/arxiv.2409.00968
- https://link.springer.com/article/10.1007/s10845-023-02309-8
- https://link.springer.com/article/10.1007/s11740-024-01306-x
- https://dl.acm.org/doi/10.1007/s10845-024-02423-1
