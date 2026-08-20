# AI for Neuromorphic Hardware

## Description

Spiking neural network training, SNN-to-chip mapping, event-based processing, and co-design with analog/mixed-signal neuromorphic platforms.

## When to use

You are programming or designing neuromorphic chips (e.g., Loihi, TrueNorth, BrainScaleS, SpiNNaker) and need to train and deploy SNNs.

## Key concepts

- **Spiking neural networks (SNNs)**: event-driven, sparse computation with temporal dynamics.
- **Training methods**: surrogate gradients, ANN-to-SNN conversion, and direct SNN training with time-to-first-spike coding.
- **Chip mapping**: mapping neurons/synapses to cores, on-chip learning, and spike routing constraints.
- **Event-based sensing**: pairing DVS cameras and silicon cochleas with neuromorphic processors.

## Code pattern

```python
import snntorch as snn
import torch

# Leaky integrate-and-fire neuron
lif = snn.Leaky(beta=0.9)
spk, mem = lif(cur_in, mem_prev)
```

## Tuning notes

- Choose time constants and thresholds that match the target neuromorphic hardware.
- Balance accuracy with spike sparsity to maximize energy efficiency.
- Validate on the target chip or a cycle-accurate simulator, not just a software backend.

## Verification

1. Train an SNN classifier on a neuromorphic dataset (e.g., N-MNIST, DVS Gesture) and report accuracy vs. event count.
2. Map an SNN to a Loihi/SpiNNaker core graph and verify spike routing feasibility.
3. Measure energy per spike on the target neuromorphic hardware for a keyword-spotting task.

## References

- https://arxiv.org/abs/1901.03690
- https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2022.795876/full
- https://impact.ornl.gov/en/publications/a-review-of-spiking-neuromorphic-hardware-communication-systems/
- https://www.frontiersin.org/journals/neuroscience/articles/10.3389/fnins.2021.667011/full
