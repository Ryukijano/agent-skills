# AI for Condensed Matter

## Description

Use machine learning to classify phases, learn interatomic potentials, and emulate quantum many-body and density-functional calculations.

## When to use

You are identifying phases and order parameters, learning interatomic potentials, or emulating quantum many-body Hamiltonians.

## Usage

- Classify spin, electronic, and structural phases across phase diagrams.
- Learn neural-network interatomic potentials and DFT exchange-correlation surrogates.
- Identify topological invariants and hidden order parameters.
- Emulate quantum many-body systems with neural quantum states and tensor networks.

## Steps

1. Generate or load spin, electronic, and structural configurations with phase labels near critical points.
2. Design symmetry-respecting descriptors or graph representations for the material.
3. Train a classifier, neural potential, or DFT surrogate with physics-aware featurization.
4. Validate generalization at critical points, topological boundaries, and unseen compositions.
5. Use the model to screen structures or accelerate molecular-dynamics and DFT workflows.

## Code pattern

```python
import numpy as np
from sklearn.neural_network import MLPClassifier

# Classify spin configurations from a 2D Ising model
configs = np.load("ising_configs.npy")
labels = np.load("ising_labels.npy")
clf = MLPClassifier(hidden_layer_sizes=(128, 64), max_iter=500).fit(configs, labels)
```

## Tuning notes

- Choose descriptors that respect lattice and gauge symmetries.
- Use transfer learning across related Hamiltonians when data is scarce.
- Check generalization near critical points and topological phase boundaries.

## Verification

1. Classify ordered versus disordered Ising phases and locate the critical point.
2. Train an ML potential for a small molecule or crystal and validate energies.
3. Identify a topological phase from entanglement or Wilson-loop data.

## References

- https://doi.org/10.1088/1361-648x/abb895
- https://www.nature.com/articles/nphys4035
- https://doi.org/10.1103/revmodphys.91.045002
- https://www.nature.com/articles/s41524-019-0221-0
