# AI for Energy Grid

## Description

Solve AC optimal power flow with neural surrogates to schedule generation and integrate renewables within milliseconds.

## When to use

You are building, operating, or studying power systems with high renewable penetration and need fast, scalable, and physically consistent predictions or optimizations.

## Usage

- Solve or approximate AC/DC power flow and Optimal Power Flow (OPF) with neural surrogates.
- Forecast solar, wind, and demand with probabilistic time-series models.
- Monitor grid stability, fault detection, and N-1 contingency security in real time.
- Deploy grid foundation models (e.g., GridSFM, OpenGridFM, GridFM) for millisecond dispatch decisions.

## Steps

1. Build or load a grid model (e.g., pandapower IEEE case or a real network) and define constraints (voltage, thermal, generator limits).
2. Train a neural surrogate or foundation model to predict power-flow/OPF solutions from load and generation inputs.
3. Implement probabilistic solar, wind, and load forecasting with rolling cross-validation.
4. Run stability and N-1 contingency checks, flagging constraint violations and critical branches.
5. Compare the neural OPF surrogate to a conventional solver on held-out operating conditions and check feasibility.
6. Deploy the fastest-acceptable model in a control room or market-clearing loop with uncertainty-aware reserve scheduling.

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
