# Pauli LCU Block Encoding

## Description

Use the linear-combination-of-unitaries (LCU) block encoding for Pauli Hamiltonians in CUDA-Q Algorithms.

## When to use

You need to block-encode a Hamiltonian expressed as a weighted sum of Pauli strings so it can be used by qubitization, QSVT, or other quantum signal-processing routines.

## Usage

- Encode a Pauli Hamiltonian dictionary into a unitary that acts on the system plus an ancilla register.
- Query the subnormalization factor `alpha` and the unitary list for manual inspection or custom kernels.
- Compose the encoding with `Walk` or `QSVT` primitives.

## Steps

1. Represent the Hamiltonian as a dictionary mapping Pauli strings to real coefficients, e.g. `{"ZZ": 0.5, "XI": 0.3}`.
2. Create `PauliLCU(hamiltonian)`.
3. Inspect `encoding.alpha` and `encoding.unitaries`.
4. Pass `encoding` to `Walk(encoding)` or a custom `BlockEncoding`-aware kernel.

## Code pattern

```python
from cudaq_algorithms import PauliLCU

hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
encoding = PauliLCU(hamiltonian)
print("alpha =", encoding.alpha)
print("unitaries =", encoding.unitaries)
```

## Tuning notes

- Keep the number of Pauli terms and the subnormalization factor small to reduce ancilla and gate costs.
- Pauli LCU is convenient for spin/qubit Hamiltonians; for chemistry, consider double factorization for larger systems.

## Verification

1. Reconstruct the encoded Hamiltonian from the block encoding and compare to the input coefficients.
2. Verify the `alpha` matches the sum of absolute Pauli coefficients.
3. Compose with `Walk` and check that Chebyshev moments reproduce the Hamiltonian spectrum on a small system.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/1511.02306
