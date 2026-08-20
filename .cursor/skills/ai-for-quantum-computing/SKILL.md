# AI for Quantum Computing

## Description

Machine learning for quantum state tomography, variational quantum algorithms, quantum control, and error mitigation.

## When to use

You are designing variational circuits, optimizing quantum controls, or mitigating errors in NISQ devices.

## Key concepts

- **Variational Quantum Eigensolver (VQE)**: hybrid quantum-classical optimization.
- **Quantum Neural Networks**: parameterized circuits as models.
- **Quantum control with RL/optimization**: pulse shaping and gate design.
- **Error mitigation**: zero-noise extrapolation, probabilistic error cancellation.
- **Simulators**: Qiskit, PennyLane, Cirq, cuQuantum.

## Code pattern

```python
import pennylane as qml

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev)
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(0))

opt = qml.GradientDescentOptimizer(stepsize=0.4)
```

## Tuning notes

- Barren plateaus are a major challenge in deep quantum circuits.
- Use parameter-shift or finite-difference gradients on hardware.
- Simulators are useful; validate on real hardware when feasible.

## Verification

1. Run a VQE for a small molecule on a simulator.
2. Optimize a quantum control pulse to reach a target unitary.
3. Compare a quantum circuit output with and without error mitigation.

## References

- https://pennylane.ai/
- https://qiskit.org/
- https://arxiv.org/abs/2312.06843
- https://developer.nvidia.com/cuquantum
