# AI for Oil and Gas

## Description

Use AI for Oil and Gas to interpret seismic and well logs, characterize reservoirs and forecast production.

## When to use

You are interpreting seismic and well-log data, characterizing reservoirs, forecasting production, or monitoring surface facilities and need data-driven or physics-aware models.


## Usage


- **Physics-informed neural networks (PINNs)**: Embed reservoir flow equations for consistent simulation and history matching.
- **Computer vision for core and thin-section analysis**: Automatic mineralogy, pore classification, and fracture detection.
- **Seismic facies and fault interpretation**: CNN and transformer models for structural interpretation.
- **Production forecasting**: LSTM, N-BEATS, and temporal fusion models for decline and well performance.
- **NLP for drilling and completion reports**: Extract nonproductive time, lessons learned, and risk events.

## Steps

1. Collect and prepare seismic, well-log, production and completion data.
2. Interpret seismic and well-log data.
3. Characterize reservoirs.
4. Forecast production.
5. Validate by forecasting monthly oil rate on a blind well with MAPE below 15%.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import torch
import torch.nn as nn

class ProductionLSTM(nn.Module):
    def __init__(self, input_size=5, hidden_size=32, num_layers=2):
        super().__init__()
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

model = ProductionLSTM()
```


## Tuning notes

- Normalize rates, pressures, and temperatures; handle irregular sampling with interpolation or neural ODEs.
- Combine first-principles constraints (mass balance, Darcy flow) for better generalization across wells.
- Use transfer learning from analog reservoirs when target data are limited.
- Validate forecasts against decline-curve and material-balance baselines.


## Verification

1. Forecast monthly oil rate on a blind well with MAPE below 15%.
2. Classify seismic facies and compare predictions to interpreter picks.
3. Solve a 1D Buckley-Leverett flow problem with a PINN and match the analytical solution.

## References

- https://www.sciopen.com/article/10.46690/ager.2025.09.01
- https://doi.org/10.3390/en18020391
- https://link.springer.com/article/10.1007/s44274-026-00797-y
- https://link.springer.com/book/10.1007/978-1-4842-6094-4
