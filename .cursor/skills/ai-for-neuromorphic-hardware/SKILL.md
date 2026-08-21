# AI for Neuromorphic Hardware

## Description

Use machine learning to train spiking neural networks and map them to neuromorphic chips such as Loihi and SpiNNaker.

## When to use

You are programming or designing neuromorphic chips (e.g., Loihi, TrueNorth, BrainScaleS, SpiNNaker) and need to train and deploy SNNs.

## Usage

- Train event-driven SNNs with surrogate gradients, ANN-to-SNN conversion, or direct time-to-first-spike coding.
- Map neurons and synapses to cores while respecting on-chip learning and routing constraints.
- Pair DVS cameras and silicon cochleas with neuromorphic processors for event-based sensing.
- Balance accuracy with spike sparsity for energy-efficient inference.

## Steps

1. Choose a neuromorphic chip or simulator (Loihi, TrueNorth, BrainScaleS, SpiNNaker).
2. Prepare an event-based dataset (N-MNIST, DVS Gesture) and preprocess spikes.
3. Train the SNN with surrogate gradients or conversion and tune time constants.
4. Map the SNN to cores and verify spike routing feasibility.
5. Validate accuracy and event count on the target simulator or hardware.
6. Measure energy per spike and latency for the target workload.

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
