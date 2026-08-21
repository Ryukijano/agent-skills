# AI for Rare Disease

## Description

Integrate phenotypes, genotypes, and medical literature to shorten the diagnostic odyssey and prioritize rare-disease candidates.

## When to use

You are diagnosing an undiagnosed patient, prioritizing drug targets, or building models for rare and ultra-rare diseases with limited data.

## Usage

- **Phenotype-driven diagnosis**: match HPO terms, clinical notes, and images to rare-disease knowledge bases.
- **Genotype-phenotype integration**: combine exome/variant data with phenotype matching for gene/disease ranking.
- **Small-sample learning**: apply transfer learning, federated learning, or synthetic data to limited rare-disease cohorts.
- **Literature synthesis**: use ML or LLM tools to surface disease-gene evidence from PubMed and case reports.
- **Target and therapy prioritization**: rank candidate genes, pathways, or repurposed drugs for rare diseases.
- **Explainable differential diagnosis**: produce transparent, clinician-reviewable reasoning for each candidate.

## Steps

1. Assemble patient phenotypes (HPO terms, free text, imaging) and genomic variants (VCF/Exomiser).
2. Embed and match phenotypes to disease and gene knowledge bases plus primary literature.
3. Rank candidate diagnoses or genes using ML or LLM-based reasoning.
4. Integrate genotype evidence (pathogenicity, inheritance, allele frequency) with phenotype concordance.
5. Generate an explainable differential diagnosis with literature links for expert adjudication.
6. Validate against external case series, reanalysis, or functional studies.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Rare disease diagnosis from HPO terms
hpo_df = pd.read_csv('hpo_patient_terms.csv')
vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split(';'), lowercase=False)
X = vectorizer.fit_transform(hpo_df['hpo_terms'])
y = hpo_df['diagnosis']

clf = RandomForestClassifier(class_weight='balanced')
clf.fit(X, y)

# Predict top-3 differential diagnoses for a new patient
new_terms = 'HP:0001250;HP:0001263;HP:0002119'
proba = clf.predict_proba(vectorizer.transform([new_terms]))[0]
top3 = proba.argsort()[-3:][::-1]
print([clf.classes_[i] for i in top3])
```

## Tuning notes

- Rare classes are extremely imbalanced; use class weights, resampling, or ensembling.
- Combine HPO with variant features for multi-modal diagnosis.
- Transfer learning from common diseases can bootstrap rare-disease models.
- Validate on external case reports and prospective cases.
- Maintain explainability; clinicians need transparent reasoning.

## Verification

1. Train a top-k rare-disease classifier on HPO term profiles.
2. Add VCF variant features and measure gain in top-1/Recall@5.
3. Compare predictions against a clinical genetics pipeline such as Exomiser.

## References

- https://raresource.nih.gov/
- https://doi.org/10.1038/s41586-025-10097-9
- https://github.com/MAGIC-AI4Med/DeepRare
- https://doi.org/10.1186/s13073-026-01671-5
- https://www.microsoft.com/en-us/research/publication/evidence-aggregator-ai-reasoning-applied-to-rare-disease-diagnostics/
