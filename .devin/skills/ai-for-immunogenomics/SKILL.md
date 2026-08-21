# AI for Immunogenomics

## Description

Use machine learning to predict MHC-peptide binding, analyze TCR and BCR repertoires, identify epitopes and neoantigens and support vaccine and immunotherapy design.

## When to use

You are studying immune receptor repertoires, MHC-peptide binding, T/B cell responses, neoantigens, or vaccine design and want to predict or analyze immunogenic sequences.

## Usage

- **Predict MHC binding**: score MHC class I/II binding and antigen processing.
- **Analyze repertoires**: study V(D)J recombination and clonotype diversity in TCR and BCR data.
- **Find neoantigens**: identify tumor-specific peptides from somatic mutations and expression.
- **Integrate immunopeptidomics**: use mass spectrometry of HLA-bound peptides for antigen discovery.
- **Model TCR-pMHC pairing**: predict TCR recognition and HLA coverage for personalized vaccines.

## Steps

1. Collect HLA allele information and peptide or repertoire sequencing data.
2. Predict MHC binding, processing, and immunogenicity with NetMHCpan, MHCflurry, or similar.
3. Assemble TCR/BCR clonotypes and analyze repertoire diversity and expansion.
4. Call somatic mutations and expression to predict and prioritize neoantigens.
5. Validate predicted epitopes with binding, elution, or functional assays.
6. Compute population HLA coverage and design vaccine or cell-therapy candidates.

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
