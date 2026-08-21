# AI for Content Strategy

## Description

Use AI to audit content libraries, identify topic gaps, optimize for generative-engine citation, and adapt assets across channels.

## When to use

You are planning editorial calendars, auditing content libraries, adapting assets across channels, or optimizing for AI search citations.

## Usage

- Inventory existing content and cluster it into topic pillars.
- Identify performance gaps and competitive whitespace.
- Structure content so LLMs cite the brand in their answers.
- Repurpose long-form content into social, email, and video scripts.

## Steps

1. Export the content inventory and performance data.
2. Cluster content into topic pillars using NLP or embeddings.
3. Map buyer prompts and answer-first passages to target for GEO.
4. Audit for gaps and generate a prioritized topic backlog.
5. Reformat a flagship piece into channel-specific variants and track LLM citation share.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster existing content into topic pillars
df = pd.read_csv("content_inventory.csv")
vectors = TfidfVectorizer(stop_words="english").fit_transform(df["body"])
df["cluster"] = KMeans(n_clusters=6, random_state=42, n_init="auto").fit_predict(vectors)
print(df[["title", "cluster"]].head())
```

## Tuning notes

- Focus on answer-first, structured, citeable passages for GEO.
- Map content to buyer prompts, not just keywords.
- Maintain a single source of truth for brand voice and facts.
- Measure LLM citation share, not just search ranking.

## Verification

1. Audit a site and produce a gap analysis with 10 new topic recommendations.
2. Reformat one long-form article into social, email, and video scripts.
3. Track citation rate in a small LLM-retrieval benchmark.

## References

- https://doi.org/10.1177/14413582251390582
- https://doi.org/10.1177/00472816211041951
- https://doi.org/10.1145/3648188.3675142
- https://doi.org/10.1108/ejim-03-2024-0317
