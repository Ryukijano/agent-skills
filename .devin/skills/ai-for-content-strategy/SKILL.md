# AI for Content Strategy

## Description

Planning, auditing, and orchestrating content portfolios with AI, including generative-engine optimization and cross-platform adaptation.

## When to use

You are planning editorial calendars, auditing content libraries, adapting assets across channels, or optimizing for AI search citations.

## Key concepts

- **Content audit and gap analysis**: inventory, performance data, topic clusters, and competitive whitespace.
- **Generative engine optimization (GEO)**: structuring content so LLMs cite your brand in their answers.
- **Cross-platform adaptation**: tone, length, and format for web, social, email, and video.
- **Personalization and audience personas**: AI-driven segmentation and messaging.
- **Governance and quality**: brand voice, fact-checking, and editorial guidelines.

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
