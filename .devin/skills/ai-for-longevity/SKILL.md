# AI for Longevity

## Description

Biological aging clocks, biomarkers of aging, longevity intervention mining, and integrative multi-omic models of aging.

## When to use

You are estimating biological age, mining longevity interventions, or integrating multi-omic data to understand aging trajectories.

## Key concepts

- **Aging clocks**: predictors trained on DNA methylation, transcriptomics, proteomics, etc.
- **Biomarkers of aging**: clocks that correlate with mortality and morbidity.
- **Longevity interventions**: drugs, diet, and genetic manipulations that extend lifespan.
- **Multi-omic integration**: DNA methylation + RNA + metabolites + clinical labs.
- **Survival analysis**: Cox models, accelerated failure time.
- **Comparative biology**: cross-species aging mechanisms.

## Code pattern

```python
import anndata
import pyaging

# Load an anndata object with methylation CpGs as .var_names
adata = anndata.read_h5ad('methylation_betas.h5ad')

# Apply one or more aging clocks
adata = pyaging.predict._pred.predict_age(
    adata,
    clock_names=['horvath2013', 'hannum'],
    device='auto',
)
print(adata.obs[['horvath2013', 'hannum']].head())
```

## Tuning notes

- Choose a clock trained on the same tissue as your data.
- Missing CpG sites can be imputed from a reference; results are sensitive to imputation.
- Adjust for chronological age and confounders when evaluating intervention effects.
- Use longitudinal data to assess within-individual aging rate.
- Validate clocks against health outcomes, not just chronological age.

## Verification

1. Predict biological age with at least two clocks and compare correlation with chronological age.
2. Test whether a longevity intervention shifts predicted age in a cohort.
3. Reproduce one published aging clock from its original CpG list and beta coefficients.

## References

- https://github.com/lucascamillomd/pyaging
- https://doi.org/10.1093/bioinformatics/btae200
- https://www.genomics.senescence.info/
- https://www.clockbase.org/
- https://gladyshevlab.org/mSALT/
