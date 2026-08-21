# AI for Biophysics

## Description

Use machine learning to learn molecular dynamics, map free-energy landscapes, and extract kinetics from single-molecule measurements.

## When to use

You are analyzing molecular dynamics trajectories, predicting free energies, or extracting kinetics from single-molecule measurements.

## Usage

- Learn neural-network potentials and coarse-grained models for biomolecular dynamics.
- Build Markov state models and free-energy landscapes from MD trajectories.
- Coarse-grain high-dimensional motion into interpretable collective variables.
- Segment single-molecule FRET and force-spectroscopy traces.

## Steps

1. Load and align MD trajectories or single-molecule time series.
2. Choose physically meaningful collective variables or learned embeddings.
3. Train a neural potential, Markov state model, or hidden-Markov model.
4. Validate against experimental observables such as NMR, FRET, or cryo-EM.
5. Use the model to predict rare events, binding kinetics, or free-energy differences.

## Code pattern

```python
import mdtraj
from sklearn.decomposition import PCA

# Reduce dimensionality of a protein trajectory
traj = mdtraj.load("trajectory.xtc", top="topology.pdb")
coords = traj.xyz.reshape(traj.n_frames, -1)
pca = PCA(n_components=2).fit_transform(coords)
```

## Tuning notes

- Choose collective variables with clear physical meaning.
- Validate against experimental observables (NMR, FRET, cryo-EM).
- Use uncertainty-aware models and enhanced sampling for rare events.

## Verification

1. Build a Markov state model and compare implied timescales.
2. Predict a binding free energy with a neural potential.
3. Segment single-molecule FRET trajectories into metastable states.

## References

- https://doi.org/10.1063/5.0248589
- https://doi.org/10.1063/5.0082179
- https://doi.org/10.1146/annurev-physchem-042018-052331
- https://doi.org/10.1016/j.sbi.2023.102569
