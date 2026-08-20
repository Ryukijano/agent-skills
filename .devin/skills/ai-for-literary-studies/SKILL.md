# AI for Literary Studies

## Description

Computational stylistics, authorship attribution, genre and style analysis, and interpretive NLP for literary texts and corpora.

## When to use

You are analyzing style, genre, authorship, intertextuality, or thematic structures in literary texts and corpora.

## Key concepts

- **Stylometry and computational stylistics**: frequency-based, vector-space, and neural methods for style and authorship.
- **Genre and period classification**: supervised and unsupervised models for literary categorization.
- **Authorship attribution and verification**: Burrows' Delta, embedding-based classifiers, and attribution benchmarks.
- **Interpretive NLP and LLMs**: probing language models for literary style, metaphor, and intertextual allusion.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# Simple authorship attribution from most-frequent-word features
vectorizer = TfidfVectorizer(max_features=500, ngram_range=(1, 2))
X = vectorizer.fit_transform(corpus)
model = MultinomialNB().fit(X, authors)
```

## Tuning notes

- Use closed-vocabulary features for stylometry to reduce content leakage into style signals.
- Compare model predictions with close-reading interpretations and literary theory.
- Watch for anachronism in training corpora and chronological leakage in attribution tasks.

## Verification

1. Attribute authorship on a benchmark corpus and compare to Burrows' Delta.
2. Classify genre or period and inspect the most predictive features.
3. Probe an LLM for stylistic features and compare to human-annotated style dimensions.

## References

- https://txtlab.org/wp-content/uploads/2021/10/Herrmann_Piper_Jacobs_CompStylistics_2021.pdf
- https://www.cambridge.org/core/journals/computational-humanities-research/article/looking-for-the-inner-music/558CF901089D78168E83915B0AD9C34C
- https://doi.org/10.1057/s41599-025-05986-3
- https://aclanthology.org/2025.emnlp-main.1227.pdf
- https://www.routledge.com/Computational-Literary-Studies-Theory-and-Methods/Rebora/p/book/9781041059769
