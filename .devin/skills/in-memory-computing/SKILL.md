# In-Memory Computing

## Description

Compute-in-memory, processing-in-memory, and emerging NVM technologies (PCM, RRAM, MRAM) for AI.

## When to use

You are designing hardware or algorithms that reduce data movement by placing computation inside or near memory arrays.

## Key concepts

- **Compute-in-memory (CIM) / processing-in-memory (PIM)**: perform MACs inside memory arrays.
- **Analog CIM**: use Ohm's law and Kirchhoff's laws for vector-matrix multiplication.
- **Emerging NVMs**: RRAM, PCM, MRAM, FeFET as compute/storage elements.
- **Memory wall**: von Neumann bottleneck driving CIM research.
- **Noise and precision**: analog CIM introduces device and readout noise.

## Code pattern

```python
import numpy as np

# Idealized analog CIM: G stores weights, V is input vector, I is output
G = np.array([[1.0, 0.5], [0.2, 0.9]])  # conductance matrix
V = np.array([0.5, 0.3])                # input voltages
I = G @ V                               # Kirchhoff current summation
```

## Tuning notes

- ADC/DAC and readout circuits often dominate energy and area in analog CIM.
- Weight programming and drift compensation are critical for accuracy.
- Start with behavioral models before taping out analog macros.

## Verification

1. Simulate an ideal conductance-based MAC and compare to digital golden reference.
2. Add conductance noise / quantization and measure accuracy drop on a DNN layer.
3. Compare throughput, energy, and area estimates to a digital baseline.

## References

- https://pmc.ncbi.nlm.nih.gov/articles/PMC12164277/
- https://www.mdpi.com/1424-8220/25/12/3618
- https://link.springer.com/article/10.1007/s11432-023-3789-7
- https://par.nsf.gov/biblio/10649488
