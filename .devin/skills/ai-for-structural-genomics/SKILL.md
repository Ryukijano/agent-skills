# AI for Structural Genomics

## Description

3D genome organization, Hi-C analysis, protein structure prediction with deep learning, and multiscale structural modeling.

## When to use

You are studying the three-dimensional organization of genomes, protein structures, or chromatin conformations and need to predict, analyze, or model spatial molecular structures.

## Key concepts

- **3D genome organization**: chromatin loops, topologically associating domains (TADs), and A/B compartments.
- **Hi-C and related assays**: chromosome conformation capture at scale.
- **Protein structure prediction**: AlphaFold and related deep learning models.
- **Multiscale modeling**: integrating sequence, imaging, and polymer physics.
- **Structural variation**: linking genome folding to gene regulation and disease.

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
