# Quantum Machine Learning

## Description

Hybrid quantum-classical ML with variational quantum circuits, PennyLane, TensorFlow Quantum, and Qiskit.

## When to use

You are exploring whether parameterized quantum circuits can improve expressivity or efficiency for small, structured ML problems.

## Key concepts

- **Variational Quantum Circuits (VQCs)**: parameterized gates optimized classically.
- **Quantum embeddings**: amplitude/angle encoding of classical data.
- **Hybrid quantum-classical models**: combine a small quantum co-processor with a neural network.
- **PennyLane / TFQ / Qiskit**: frameworks for differentiable quantum circuits.
- **Barren plateaus**: watch for vanishing gradients in deep unstructured circuits.

## Code pattern

```python
import pennylane as qml
import torch

dev = qml.device("default.qubit", wires=2)

@qml.qnode(dev, interface="torch")
def qnode(inputs, weights):
    qml.AngleEmbedding(inputs, wires=range(2))
    qml.BasicEntanglerLayers(weights, wires=range(2))
    return qml.expval(qml.PauliZ(0))
```

## Tuning notes

- Use data re-uploading or feature maps carefully to avoid exponential qubit needs.
- Start with small circuits and simulators; real hardware is noisy and expensive.
- Regularize to avoid overfitting on tiny quantum datasets.

## Verification

1. Train a VQC binary classifier on a 2D toy dataset.
2. Compare test accuracy to a classical MLP on the same data.
3. Analyze gradient variance across circuit depth (barren-plateau check).

## References

- https://pennylane.ai
- https://www.tensorflow.org/quantum
- https://github.com/tensorflow/quantum
- https://github.com/PennyLaneAI/pennylane-qiskit
