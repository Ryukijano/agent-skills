# AI for Immunogenomics

## Description

MHC and peptide binding prediction, TCR/BCR repertoire analysis, epitope and neoantigen prediction, and immunoinformatics.

## When to use

You are studying immune receptor repertoires, MHC-peptide binding, T/B cell responses, neoantigens, or vaccine design and want to predict or analyze immunogenic sequences.

## Key concepts

- **MHC/HLA**: human leukocyte antigen molecules and peptide binding grooves.
- **TCR and BCR repertoires**: V(D)J recombination and clonotype analysis.
- **Epitope prediction**: MHC class I/II binding, antigen processing, and presentation.
- **Neoantigens**: tumor-specific mutations that can elicit T-cell responses.
- **Immunopeptidomics**: mass spectrometry of MHC-presented peptides.

## Code pattern

```python
from mhcflurry import Class1PresentationPredictor

predictor = Class1PresentationPredictor.load()
predictions = predictor.predict(
    peptides=["SIINFEKL", "NLVPMVATV"],
    alleles=["HLA-A*02:01"]
)
print(predictions[["peptide", "mhcflurry_presentation_percentile"]])
```

## Tuning notes

- Choose prediction tools (NetMHCpan, MHCflurry, MixMHCpred) matched to available data.
- Distinguish MHC binding from antigen processing and immunogenicity.
- Account for HLA allele diversity and population coverage.
- Validate in vitro before clinical or vaccine decisions.

## Verification

1. Benchmark MHC predictions against a measured binding or elution dataset.
2. Compare predicted epitopes to NetMHCpan and validate with a subset by experiment.
3. Calculate HLA coverage and neoantigen load for a given population.

## References

- https://doi.org/10.1038/s41541-025-01258-y
- https://doi.org/10.1146/annurev-biodatasci-021920-100259
- https://doi.org/10.1146/annurev-immunol-082119-124838
- https://doi.org/10.1371/journal.pcbi.1006457
- https://doi.org/10.1093/bib/bbz051
