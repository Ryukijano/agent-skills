# AI for Epigenomics

## Description

DNA methylation, histone modifications, chromatin accessibility, enhancer-promoter interactions, and deep learning models of gene regulation.

## When to use

You are working with DNA methylation, histone modifications, chromatin accessibility, or other epigenomic assays and want to predict regulatory states, annotate genomic elements, or integrate epigenomic data with expression or phenotype data.

## Key concepts

- **DNA methylation**: CpG and non-CpG methylation patterns, often measured by WGBS or array-based assays.
- **Histone modifications**: ChIP-seq marks such as H3K4me3, H3K27ac, and H3K27me3 that define promoters and enhancers.
- **Chromatin accessibility**: ATAC-seq and DNase-seq that identify open regulatory regions.
- **Enhancer-promoter interactions**: 3D contact data linking distal regulatory elements to target genes.
- **Deep epigenomics models**: DeepSEA, Basenji, and Enformer-style sequence-to-activity predictors.

## Code pattern

```python
import numpy as np
import pyBigWig
from scipy.signal import find_peaks

# Load a bigWig track and scan a region for peaks
bw = pyBigWig.open("H3K27ac.bigWig")
values = np.array([v if v is not None else 0.0 for v in bw.values("chr1", 0, 1000000)])
peaks, _ = find_peaks(values, height=5.0, distance=1000)
```

## Tuning notes

- Use the same reference genome and blacklist regions for all samples.
- Normalize signal for sequencing depth and input control.
- Pay attention to class imbalance when training classifiers on peaks.
- Interpret models with attribution methods (e.g., Integrated Gradients) and motif analysis.

## Verification

1. Call peaks with a standard tool (MACS2/3) and compare overlap with model predictions.
2. Predict known enhancer activity and validate against matched RNA-seq or reporter data.
3. Evaluate the model on held-out chromosomes to estimate generalization.

## References

- https://doi.org/10.1038/nrg3920
- https://doi.org/10.1038/s41576-025-00841-2
- https://doi.org/10.1016/j.compbiomed.2024.109302
- https://doi.org/10.1016/j.bbcan.2021.188588
- https://doi.org/10.3390/biomedicines9111733
