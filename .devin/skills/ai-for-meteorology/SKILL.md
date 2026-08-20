# AI for Meteorology

## Description

Numerical weather prediction emulators, precipitation nowcasting, extreme-weather detection, and weather foundation models.

## When to use

You need to forecast weather, downscale climate output, nowcast precipitation, or detect extreme-weather events.

## Key concepts

- **Nowcasting**: short-term (<6 h) prediction of precipitation and storms from radar/satellite.
- **NWP emulators and surrogates**: ML models that emulate or bias-correct numerical weather prediction.
- **Foundation models**: GraphCast, FourCastNet, Pangu-Weather, FengWu, ClimaX.
- **Downscaling and bias correction**: super-resolution and statistical adjustment of model output.
- **Extreme weather detection**: identify tropical cyclones, atmospheric rivers, and convective hazards.

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
