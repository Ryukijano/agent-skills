# AI for Rare Disease

## Description

AI for rare disease diagnosis, target prioritization, drug repurposing, natural history modeling, and diagnostic-odyssey support.

## When to use

You are diagnosing an undiagnosed patient, prioritizing drug targets, or building models for rare and ultra-rare diseases with limited data.

## Key concepts

- **Diagnostic odyssey**: long, multi-specialty path to a rare disease diagnosis.
- **Phenotype ontologies**: Human Phenotype Ontology (HPO) terms.
- **Small-sample ML**: transfer learning, federated learning, synthetic data.
- **Genotype-phenotype integration**: exome/variant + HPO matching.
- **Target prioritization**: genetic, functional, and literature evidence.
- **Drug repurposing for rare diseases**: identifying existing drugs for new rare indications.

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
