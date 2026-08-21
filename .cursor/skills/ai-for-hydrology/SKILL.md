# AI for Hydrology

## Description

Use ML and physics-informed models to predict rainfall-runoff, forecast streamflow, predict floods, and build digital twins for water systems.

## When to use

You are modeling rainfall-runoff, streamflow, floods, or water quality and want data-driven forecasts or surrogates.

## Usage

- Predict discharge from precipitation and catchment properties.
- Forecast streamflow with LSTM, transformers, or NARX time-series models.
- Classify or forecast flood events from meteorological and hydrological inputs.
- Embed mass and momentum conservation with PINNs and build real-time digital twins of water systems.

## Steps

1. Collect precipitation, streamflow, catchment attributes, and weather data for target basins.
2. Normalize inputs by catchment area and long-term statistics; engineer lag and sequence features.
3. Train a rainfall-runoff or streamflow model (LSTM, transformer, NARX) and evaluate with NSE/KGE/bias.
4. Build a flood-forecasting or classification pipeline and validate on extreme events not seen in training.
5. Add physics-informed constraints or a digital-twin layer that assimilates real-time sensor data.
6. Compare with conceptual/physical hydrologic models and deploy the best model for operational forecasting.

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
