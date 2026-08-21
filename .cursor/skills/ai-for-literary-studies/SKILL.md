# AI for Literary Studies

## Description

Attribute authorship and detect stylistic patterns across literary corpora to study genre, influence, and intertextuality.

## When to use

You are analyzing style, genre, authorship, intertextuality, or thematic structures in literary texts and corpora.

## Usage

- OCR/segment texts, paratext, and marginalia.
- Identify style, authorship, intertextuality, and themes.
- Create annotated editions and linked data.
- Model narrative structures and character networks.

## Steps

1. OCR/segment texts, paratext, and marginalia.
2. Identify style, authorship, intertextuality, and themes.
3. Create annotated editions and linked data.
4. Model narrative structures and character networks.
5. Validate with literary scholars and primary sources.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

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
