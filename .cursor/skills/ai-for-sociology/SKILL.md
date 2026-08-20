# AI for Sociology

## Description

Computational social science for sociology: text and image classification, survey augmentation, social network analysis, and modeling social inequalities.

## When to use

You are studying social behavior, institutions, or inequalities and want to use large-scale digital data, text, images, and networks to test sociological theories.

## Key concepts

- **Text-as-data**: classify, scale, and topic-model documents to measure social constructs.
- **Social network analysis**: identify communities, influencers, and diffusion patterns.
- **Survey augmentation and imputation**: use ML to handle item nonresponse and improve estimation.
- **Heterogeneity and segmentation**: discover subpopulations with causal forests or clustering.
- **Computational approaches to inequality**: audit algorithms, analyze mobility, and detect disparities.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Example: classify open-ended survey responses by theme
X_train, X_test, y_train, y_test = train_test_split(df["response"], df["theme"], stratify=df["theme"])
vec = TfidfVectorizer(max_features=5000, ngram_range=(1, 2))
clf = LogisticRegression(max_iter=1000)
clf.fit(vec.fit_transform(X_train), y_train)
print(clf.score(vec.transform(X_test), y_test))
```

## Tuning notes

- Validate text-based measures against representative surveys when possible.
- Address sampling bias from digital platforms and administrative records.
- Ensure constructs like class, race, and gender are measured with care and theory.
- Use causal inference rather than purely predictive models to support sociological claims.

## Verification

1. Replicate a published text-as-data finding on a new sample.
2. Compare a network-derived community partition to a demographic baseline.
3. Validate a survey-imputation model against a gold-standard subsample.

## References

- https://www.annualreviews.org/content/journals/10.1146/annurev-soc-073117-041106
- https://doi.org/10.1146/annurev-soc-121919-054621
- https://journals.sagepub.com/doi/full/10.1177/23780231241259651
- https://link.springer.com/article/10.1007/s13278-025-01428-9
