# Renewable Energy Forecasting and Grid Optimization

## Description

Spatio-temporal diffusion, FNO, attention, and RL for solar/wind forecasting and energy dispatch.

## When to use

You are forecasting solar/wind power or optimizing energy systems with ML.

## Key concepts

- **Solar/wind forecasting**: time-series, spatio-temporal diffusion, FNO, transformers.
- **Grid optimization**: unit commitment, economic dispatch, RL for battery management.
- **Carbon capture scheduling**: integrate forecasts with equipment control.
- **Datasets**: ERA5, NREL, Open Power System Data.

## Code pattern

```python
import torch
from neuralop.models import FNO

fno = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=3, out_channels=1)
fno = fno.to('cuda')
```

## Tuning notes

- Use historical weather and satellite data as inputs.
- Probabilistic forecasts are often required for grid planning.
- RL can reduce operational regret by 76-93% in some battery dispatch tasks.

## Verification

1. Train a wind/solar forecasting model and compare RMSE to persistence baseline.
2. Run an RL battery dispatch simulation and measure cost reduction.
3. Backtest on a held-out year of data.

## References

- https://arxiv.org/abs/2509.06925
- https://www.mdpi.com/2071-1050/18/2/738
- https://www.nrel.gov/
