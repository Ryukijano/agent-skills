# Sports Biomechanics and Injury Prediction

## Description

Wearable sensors, ST-GNNs, federated learning, and multimodal fusion for athlete performance and injury risk.

## When to use

You are analyzing athlete biomechanics, wearable data, or injury risk.

## Key concepts

- **Wearable sensors**: IMU, sEMG, PPG, accelerometers.
- **Skeleton graphs**: spatio-temporal GNNs on human pose.
- **Injury prediction**: load monitoring, recovery, biomechanical markers.
- **Federated learning**: train across teams/institutions without centralizing data.

## Code pattern

```python
import torch
from stgcn import STGCN

model = STGCN(in_channels=3, num_classes=2)
model = model.to('cuda')
```

## Tuning notes

- Data is highly personal; handle privacy carefully.
- Cross-sport transfer can help with limited data.
- Combine video pose estimation with wearable signals.

## Verification

1. Train an ankle injury prediction model and report AUC/sensitivity.
2. Compare injury predictions to actual injury records.
3. Validate with leave-one-athlete-out cross-validation.

## References

- https://doi.org/10.1177/18724981251380391
- https://link.springer.com/article/10.1186/s13102-026-01625-9
- https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1687895/full
