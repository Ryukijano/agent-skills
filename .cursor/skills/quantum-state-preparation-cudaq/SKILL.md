# Quantum State Preparation with CUDA-Q Algorithms

## Description

Prepare reference quantum states such as Hartree–Fock and Givens-rotation Slater determinants inside CUDA-Q kernels.

## When to use

You need a clean, verifiable reference state (e.g., Hartree–Fock, Slater determinant) as input to a quantum chemistry or algorithm workflow.

## Usage

- Prepare a Hartree–Fock state from occupation numbers.
- Generate a Slater determinant from a Givens-rotation decomposition.
- Compose state preparation with `Walk`, `QSVT`, or `Trotter` in a single kernel.

## Steps

1. Define the number of qubits, occupied spin orbitals, and optional unitary parameterization.
2. Call the state-prep utility or write a `@cudaq.kernel` that applies the Givens rotations.
3. Pass the resulting kernel to `Walk.moments()` or another algorithm primitive.
4. Verify overlap with the classical state vector.

## Code pattern

```python
import cudaq
from cudaq_algorithms import hartree_fock_state, Walk

@cudaq.kernel
def hf_state(n_electrons: int):
    q = cudaq.qvector(4)
    for i in range(n_electrons):
        x(q[i])
```

## Tuning notes

- Use the smallest basis that captures the physics you need; extra virtual orbitals increase circuit depth.
- Givens-rotation circuits are more expressive but deeper than simple HF preparation.

## Verification

1. Compute the prepared state vector on `qpp-cpu` and compare to the classical HF/Slater vector.
2. Check that the state has the correct particle number and symmetry.
3. Combine with a Hamiltonian and verify the energy expectation.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/1812.00954
