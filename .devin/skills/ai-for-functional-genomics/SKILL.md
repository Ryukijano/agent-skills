# AI for Functional Genomics

## Description

Predicting gene regulatory function from sequence and epigenomic data, mapping cis-regulatory elements, and interpreting non-coding variants.

## When to use

You want to predict gene regulatory function from DNA sequence, map cis-regulatory elements, interpret genetic variants, or link epigenomic and transcriptomic states.

## Key concepts

- **Regulatory grammar**: how TF motifs, chromatin, and sequence context encode activity.
- **Functional assays**: ChIP-seq, ATAC-seq, MPRA, STARR-seq, and CAGE.
- **Sequence-to-function models**: DeepSEA, Basset, Enformer, and Basenji.
- **Variant effect prediction**: scoring non-coding variants for regulatory impact.
- **TF binding and expression**: linking enhancer states to target genes.

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
