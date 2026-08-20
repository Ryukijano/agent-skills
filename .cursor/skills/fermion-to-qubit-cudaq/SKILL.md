# Fermion-to-Qubit Mappings in CUDA-Q

## Description

Map fermionic operators to qubit operators using Jordan–Wigner, Bravyi–Kitaev, and other schemes for quantum chemistry and materials.

## When to use

You have fermionic creation/annihilation operators (from PySCF, molecular integrals, or a Hubbard model) and need a qubit Hamiltonian for a CUDA-Q algorithm.

## Usage

- Convert one- and two-electron integrals to Pauli strings with Jordan–Wigner or Bravyi–Kitaev.
- Use the Pauli Hamiltonian as input to `PauliLCU`, `Trotter`, or `Walk`.
- Compare mappings for qubit count, locality, and circuit depth trade-offs.

## Steps

1. Obtain molecular or model integrals (e.g., from PySCF `scf.get_hcore()` and `ao2mo`).
2. Choose a mapping (Jordan–Wigner, Bravyi–Kitaev, parity, etc.).
3. Generate the qubit Hamiltonian with `cudaq_algorithms.fermion_to_qubit` or equivalent.
4. Pass the Pauli dictionary to a block-encoding or time-evolution primitive.

## Code pattern

```python
from cudaq_algorithms import jordan_wigner

# h_pq and h_pqrs are numpy arrays of one-/two-electron integrals
qubit_hamiltonian = jordan_wigner(h_pq, h_pqrs)
print(qubit_hamiltonian)
```

## Tuning notes

- Jordan–Wigner is simple but has long Pauli strings.
- Bravyi–Kitaev balances locality and Pauli weight; use it for deeper circuits.
- Parity mapping can reduce qubit count by exploiting symmetries.

## Verification

1. Check that the qubit Hamiltonian reproduces the fermionic spectrum on a small basis.
2. Compare Jordan–Wigner and Bravyi–Kitaev energies for the same integrals.
3. Verify the operator algebra (number of particles, spin symmetries) is preserved.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/1701.08213
