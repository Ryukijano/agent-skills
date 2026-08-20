# Analog Computing

## Description

Reconfigurable analog accelerators, in-memory analog computing, and mixed-signal AI hardware.

## When to use

You are building or using analog/mixed-signal accelerators where continuous physical quantities directly implement mathematical operations.

## Key concepts

- **Analog computing**: continuous voltages/currents represent variables.
- **Analog in-memory computing (AIMC)**: resistive arrays compute dot products in the analog domain.
- **Reconfigurable analog engines**: switch capacitor/resistor networks to map different kernels.
- **ADC/DAC precision and noise**: analog results must be digitized; converter resolution matters.
- **HW/SW co-design**: algorithm choices must match analog noise and dynamic range.

## Code pattern

```python
import numpy as np

# Idealized analog MAC with finite ADC precision
G = np.random.randn(64, 64)
x = np.random.randn(64)
y_analog = G @ x
# quantize to e.g. 8-bit ADC
y_digital = np.round(y_analog / np.max(np.abs(y_analog)) * 127).astype(np.int8)
```

## Tuning notes

- Quantize weights and activations to match the analog accelerator's bit precision.
- Retrain with noise injection to improve robustness to analog non-idealities.
- Evaluate end-to-end accuracy with a calibrated behavioral model.

## Verification

1. Build a behavioral analog accelerator model in Python.
2. Run a small DNN layer through the model and compare to a digital reference.
3. Sweep noise, ADC bits, and weight drift to find an accuracy operating point.

## References

- https://www.nature.com/articles/s41928-025-01537-5
- https://research.ibm.com/publications/eagle-a-flexible-heterogeneous-analog-compute-in-memory-architecture-with-risc-v-programmable-multi-core-accelerators
- https://doi.org/10.1109/iccd65941.2025.00021
- https://doi.org/10.1109/iedm45741.2023.10413724
