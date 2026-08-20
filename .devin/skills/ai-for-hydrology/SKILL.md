# AI for Hydrology

## Description

Rainfall-runoff modeling, streamflow forecasting, flood prediction, and physics-informed deep learning for water systems.

## When to use

You are modeling rainfall-runoff, streamflow, floods, or water quality and want data-driven forecasts or surrogates.

## Key concepts

- **Rainfall-runoff modeling**: predict discharge from precipitation and catchment properties.
- **Streamflow forecasting**: use LSTM, transformers, or NARX networks for time-series prediction.
- **Flood prediction**: classify or forecast flood events from meteorological and hydrological inputs.
- **Physics-informed neural networks (PINNs)**: embed mass and momentum conservation into neural networks.
- **Digital twins**: integrate real-time sensor data with AI models for operational forecasting.

## Code pattern

```python
import torch

class LSTMFlow(torch.nn.Module):
    def __init__(self, input_dim, hidden_dim, num_layers):
        super().__init__()
        self.lstm = torch.nn.LSTM(
            input_dim, hidden_dim, num_layers, batch_first=True
        )
        self.fc = torch.nn.Linear(hidden_dim, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

model = LSTMFlow(input_dim=5, hidden_dim=64, num_layers=2)
```

## Tuning notes

- Normalize inputs by catchment area and long-term statistics.
- Choose appropriate sequence length and lag structure for the basin response time.
- Use NSE, KGE, and bias metrics for hydrologic model evaluation.
- Quantify uncertainty with ensembling or Bayesian methods.

## Verification

1. Train an LSTM on rainfall-runoff data and report NSE and KGE on an unseen basin.
2. Compare with a conceptual or physical model for flood events.
3. Validate on an extreme event period not included in the training set.

## References

- https://doi.org/10.3390/w18010119
- https://doi.org/10.1007/s42990-025-00201-6
- https://doi.org/10.1007/s40899-021-00584-y
- https://doi.org/10.3390/w17152281
