# AI for Structural Genomics

## Description

Use deep learning and polymer modeling to predict 3D genome organization, protein structures and chromatin conformations from sequence and contact data.

## When to use

You are studying the three-dimensional organization of genomes, protein structures, or chromatin conformations and need to predict, analyze, or model spatial molecular structures.

## Usage

- **Predict genome folding**: model chromatin compartments, TADs, loops, and enhancer-promoter contacts.
- **Analyze contact data**: process Hi-C, Micro-C, and capture-C at multiple resolutions.
- **Predict protein structures**: run AlphaFold or related models for relevant genes.
- **Model structural variation**: assess the impact of variants on 3D organization and regulation.
- **Integrate scales**: combine sequence, imaging, and polymer physics for multiscale modeling.

## Steps

1. Align and normalize Hi-C or Micro-C data and choose resolution for the target feature size.
2. Call TADs, compartments, and loops with multiple tools and compare overlaps.
3. Train or apply a sequence-based 3D genome model such as Akita, Orca, or C.Origami.
4. Predict protein structures for relevant genes using AlphaFold or related models.
5. Score structural variants and design in silico perturbations of regulatory elements.
6. Validate 3D predictions with FISH, microscopy, or gene-expression changes.

## Code pattern

```python
import cooler
import numpy as np
import cooltools

c = cooler.Cooler("hic.cool")
mat = c.matrix(balance=True).fetch("chr1:0-10000000")
insulation = cooltools.insulation(c, 100000)
```

## Tuning notes

- Choose resolution (1 kb to 100 kb) based on feature size.
- Apply bias correction (ICE/VC) before downstream analysis.
- Distinguish static structural maps from dynamic conformational ensembles.
- Integrate imaging data (FISH, super-resolution) to validate 3D models.

## Verification

1. Call TADs and loops with multiple tools (cooltools, Arrowhead) and compare overlap.
2. Compare A/B compartments from Hi-C PCA to known epigenomic marks.
3. Validate a predicted 3D structure against FISH or microscopy distances.

## References

- https://doi.org/10.1038/s41576-023-00638-1
- https://doi.org/10.1038/s44320-024-00016-x
- https://doi.org/10.1038/s41576-019-0122-6
- https://doi.org/10.1007/s00018-025-05837-z
