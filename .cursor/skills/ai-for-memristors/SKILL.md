# AI for Memristors

## Description

Crossbar array modeling, compute-in-memory mapping, device variability learning, and memristor-based AI accelerator co-design.

## When to use

You are building or simulating memristor crossbars, compute-in-memory tiles, or analog AI accelerators based on resistive switching.

## Key concepts

- **Memristor device models**: learning compact models (e.g., ODE-based, physics-informed) from I-V and pulse data.
- **Crossbar MVM**: mapping weights to conductance states and simulating analog matrix-vector multiplication with nonidealities.
- **Variability and yield**: ML predicts device-to-device and cycle-to-cycle variation effects on inference accuracy.
- **Hardware-software co-design**: mixed-precision memristor + SRAM CIM partitioning for accuracy and energy.

## Code pattern

```python
import numpy as np

# Analog MVM on a memristor crossbar with device variation
G = np.random.lognormal(mean=0.0, sigma=0.1, size=(m, n)) * G_target
I = G @ x
y = adc_quantize(I, bits=4)
```

## Tuning notes

- Calibrate conductance programming with closed-loop write-and-verify schemes.
- Model nonidealities (line resistance, sneak paths, noise, retention) at the circuit level.
- Use bit-slicing and hybrid digital/analog tiles to mitigate variability for precision-sensitive layers.

## Verification

1. Fit a neural or physics-informed surrogate to measured memristor I-V curves.
2. Simulate an MLP layer on a crossbar and measure accuracy degradation under device variation.
3. Compare the energy-delay product of a memristor CIM tile to a digital baseline for the same workload.

## References

- https://www.nature.com/articles/s41928-025-01537-5
- https://www.nature.com/articles/s41586-025-08639-2
- https://www.nature.com/articles/s41467-025-61025-4
- https://www.nature.com/articles/s44172-025-00461-y
