# AI for Smart Grid

## Description

AI and machine learning for load and renewable forecasting, grid state estimation, optimal power flow, and smart-grid control.

## When to use

You are operating or designing a smart power grid and need accurate forecasts, fast state estimation, or scalable grid optimization.

## Usage

- **Load and renewable forecasting**: short- to medium-term predictions for operations and markets.
- **State estimation and bad-data detection**: infer grid states from SCADA and AMI measurements.
- **Optimal power flow surrogates**: accelerate AC OPF with learned approximations.
- **Anomaly and event detection**: identify disturbances, faults, and cyber-physical anomalies.

## Steps

1. Assemble grid topology, historical loads, generation, and weather data.
2. Build or train forecasting, estimation, or OPF-surrogate models.
3. Validate against physical power-flow solvers and held-out operating data.
4. Tune for reliability, latency, and constraint satisfaction.
5. Integrate with energy management, market, or control systems.

## Code pattern

```python
import pandapower as pp
import pandapower.networks as pn

net = pn.case_ieee30()
pp.runpp(net)
print(net.res_bus.vm_pu.min(), net.res_bus.vm_pu.max())
```

## Tuning notes

- Respect voltage, thermal, and ramp-rate constraints in all surrogate outputs.
- Use time-based splits and avoid leakage from future grid states.
- Combine model-based and learning-based approaches for safety-critical decisions.

## Verification

1. Run a power-flow benchmark and compare bus voltages and branch loadings.
2. Backtest a load-forecast model with rolling cross-validation.
3. Evaluate an OPF surrogate against a conventional solver on out-of-sample cases.

## References

- https://www.mdpi.com/1996-1073/18/16/4408
- https://www.mdpi.com/1996-1073/17/6/1381
- https://arxiv.org/html/2507.14117v1
- https://www.mdpi.com/2071-1050/15/6/5453

## References

- https://www.mdpi.com/1996-1073/18/16/4408
- https://www.mdpi.com/1996-1073/17/6/1381
- https://arxiv.org/html/2507.14117v1
- https://www.mdpi.com/2071-1050/15/6/5453
