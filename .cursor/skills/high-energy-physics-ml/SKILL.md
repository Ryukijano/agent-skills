# High-Energy Physics and LHC ML

## Description

Jet tagging, event reconstruction, Particle Transformer, Hypergraph, and ROOT/Geant4 integration on GPU.

## When to use

You are applying ML to particle physics data from the LHC or similar experiments.

## Key concepts

- **Jet tagging**: GNNs, Particle Transformer (ParT), point-cloud jets.
- **Event reconstruction**: particle-flow, full-event reconstruction.
- **Hypergraph networks**: for complex decay chains.
- **ROOT/Geant4**: standard HEP data and simulation tools.

## Code pattern

```python
import torch
from particle_transformer import ParticleTransformer

model = ParticleTransformer(in_channels=4, num_classes=5)
model = model.to('cuda')
```

## Tuning notes

- HEP datasets are large but sparse; use efficient data loaders (uproot, awkward-array).
- Physical symmetries (Lorentz, permutation) matter.
- Inference must fit within trigger/online latency budgets.

## Verification

1. Train a jet tagger and compare ROC-AUC to a baseline.
2. Process a ROOT file through a PyTorch DataLoader.
3. Measure inference time per event on target hardware.

## References

- https://arxiv.org/abs/2601.17554
- https://github.com/key4hep/k4MLJetTagger
- https://link.springer.com/article/10.1140/epjc/s10052-023-11677-7
- https://uproot.readthedocs.io/
