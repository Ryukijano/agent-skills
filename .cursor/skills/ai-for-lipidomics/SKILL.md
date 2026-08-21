# AI for Lipidomics

## Description

Use machine learning on LC-MS/MS and shotgun lipidomics data to annotate lipid classes, resolve isomers, normalize variation and link lipid profiles to phenotypes.

## When to use

You are quantifying or classifying lipid species from LC-MS/MS or shotgun lipidomics data and need to annotate lipid classes, correct for technical variation, or link lipid profiles to phenotypes.

## Usage

- **Classify lipids**: assign species to fatty acyls, glycerolipids, glycerophospholipids, sphingolipids, and sterols.
- **Resolve isomers**: use fragmentation and retention patterns to separate structural isomers and epilipidomics modifications.
- **Normalize signals**: scale by total lipid class sum or internal standards and correct batch drift.
- **Map nomenclature**: align annotations with LipidMaps and pathway databases.
- **Build phenotype models**: link lipid signatures to disease, diet, or intervention outcomes.

## Steps

1. Acquire LC-MS/MS or shotgun lipidomics data and apply peak picking and alignment.
2. Annotate lipid classes and molecular species with LipidMaps and MS/MS fragment rules.
3. Normalize intensities by class sums or internal standards and correct batch effects.
4. Perform PCA, univariate tests, or supervised classification on lipid features.
5. Validate isomer resolution and annotation confidence with reference standards.
6. Integrate lipid signatures with clinical or phenotypic data and replicate in independent cohorts.

## Code pattern

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("lipidomics.csv")
X = df[lipid_columns]
X_scaled = StandardScaler().fit_transform(X)
pcs = PCA(n_components=2).fit_transform(X_scaled)
```

## Tuning notes

- Normalize by total lipid class sum or internal standards.
- Handle structural isomers and annotation confidence levels.
- Correct for instrument batch and column drift.
- Be cautious of correlated lipid species in multivariate models.

## Verification

1. Inspect lipid class distributions for biological plausibility.
2. Replicate sample correlation and coefficient of variation across replicates.
3. Compare class separation in PCA to a priori group labels.

## References

- https://doi.org/10.1007/s00216-023-04991-2
- https://doi.org/10.3390/biom11030473
- https://doi.org/10.1016/j.bbalip.2017.05.006
- https://doi.org/10.1021/acs.analchem.2c04406
