# AI for Immunology

## Description

Predict MHC-bound epitopes and vaccine candidates from receptor and omic data to prioritize immunotherapy and prophylaxis designs.

## When to use

You are analyzing B-cell or T-cell receptor repertoires, predicting epitope binding, or prioritizing vaccine/immunotherapy candidates.

## Usage

- **MHC/peptide prediction**: predict peptide presentation for class I and II alleles using MHCflurry/NetMHCpan.
- **AIRR analysis**: parse BCR/TCR clonotypes and link repertoire features to disease or response.
- **Receptor-antigen specificity**: model TCR/BCR recognition of epitopes and peptide-MHC complexes.
- **Vaccine and immunotherapy design**: select immunogens, map epitopes, and optimize mRNA or receptor constructs.
- **Immune-cell phenotyping**: classify cell types and states from flow, mass cytometry, or single-cell data.
- **Safety checking**: assess cross-reactivity, autoimmunity risk, and off-target binding of designed receptors.

## Steps

1. Gather peptide, MHC allele, receptor, or repertoire data and link them to the clinical question (vaccine, therapy, biomarker).
2. Predict peptide presentation and binding for candidate epitopes with allele-specific models.
3. Model TCR/BCR specificity using sequence, structure, or generative models (e.g., TCR-TRANSLATE, AlphaFold 3, HERMES).
4. Integrate immune repertoire and clinical labels to identify disease-associated clonotypes or cell states.
5. Prioritize vaccine epitopes or therapeutic receptors and check cross-reactivity and safety.
6. Validate with MHC multimer, ELISPOT, tetramer, or binding assays and refine the design.

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
