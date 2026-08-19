# CUDA-Q Hybrid Quantum-Classical Computing

## Description

CUDA-Q kernels, simulators, VQE/QAOA, PyTorch/JAX integration, and multi-GPU quantum workflows.

## When to use

You are exploring hybrid quantum-classical algorithms or quantum machine learning on NVIDIA GPUs.

## Key concepts

- **CUDA-Q kernel**: `@cudaq.kernel` (Python) or `__qpu__` (C++).
- **Execution primitives**: `cudaq.sample`, `cudaq.observe`, `cudaq.get_state`.
- **Backends**: `nvidia` (GPU state vector), `tensornet` (multi-GPU tensor network), `qpp-cpu`.
- **VQE / QAOA**: variational circuits with parameter-shift gradients and built-in optimizers.
- **Hybrid workflows**: integrate quantum kernels with PyTorch or JAX loss functions.

## Code pattern

```python
import cudaq

@cudaq.kernel
def ansatz(theta: float):
    q = cudaq.qubit()
    rx(theta, q)

@cudaq.kernel
def hamiltonian():
    q = cudaq.qubit()
    mz(q)

res = cudaq.observe(ansatz, hamiltonian, 0.5)
```

## Tuning notes

- For 33+ qubits, use `tensornet` or multi-GPU state vector.
- `density-matrix-cpu` for noisy simulation.
- Installation: `pip install cudaq`; for multi-GPU, install with MPI.

## Verification

1. Run a 10-qubit GHZ circuit and compare `sample` counts to theoretical distribution.
2. Run a small VQE on a 2-qubit Hamiltonian and check convergence.
3. Verify GPU backend is active: `cudaq.set_target("nvidia")`.

## References

- https://nvidia.github.io/cuda-quantum/latest/using/basics/kernel_intro.html
- https://nvidia.github.io/cuda-quantum/latest/using/backends/simulators.html
- https://nvidia.github.io/cuda-quantum/latest/applications/python/vqe_advanced.html
- https://nvidia.github.io/cuda-quantum/latest/applications/python/hybrid_quantum_neural_networks.html
