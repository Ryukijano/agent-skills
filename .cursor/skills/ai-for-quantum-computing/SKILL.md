# AI for Quantum Computing

## Description

Use machine learning to design, optimize, and error-mitigate variational quantum algorithms and quantum control pulses.

## When to use

You are designing variational circuits, optimizing quantum controls, or mitigating errors in NISQ devices.

## Usage

- Optimize parameterized quantum circuits (VQE, QAOA) with hybrid quantum-classical loops.
- Discover high-fidelity, time-optimal control pulses for quantum gates and state preparation.
- Mitigate hardware noise with learned error models, zero-noise extrapolation, or probabilistic cancellation.
- Accelerate quantum state tomography and characterization from limited measurements.
- Benchmark and compare algorithms on simulators (Qiskit, PennyLane, Cirq) and real NISQ hardware.

## Steps

1. Encode the target problem (molecular Hamiltonian, optimization, or control target) into a quantum circuit or pulse ansatz.
2. Choose a simulator or NISQ backend and define the noise model and device constraints.
3. Optimize circuit parameters or control pulses with a classical optimizer, using parameter-shift or finite-difference gradients.
4. Apply error mitigation (ZNE, learned models, or probabilistic cancellation) to reduce noise in expectation values.
5. Verify results against exact or classically simulable baselines on small problem instances.
6. Benchmark on real hardware when feasible and iterate the ansatz, control, or mitigation strategy.

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
