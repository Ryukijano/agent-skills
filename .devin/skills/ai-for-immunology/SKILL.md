# AI for Immunology

## Description

Machine learning for adaptive immune receptor repertoires, epitope-MHC binding, immune cell phenotyping, and vaccine/immunotherapy design.

## When to use

You are analyzing B-cell or T-cell receptor repertoires, predicting epitope binding, or prioritizing vaccine/immunotherapy candidates.

## Key concepts

- **AIRR**: adaptive immune receptor repertoire sequencing.
- **BCR/TCR clonotypes**: V(D)J rearranged receptor sequences.
- **MHC binding**: peptide presentation by class I and class II MHC molecules.
- **Epitope prediction**: mapping receptors to antigens.
- **Immune cell phenotyping**: flow/mass cytometry, single-cell RNA/CITE-seq.
- **Vaccine design**: immunogen selection, epitope mapping, mRNA optimization.

## Code pattern

```python
from mhcflurry import Class1AffinityPredictor

predictor = Class1AffinityPredictor.load()

peptides = ['SIINFEKL', 'SLYNTVATL', 'GILGFVFTL']
result = predictor.predict_to_dataframe(
    peptides=peptides,
    allele='HLA-A*02:01',
)
print(result[['peptide', 'allele', 'prediction']])
```

## Tuning notes

- MHCflurry covers common HLA alleles; rare alleles may need custom training.
- Use appropriate peptide lengths (8-11 for class I, 13-25 for class II).
- For AIRR, normalize by sampling depth and PCR/UMI errors.
- Pair immune repertoire labels with clinical metadata carefully.
- Validate predictions with ELISPOT, tetramer, or MHC multimer assays.

## Verification

1. Predict class-I MHC binding for a set of peptides and compare to experimental IC50 data.
2. Load a small AIRR dataset into immuneML and run a classification workflow.
3. Cluster clonotypes and check whether clusters correlate with disease status.

## References

- https://immuneml.uio.no/
- https://doi.org/10.1038/s42256-021-00413-z
- https://github.com/openvax/mhcflurry
- https://doi.org/10.1016/j.csbj.2025.10.007
- https://immunomind.github.io/docs/
