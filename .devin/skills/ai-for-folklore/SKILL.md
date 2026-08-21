# AI for Folklore

## Description

Classify folk-tale motifs and tale types across multilingual corpora to compare narrative traditions and cultural diffusion.

## When to use

You are studying folk tales, legends, proverbs, or other vernacular traditions and want to detect motifs, tale types, or narrative structures at scale.

## Usage

- Collect and transcribe oral narratives and texts.
- Classify tale types and motifs (ATU/Thompson).
- Map geographic and temporal diffusion.
- Generate variants and synthetic examples.

## Steps

1. Collect and transcribe oral narratives and texts.
2. Classify tale types and motifs (ATU/Thompson).
3. Map geographic and temporal diffusion.
4. Generate variants and synthetic examples.
5. Validate against archival sources and storytellers.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster a corpus of folktale variants by motif content
vectorizer = TfidfVectorizer(max_features=1000, ngram_range=(1, 2))
X = vectorizer.fit_transform(tale_texts)
clusters = KMeans(n_clusters=8, random_state=42, n_init="auto").fit_predict(X)
```

## Tuning notes

- Folklore variants are culturally specific; avoid flattening regional and historical nuance.
- Validate motif extraction against expert-annotated samples.
- Use multilingual models and cross-lingual alignment for comparative studies.

## Verification

1. Extract motifs from a set of Cinderella variants and compare to the ATU index.
2. Cluster tales by narrative similarity and interpret the resulting groups.
3. Evaluate an LLM's ability to classify tale types in a held-out test set.

## References

- https://doi.org/10.1093/9780197852712.003.0159
- https://doi.org/10.1080/0015587x.2023.2233839
- https://cacm.acm.org/research/computational-folkloristics/
- https://arxiv.org/pdf/2510.18561
- https://www.mdpi.com/2076-0787/14/12/230
