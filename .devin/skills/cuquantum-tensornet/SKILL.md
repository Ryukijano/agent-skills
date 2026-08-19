# cuQuantum cuStateVec and cuTensorNet Simulation

## Description

GPU-accelerated quantum simulation: state vector, tensor network, expectation values, and gradients.

## When to use

You are simulating quantum circuits at scale (many qubits) or computing expectation values/gradients for VQE/QAOA.

## Key concepts

- **cuStateVec**: GPU state vector simulator with gate fusion and batched ops.
- **cuTensorNet**: tensor network contractions, exact and approximate (MPS) simulation.
- **Multi-GPU**: distributed state vector (`mgpu`) for 33+ qubits.
- **Expectation + gradients**: `cutensornetExpectationComputeWithGradientsBackward`.

## Code pattern

```python
import cuquantum
import cuquantum.cutensornet as cutn

# Create a tensor network state and compute an expectation value
handle = cutn.create()
# ... build state, add gates, compute
```

For Python high-level usage, use the `cudaq` `tensornet` target.

## Tuning notes

- cuTensorNet hyper-sampling finds good contraction paths.
- For Clifford circuits, use `stim` backend instead of state vector.
- Gate fusion reduces memory movement in cuStateVec.

## Verification

1. Run a 20-qubit GHZ and compare state vector to a CPU simulator.
2. Compute a 1D TFIM expectation value and compare to exact diagonalization.
3. For VQE, check gradient converges with parameter shift.

## References

- https://docs.nvidia.com/cuda/cuquantum/latest/custatevec/overview/index.html
- https://docs.nvidia.com/cuda/cuquantum/latest/cutensornet/overview.html
- https://docs.nvidia.com/cuda/cuquantum/latest/cutensornet/examples/expectation-gradient.html
- https://developer.nvidia.com/cuquantum-sdk
