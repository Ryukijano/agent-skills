# AI for Functional Genomics

## Description

Use sequence-to-function models to predict gene-regulatory activity, map cis-regulatory elements and interpret non-coding variants from genomic sequence and epigenomic data.

## When to use

You want to predict gene regulatory function from DNA sequence, map cis-regulatory elements, interpret genetic variants, or link epigenomic and transcriptomic states.

## Usage

- **Map regulatory grammar**: infer TF motifs, chromatin, and sequence context.
- **Integrate assays**: combine ChIP-seq, ATAC-seq, MPRA, STARR-seq, and CAGE data.
- **Train sequence models**: build or apply DeepSEA, Basset, Enformer, Borzoi, or AlphaGenome.
- **Predict variant effects**: score non-coding and fine-mapped GWAS variants.
- **Interpret mechanisms**: link enhancers to genes and explain with motif and attribution analysis.

## Steps

1. Assemble reference genomes, blacklist regions, and collect functional assay data.
2. Preprocess and binarize or quantify regulatory activity across cell types and conditions.
3. Train or load a sequence-to-function model and evaluate on held-out chromosomes.
4. Score non-coding variants and fine-mapped GWAS loci for regulatory impact.
5. Interpret model predictions with motif discovery, attribution, and in silico mutagenesis.
6. Validate predicted regulatory effects with MPRA, reporter assays, or eQTL data.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor

# One-hot encode a DNA sequence (A=1000, C=0100, G=0010, T=0001)
def onehot(seq):
    mapping = {"A": 0, "C": 1, "G": 2, "T": 3}
    arr = np.zeros((len(seq), 4), dtype=int)
    for i, b in enumerate(seq):
        arr[i, mapping[b]] = 1
    return arr.flatten()

X = np.array([onehot(s) for s in sequences])
y = np.array(regulatory_activity)
model = GradientBoostingRegressor(n_estimators=500).fit(X, y)
```

## Tuning notes

- Match model input length to the assay (e.g., 1 kb for ChIP, 100 kb for Enformer).
- Use the same reference genome and avoid train/test leakage across chromosomes.
- Balance classes or use regression losses for continuous activity.
- Interpret with motif and variant scoring, not just overall accuracy.

## Verification

1. Compare predicted regulatory activity to matched ChIP/ATAC signal.
2. Score known GWAS fine-mapped variants and check enrichment in predicted enhancers.
3. Test generalization on a different cell type or held-out chromosome.

## References

- https://doi.org/10.1146/annurev-biodatasci-020722-115651
- https://doi.org/10.1038/s41592-024-02331-5
- https://doi.org/10.1016/j.csbj.2021.07.021
- https://doi.org/10.1038/s41576-019-0122-6
