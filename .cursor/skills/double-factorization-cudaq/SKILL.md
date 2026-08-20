# Double Factorization for CUDA-Q

## Description

Use double factorization block encodings to reduce the cost of quantum chemistry Hamiltonians in CUDA-Q Algorithms.

## When to use

You are simulating a molecule or material with many orbitals and need a more compact block encoding than a naive Pauli LCU.

## Usage

- Decompose the two-electron tensor into auxiliary factors.
- Build a double-factorized block encoding.
- Swap the encoding into a `Walk` or `QSVT` workflow without changing downstream code.

## Steps

1. Compute one- and two-electron integrals from PySCF or a model Hamiltonian.
2. Run a double-factorization routine (e.g., ERI factorization).
3. Construct the `BlockEncoding` object from the factorized form.
4. Use it with `Walk` or `QSVT` exactly as you would with `PauliLCU`.

## Code pattern

```python
from cudaq_algorithms import DoubleFactorization, Walk

# factors and one-body terms obtained from factorization
encoding = DoubleFactorization(one_body, two_body_factors)
walk = Walk(encoding)
```

## Tuning notes

- Truncate small factors to balance accuracy and circuit depth.
- For large systems, combine with active-space truncation.
- Compare Pauli LCU and double-factorization resources for the same molecule.

## Verification

1. Confirm the factorized Hamiltonian reproduces the original two-electron integrals.
2. Compare ground-state energy from `Walk` with double factorization to FCI or Pauli-LCU results.
3. Track qubit and gate counts as a function of factorization rank.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/2103.14750
