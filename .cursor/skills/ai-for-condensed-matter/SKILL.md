# AI for Condensed Matter

## Description

Machine learning for phase classification, topological order, Hamiltonian learning, density functional surrogates, and quantum many-body systems.

## When to use

You are identifying phases and order parameters, learning interatomic potentials, or emulating quantum many-body Hamiltonians.

## Key concepts

- **Order parameters and phase transitions**: supervised classification of spin and electronic configurations.
- **Topological invariants**: learning hidden order without local order parameters.
- **ML potentials and DFT surrogates**: neural-network potentials and exchange-correlation functionals.
- **Quantum many-body systems**: tensor networks, neural quantum states, and variational ansätze.

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
