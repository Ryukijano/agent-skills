# AI for Longevity

## Description

Estimate biological age and discover longevity interventions by applying epigenetic clocks and multi-omic aging models to molecular data.

## When to use

You are estimating biological age, mining longevity interventions, or integrating multi-omic data to understand aging trajectories.

## Usage

- **Biological-age estimation**: apply DNA methylation, transcriptomic, or proteomic clocks to estimate biological age.
- **Aging-biomarker discovery**: identify clocks and EpiScores that correlate with mortality, frailty, or disease risk.
- **Intervention mining**: screen public molecular compendia for drugs, diets, or genetic manipulations that modify biological age.
- **Multi-omic integration**: combine DNA methylation, RNA, metabolites, and clinical lab data.
- **Longitudinal tracking**: use repeated measures to assess within-individual aging trajectories.
- **Outcome validation**: test clock predictions against survival, health outcomes, or experimental models.

## Steps

1. Select the tissue/cell type and aging clock(s) appropriate for the biological question (e.g., Horvath, GrimAge, PhenoAge, DunedinPACE).
2. Preprocess and impute missing CpGs or features against a reference panel.
3. Compute biological age and residualized age-acceleration scores for each sample.
4. Correlate predicted age with interventions, exposures, or health outcomes in longitudinal or cross-sectional data.
5. Use systematic reanalysis or knowledge-graph tools to mine candidate geroprotective interventions.
6. Validate top candidates in independent cohorts or experimental models and update the clock as needed.

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
