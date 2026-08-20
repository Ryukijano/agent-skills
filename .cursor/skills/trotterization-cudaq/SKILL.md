# Trotterization with CUDA-Q Algorithms

## Description

Simulate Hamiltonian time evolution using Trotter-Suzuki decomposition in CUDA-Q Algorithms.

## When to use

You need a short-time or long-time evolution of a qubit or fermionic Hamiltonian and want a first- or higher-order Trotter circuit.

## Usage

- Decompose the Hamiltonian into local terms and build a Trotter circuit.
- Control the step size, order, and number of Trotter steps.
- Integrate state preparation into the same `@cudaq.kernel`.

## Steps

1. Define or import the Hamiltonian as Pauli strings or from a chemistry workflow.
2. Instantiate `Trotter(hamiltonian, order, trotter_steps)`.
3. Optionally prepare an initial state with a CUDA-Q kernel.
4. Set a CUDA-Q target and sample/expectation values at the final time.

## Code pattern

```python
from cudaq_algorithms import Trotter

hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
unitary = Trotter(hamiltonian, order=1, trotter_steps=4, time=1.0)
```

## Tuning notes

- Reduce Trotter error by decreasing the step size or increasing the Suzuki order.
- For long-time evolution, combine Trotter with qubitization/QSP for better scaling.
- Match the gate set to the target QPU or simulator.

## Verification

1. Compare the final state or expectation value to a small-scale exact diagonalization.
2. Check convergence with decreasing step size.
3. Verify energy conservation for a closed system.

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/1612.09584
