# Neuroscience and Brain ML on GPU

## Description

fMRI, calcium imaging, connectomics, and neural decoding with cuBNM, DeepWonder, scGPT, and RAPIDS.

## When to use

You are analyzing large-scale neural data (imaging, electrophysiology, connectomics) on GPU.

## Key concepts

- **Connectome modeling**: cuBNM for whole-brain network models (Wong-Wang, Jansen-Rit).
- **Calcium imaging**: DeepWonder, DeepCAD-RT, CAPT for denoising and neuron extraction.
- **fMRI/MEG/EEG**: PAGANI, NeuralSet, resting-state analysis.
- **Single-cell**: scVI/scGPT for transcriptomics, RAPIDS cuDF.
- **Neural decoding**: population dynamics, latent variable models.

## Code pattern

```python
# cuBNM example (Python wrapper)
from cubnm import simulations
sim = simulations.Sim(...)
sim.run()
```

For calcium imaging:

```python
# DeepWonder / DeepCAD-RT are deep models run in PyTorch
```

## Tuning notes

- Large imaging datasets need efficient video loading (e.g., Zarr/FFMPEG + dask).
- Connectome models can be highly parallel; use one GPU per subject or model instance.
- Calcium signals are noisy; use self-supervised or synthetic pretraining.

## Verification

1. Run cuBNM on a small connectome and reproduce known BOLD dynamics.
2. Extract neurons from a short calcium video and compare to manual labels.
3. Train scVI on 100k cells and compare latent space to CPU run.

## References

- https://github.com/amnsbr/cubnm
- https://www.nature.com/articles/s41592-023-01838-7
- https://github.com/bowang-lab/scGPT
- https://pmc.ncbi.nlm.nih.gov/articles/PMC6866286/
