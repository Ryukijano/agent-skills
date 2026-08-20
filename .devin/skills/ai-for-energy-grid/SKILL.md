# AI for Energy Grid

## Description

Power-flow surrogates, renewable and load forecasting, grid stability, optimal power flow, and AI-assisted grid operations.

## When to use

You are building, operating, or studying power systems with high renewable penetration and need fast, scalable, and physically consistent predictions or optimizations.

## Key concepts

- **AC/DC power flow**: compute bus voltages, branch flows, and generator dispatch subject to physical and operational constraints.
- **Optimal Power Flow (OPF)**: cost-minimizing dispatch while satisfying voltage, thermal, and generator limits.
- **Renewable and load forecasting**: probabilistic time-series models for solar, wind, and demand.
- **Grid foundation models**: neural surrogates such as GridSFM and OpenGridFM that solve OPF in milliseconds.
- **Stability and contingency**: N-1 security, fault detection, and dynamic stability analysis.

## Code pattern

```python
import pandapower as pp
import pandapower.networks as pn

net = pn.case_ieee30()
pp.runpp(net)
print(net.res_bus.vm_pu.min(), net.res_bus.vm_pu.max())
```

## Tuning notes

- Respect physical constraints (voltage limits, thermal limits, generator ramp rates).
- Use probabilistic forecasts and reserve scheduling for renewables and demand uncertainty.
- Neural surrogates should be validated against conventional solvers and checked for feasibility.

## Verification

1. Run a power flow on an IEEE benchmark and inspect bus voltages and branch loadings.
2. Train a PV/wind or load forecaster and backtest with rolling cross-validation.
3. Compare a neural OPF surrogate to a conventional solver on a held-out grid.

## References

- https://www.pandapower.org/start/
- https://github.com/microsoft/gridsfm
- https://research.ibm.com/blog/gridfm-neural-solver-power-grid
- https://doi.org/10.1016/j.egyai.2026.100842
