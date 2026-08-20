# CUDA-Q Algorithms

## Description

Build and compose fault-tolerant quantum programs with the CUDA-Q Algorithms library: Pauli LCU, qubitization, QSVT, Trotter, state preparation, and quantum chemistry utilities.

## When to use

You are designing or prototyping fault-tolerant quantum algorithms on CUDA-Q and need reusable, composable primitives rather than writing circuit construction from scratch.

## Usage

- **Block encodings**: encode a Hamiltonian as a unitary with `PauliLCU` or custom `BlockEncoding` objects.
- **Qubitization**: build a walk operator from an encoding and measure Chebyshev moments with `Walk`.
- **QSVT**: apply polynomial transformations to a block-encoded matrix.
- **Trotterization**: simulate time evolution of a Hamiltonian.
- **State preparation**: prepare Hartree–Fock or Givens-rotation Slater determinants inside a CUDA-Q kernel.
- **Quantum chemistry**: connect PySCF integrals to Jordan–Wigner Hamiltonians and ground-state workflows.

## Steps

1. Install `cudaq-algorithms` alongside `cudaq` (`pip install cudaq-algorithms`).
2. Import `PauliLCU`, `Walk`, `QSVT`, `Trotter`, and state-prep utilities.
3. Build a Hamiltonian from a Pauli dictionary or from PySCF molecular integrals.
4. Create a `BlockEncoding`, then compose it with `Walk` or `QSVT` inside a `@cudaq.kernel`.
5. Set a CUDA-Q target (`qpp-cpu`, `nvidia`, etc.) and run/verify against a classical reference.

## Code pattern

```python
import cudaq
import numpy as np
from cudaq_algorithms import PauliLCU, Walk

@cudaq.kernel
def main():
    q = cudaq.qvector(2)

# Block-encode a Pauli Hamiltonian
hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
encoding = PauliLCU(hamiltonian)
walk = Walk(encoding)

state = np.array([1, 0, 0, 0], dtype=complex)
moments = walk.moments(state, 4)
print(moments)
```

## Tuning notes

- Choose the encoding (Pauli LCU vs. double factorization) to match your Hamiltonian sparsity and the target number of logical qubits.
- Use `qpp-cpu` for algorithm validation before moving to `nvidia` or physical backends.
- Capture large molecular integrals as numpy arrays and pass them into the CUDA-Q kernel with the `BlockEncoding` interface.

## Verification

1. Compare Chebyshev moments to a dense matrix calculation.
2. Verify ground-state energies against full configuration interaction for a small molecule.
3. Test the same workflow with two different block encodings to ensure they give consistent results.

## References

- https://github.com/NVIDIA/cudaq-algorithms
- https://nvidia.github.io/cudaq-algorithms/
- https://nvidia.github.io/cuda-quantum/blogs/blog/2026/08/18/cudaq-algorithms-0.1/
