# Qubitization and Walk Operators

## Description

Build qubitization walk operators from a block encoding and measure Chebyshev moments in CUDA-Q Algorithms.

## When to use

You want to perform quantum signal processing on a block-encoded Hamiltonian, such as measuring Chebyshev moments for a Krylov eigensolver or preparing an approximate ground state.

## Usage

- Construct `Walk(encoding)` from any `BlockEncoding`.
- Compute `walk.moments(state, k)` to sample `<T_k(H/alpha)>`.
- Use the moments as input to a classical Krylov or filtering algorithm.

## Steps

1. Prepare or obtain a `BlockEncoding` (`PauliLCU`, custom, etc.).
2. Create `Walk(encoding)`.
3. Provide an initial state (numpy array or CUDA-Q kernel).
4. Measure the first `k` Chebyshev moments.
5. Post-process the moments classically (e.g., Lanczos/Krylov).

## Code pattern

```python
from cudaq_algorithms import PauliLCU, Walk
import numpy as np

encoding = PauliLCU({"ZZ": 0.5, "XI": 0.3, "IX": 0.3})
walk = Walk(encoding)
state = np.array([1, 0, 0, 0], dtype=complex)
moments = walk.moments(state, 4)
```

## Tuning notes

- Choose the moment order `k` to balance resolution of the spectrum with circuit depth.
- Ensure the initial state has overlap with the target eigenstate.

## Verification

1. Compare measured moments to dense linear-algebra Chebyshev moments for the same Hamiltonian.
2. Run on `qpp-cpu` and verify convergence as `k` increases.
3. Cross-check the ground-state energy from a Krylov solve against exact diagonalization.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/1610.0653
