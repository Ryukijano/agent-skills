# AI for Memristors

## Description

Use machine learning to model memristor devices, simulate crossbar arrays, and co-design compute-in-memory accelerators.

## When to use

You are building or simulating memristor crossbars, compute-in-memory tiles, or analog AI accelerators based on resistive switching.

## Usage

- Learn compact device models from I-V and pulse data.
- Simulate analog matrix-vector multiplication on crossbars with device nonidealities.
- Predict device-to-device and cycle-to-cycle variation effects on inference accuracy.
- Co-design mixed-precision memristor and SRAM compute-in-memory tiles.

## Steps

1. Collect memristor I-V, pulse, and endurance data from the target device technology.
2. Fit a neural or physics-informed surrogate to the device behavior.
3. Build a crossbar simulator that models conductance, line resistance, and noise.
4. Run an MLP or kernel layer on the crossbar and measure accuracy under variation.
5. Co-design with digital tiles and quantization to meet accuracy and energy targets.
6. Verify the design against SPICE or measured data and compare energy-delay to a digital baseline.

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
