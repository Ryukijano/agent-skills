# AI for Gas Utilities

## Description

Machine learning for natural gas demand forecasting, pipeline leak detection, compressor optimization, and asset integrity.

## When to use

You operate a natural gas distribution or transmission network and need to forecast demand, detect leaks, optimize compression, or manage asset integrity.

## Usage

- **Short-term gas demand and line-pack forecasting**: predict consumption and network storage.
- **Pipeline leak detection and localization**: identify and locate leaks from pressure and flow data.
- **Asset condition and risk-based maintenance**: prioritize inspections and replacements.
- **Customer and billing analytics**: detect anomalies and support demand-side programs.

## Steps

1. Collect flow, pressure, temperature, and weather data across the network.
2. Build network topology and asset condition datasets.
3. Train forecasting, classification, or optimization models.
4. Validate with geographical and temporal holdouts.
5. Integrate with SCADA, GIS, and enterprise asset management.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Forecast short-term gas demand from weather and calendar
X = df[["temperature", "hour", "day_of_week", "industrial_load"]]
y = df["gas_demand"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Gas demand is highly weather and industrial-driven; include heating-degree days.
- Leak detection needs real-time pressure and flow monitoring plus ground truthing.
- Ensure safety and regulatory compliance for any automated control.

## Verification

1. Backtest demand forecasts against actual city-gate or customer consumption.
2. Evaluate leak detection precision and recall on confirmed incidents.
3. Measure compressor energy savings from optimized scheduling.

## References

- https://doi.org/10.3390/en19041101
- https://www.mdpi.com/1996-1073/17/21/5517
- https://www.osti.gov/biblio/1996417
- https://doi.org/10.3389/fenvs.2025.1569621
