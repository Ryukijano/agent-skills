# AI for Biophysics

## Description

Machine learning for molecular dynamics, free-energy landscapes, protein-ligand kinetics, single-molecule analysis, and membrane systems.

## When to use

You are analyzing molecular dynamics trajectories, predicting free energies, or extracting kinetics from single-molecule measurements.

## Key concepts

- **Molecular dynamics and force fields**: ML potentials and coarse-grained models.
- **Free energy and kinetics**: Markov state models, umbrella sampling, and metadynamics.
- **Coarse graining**: learning low-dimensional representations of biomolecular motion.
- **Single-molecule biophysics**: hidden Markov models and dwell-time analysis.

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
