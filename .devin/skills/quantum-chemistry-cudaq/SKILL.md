# Quantum Chemistry with CUDA-Q Algorithms

## Description

End-to-end quantum chemistry workflows from PySCF molecular integrals to CUDA-Q ground-state calculations.

## When to use

You want to compute molecular ground-state energies or simulate electronic structure with a CUDA-Q algorithm using realistic chemistry inputs.

## Usage

- Run a PySCF mean-field calculation to obtain molecular integrals.
- Build a Jordan–Wigner or Bravyi–Kitaev Hamiltonian.
- Choose a block encoding and a solver (qubitization moments + Krylov, QSVT, Trotter).
- Verify the result against full configuration interaction for small molecules.

## Steps

1. Install PySCF and `cudaq-algorithms`.
2. Define a molecule and basis, then run PySCF RHF/UHF.
3. Extract one- and two-electron integrals.
4. Map fermion to qubit and create a `PauliLCU` (or double-factorized) encoding.
5. Build `Walk` or `QSVT` and compute ground-state energy.
6. Compare to FCI or experimental reference.

## Code pattern

```python
from pyscf import gto, scf
from cudaq_algorithms import jordan_wigner, PauliLCU, Walk

mol = gto.M(atom='H 0 0 0; H 0 0 0.74', basis='sto-3g')
mf = scf.RHF(mol).run()
hpq, hpqrs = mf.get_hcore(), mol.intor('int2e')
qubit_h = jordan_wigner(hpq, hpqrs)
encoding = PauliLCU(qubit_h)
walk = Walk(encoding)
```

## Tuning notes

- Use a minimal basis (`sto-3g`) for verification, then scale up.
- Double factorization reduces qubit/gate cost for larger active spaces.
- Active-space selection controls the number of correlated electrons and orbitals.

## Verification

1. Compare CUDA-Q ground-state energy to PySCF FCI for a small molecule.
2. Check that the mean-field energy from PySCF matches the Hartree–Fock reference.
3. Vary the active space and confirm convergence toward the full-basis limit.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://pyscf.org/
- https://github.com/NVIDIA/cudaq-algorithms
