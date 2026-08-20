# Quantum Singular Value Transformation

## Description

Apply polynomial transformations to block-encoded matrices with QSVT in CUDA-Q Algorithms.

## When to use

You need to apply a polynomial function to a matrix (or its inverse, square root, filter, etc.) encoded as a block of a larger unitary.

## Usage

- Build a `QSVT` object from a `BlockEncoding` and a polynomial phase sequence.
- Embed the resulting kernel in a user-defined `@cudaq.kernel`.
- Use it for Hamiltonian simulation, matrix inversion, eigenstate filtering, or signal processing.

## Steps

1. Obtain a `BlockEncoding` for the target matrix.
2. Design a polynomial phase sequence (Chebyshev / Jacobi-Anger expansion) for the desired function.
3. Create `QSVT(encoding, phases)` and compose it with a state-preparation kernel.
4. Execute and post-select or measure the desired observable.

## Code pattern

```python
from cudaq_algorithms import QSVT, PauliLCU
import numpy as np

encoding = PauliLCU({"ZZ": 0.5, "XI": 0.3, "IX": 0.3})
phases = np.array([...])  # angles for target polynomial
qsvt = QSVT(encoding, phases)
```

## Tuning notes

- Degree and phase-angle precision dominate approximation error and circuit depth.
- For Hamiltonian simulation, use Jacobi-Anger expansion of the exponential.
- For eigenstate filtering, use a high-degree polynomial with sharp transition.

## Verification

1. Compare the transformed matrix to the target polynomial computed classically on a small instance.
2. Verify unitarity and the block structure of the constructed kernel.
3. Test that the output state overlaps with the expected filtered state.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://arxiv.org/abs/2105.02859
- https://github.com/NVIDIA/cudaq-algorithms
