# AI for Neuroinformatics

## Description

Data science for brain imaging, neural signals, connectomics, and computational neuroscience workflows.

## When to use

You are integrating, analyzing, or sharing large-scale neuroscience data such as neuroimaging, electrophysiology, genomics, and connectomics.

## Key concepts

- **Neuroimaging data formats and pipelines**: NIfTI, CIFTI, BIDS, and tools such as fMRIPrep and FreeSurfer.
- **Electrophysiology and calcium imaging analysis**: spike sorting, local field potentials, and time-series neural data.
- **Brain connectomics and network neuroscience**: structural and functional connectivity, graph theory, and network dynamics.
- **Open neuroscience data repositories and standards**: OpenNeuro, NeuroVault, and data-sharing conventions.
- **Multimodal fusion of neural, genetic, and behavioral data**: integrating across scales and modalities.

## Code pattern

```python
import nibabel as nib
from nilearn import datasets, plotting

# Load and plot a functional brain atlas
atlas = datasets.fetch_atlas_harvard_oxford('cort-maxprob-thr25-2mm')
atlas_img = nib.load(atlas.maps)
plotting.plot_roi(atlas_img, title="Harvard-Oxford Atlas")
```

## Tuning notes

- Use BIDS for data organization and reproducibility.
- Correct for multiple comparisons and control false positives in neuroimaging.
- Report effect sizes and confidence intervals, not just p-values.
- Share preprocessed data and code through open repositories.

## Verification

1. Preprocess an fMRI dataset and derive a group-level connectivity matrix.
2. Train a classifier to decode a cognitive state from EEG or fMRI data.
3. Publish a BIDS-organized dataset and analysis pipeline on an open repository.

## References

- https://doi.org/10.1007/s12021-024-09692-4
- https://doi.org/10.3390/jcm14020550
- https://doi.org/10.1016/j.metrad.2026.100224
- https://www.frontiersin.org/journals/neuroinformatics/articles/10.3389/fninf.2024.1399931/full
