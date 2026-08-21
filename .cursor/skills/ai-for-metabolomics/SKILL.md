# AI for Metabolomics

## Description

Use machine learning on LC-MS, GC-MS and NMR metabolite profiles to annotate features, discover biomarkers and predict disease risk or metabolic phenotypes.

## When to use

You are analyzing mass spectrometry or NMR metabolomics data to identify metabolites, find biomarkers, classify samples, or integrate metabolism with other omics layers.

## Usage

- **Process spectra**: convert LC-MS, GC-MS, and NMR data into aligned peak tables and features.
- **Annotate metabolites**: match m/z, retention time, and fragmentation to reference libraries.
- **Normalize data**: correct batch effects, drift, and sample size before modeling.
- **Map pathways**: connect significant features to KEGG, HMDB, and Reactome pathways.
- **Predict phenotypes**: train classifiers and risk scores for disease and patient stratification.

## Steps

1. Import raw spectral or peak-table data and apply quality control and missing-value imputation.
2. Annotate metabolites with m/z, RT, MS/MS libraries, or NMR chemical-shift databases.
3. Normalize and correct for batch effects using QC samples or statistical alignment.
4. Perform univariate, multivariate, or ML-based biomarker discovery with cross-validation.
5. Map significant features to metabolic pathways and interpret biological relevance.
6. Validate biomarkers with targeted assays and independent cohorts.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score

df = pd.read_csv("metabolites.tsv", sep="\t")
X = df[metabolite_columns]
y = df["condition"]
model = RandomForestClassifier(n_estimators=500, random_state=42)
scores = cross_val_score(model, X, y, cv=5)
```

## Tuning notes

- Impute missing values carefully (k-NN, half-minimum, or probabilistic).
- Correct for batch effects with QC samples and ComBat or median batch alignment.
- Use internal validation (nested CV) to avoid overfitting high-dimensional data.
- Validate putative biomarkers with targeted assays.

## Verification

1. Reproduce principal-component separation by batch and condition.
2. Check whether significant features remain stable across independent cohorts.
3. Run pathway enrichment and confirm expected biology for the phenotype.

## References

- https://doi.org/10.1016/j.trac.2024.117852
- https://doi.org/10.3390/metabo10060243
- https://doi.org/10.1002/smtd.202400305
- https://doi.org/10.3390/ijms231911269
