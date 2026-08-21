# AI for Meteorology

## Description

Nowcast extreme precipitation from radar with physics-embedded deep generative models to improve flood and hydropower decisions.

## When to use

You need to forecast weather, downscale climate output, nowcast precipitation, or detect extreme-weather events.

## Usage

- Nowcast precipitation and storms (<6 h) from radar and satellite data.
- Emulate or bias-correct numerical weather prediction (NWP) with fast neural surrogates.
- Apply weather foundation models (GraphCast, FourCastNet, Pangu-Weather, FengWu, Aurora, ClimaX) for medium-range forecasts.
- Downscale and bias-correct model output, and detect tropical cyclones, atmospheric rivers, and convective hazards.

## Steps

1. Ingest radar, satellite, NWP, reanalysis, and climate-projection data for the target region and lead time.
2. Train a precipitation nowcaster (ConvLSTM, diffusion) and compare RMSE/CSI to persistence and NWP baselines.
3. Fine-tune or run a weather foundation model for deterministic or probabilistic medium-range forecasting.
4. Downscale and bias-correct model output with super-resolution or statistical adjustment methods.
5. Detect and track extreme events (cyclones, atmospheric rivers, convective hazards) and compare to labeled databases.
6. Evaluate with CRPS, CSI, Brier score, and physical-conservation metrics, then deploy operationally with ensemble post-processing.

## Code pattern

```python
import torch

class ConvLSTMNowcast(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super().__init__()
        self.encoder = torch.nn.Conv2d(in_channels, hidden_channels, 3, padding=1)
        self.decoder = torch.nn.Conv2d(hidden_channels, 1, 3, padding=1)

    def forward(self, x):
        return self.decoder(torch.relu(self.encoder(x)))

model = ConvLSTMNowcast(in_channels=10, hidden_channels=32)
```

## Tuning notes

- Use physics-informed or constrained loss functions to respect conservation laws.
- Tune lead time, spatial resolution, and input channels for the target variable.
- Apply bias correction and ensembling before operational use.
- Evaluate with CRPS, CSI, and Brier score for probabilistic forecasts.

## Verification

1. Train a precipitation nowcaster and compare RMSE/CSI to persistence and NWP baseline.
2. Fine-tune a weather foundation model on a regional reanalysis and evaluate downscaling.
3. Detect extreme events and compare to a labeled event database.

## References

- https://doi.org/10.3390/atmos16010082
- https://doi.org/10.1016/j.engappai.2025.112335
- https://doi.org/10.48550/arxiv.2501.06907
- https://doi.org/10.5194/gmd-16-6433-2023
