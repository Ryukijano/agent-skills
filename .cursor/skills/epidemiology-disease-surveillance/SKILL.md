# Epidemiological Modeling and Disease Surveillance

## Description

SIR/SEIR models, GNNs, Gaussian processes, and transfer learning for outbreak prediction and disease dynamics.

## When to use

You are modeling infectious disease spread or building surveillance systems.

## Key concepts

- **Compartmental models**: SIR, SEIR, metapopulation models.
- **Agent-based simulations**: contact networks, superspreader events.
- **GNNs**: for spatio-temporal outbreak prediction.
- **Surveillance**: nowcasting, anomaly detection, early warning.

## Code pattern

```python
import torch
from torch_geometric.nn import GCNConv

class EpidemicGNN(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = GCNConv(10, 64)
        self.conv2 = GCNConv(64, 1)
```

## Tuning notes

- Real data is noisy and delayed; use nowcasting to correct reporting delay.
- Combine mechanistic models with ML for hybrid forecasts.
- Respect privacy and ethics in surveillance data.

## Verification

1. Fit an SIR/SEIR model to historical data and compare to observed peaks.
2. Run a GNN forecast and compute MAE/CRPS.
3. Test early-warning system on past outbreaks.

## References

- https://link.springer.com/article/10.1186/s12911-025-03310-2
- https://arxiv.org/html/2411.05556
- https://www.nature.com/articles/s41586-024-08564-w
