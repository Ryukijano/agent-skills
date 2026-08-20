# Neuromorphic Computing

## Description

Spiking neural networks (SNNs), event-based processing, and brain-inspired low-power accelerators like Intel Loihi and BrainChip.

## When to use

You need ultra-low-power inference, event-based sensing, or brain-inspired temporal computation for edge or robotics workloads.

## Key concepts

- **Spiking Neural Networks (SNNs)**: neurons communicate via discrete spikes over time.
- **Event-based processing**: react to changes rather than frame-based sampling.
- **Neuromorphic hardware**: analog/digital chips (Intel Loihi, BrainChip Akida) that emulate neural dynamics.
- **Surrogate gradients**: train SNNs with backpropagation through time.
- **Neuromorphic sensors**: event cameras (DAVIS, Dynamic Vision Sensor) output spike streams.

## Code pattern

```python
import snntorch as snn
import torch

# Leaky integrate-and-fire neuron
lif = snn.Leaky(beta=0.8)
spk, mem = lif(x, mem)
```

## Tuning notes

- Time constants and spike thresholds strongly affect accuracy and sparsity.
- Use surrogate gradients (e.g., fast sigmoid) for BPTT training.
- Quantize weights and biases for deployment on neuromorphic edge chips.

## Verification

1. Train an SNN classifier on a small spiking dataset (e.g., N-MNIST, DVSGesture).
2. Compare energy and latency to an equivalent ANN on edge hardware.
3. Visualize spike raster and measure mean firing rate.

## References

- https://redwood.berkeley.edu/wp-content/uploads/2021/08/Davies2018.pdf
- https://www.intel.com/content/dam/www/central-libraries/us/en/documents/neuromorphic-computing-loihi-2-brief.pdf
- https://www.nature.com/articles/s41467-024-53827-9
- https://proceedingsoftheieee.ieee.org/advancing-neuromorphic-computing-with-loihi-a-survey-of-results-and-outlook/
