# AI for Epigenomics

## Description

Use deep learning to predict gene-regulatory states and interpret non-coding variants from DNA methylation, histone marks, chromatin accessibility and 3D contact data.

## When to use

You are working with DNA methylation, histone modifications, chromatin accessibility, or other epigenomic assays and want to predict regulatory states, annotate genomic elements, or integrate epigenomic data with expression or phenotype data.

## Usage

- **Predict DNA methylation**: identify regulatory and imprinting changes from WGBS or array data.
- **Classify enhancers and promoters**: use ChIP-seq marks such as H3K4me3, H3K27ac, and H3K27me3.
- **Model chromatin accessibility**: interpret ATAC-seq and DNase-seq to find open regulatory regions.
- **Link distal elements**: connect enhancers to target genes with 3D contact and HiChIP data.
- **Score variants**: predict the impact of non-coding variants and interpret with motif and attribution analysis.

## Steps

1. Collect and align WGBS, ChIP-seq, ATAC-seq, or array data to the same reference and blacklist.
2. Call peaks or quantify signals, normalize for depth and input control, and annotate genomic regions.
3. Train or load a sequence-to-activity model such as Enformer, Basenji, or Corgi on genomic windows.
4. Annotate enhancers, promoters, and 3D contacts and link distal elements to target genes.
5. Score variants and interpret predictions with motif analysis and attribution maps.
6. Validate predicted regulatory effects against reporter assays, RNA-seq, or matched epigenomic profiles.

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
