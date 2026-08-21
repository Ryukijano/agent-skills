# AI for Data Discovery

## Description

Help users find, understand, and trust the right data and AI assets.

## When to use

Users cannot find the right data in a lake, catalog, or open repository, and keyword search is insufficient.

## Usage

- Search catalogs with natural language (Alation, Atlan, DataHub).
- Auto-generate descriptions, tags, and glossary links.
- Recommend similar or related datasets.
- Show data quality, popularity, and owner context.
- Embed search into BI and notebooks for self-service.

## Steps

1. Crawl data sources and extract metadata.
2. Build knowledge graph of datasets, terms, and users.
3. Train ranking and recommendation models.
4. Expose natural-language search and recommendations.
5. Track adoption and improve relevance.

## Code pattern

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

model = SentenceTransformer("all-MiniLM-L6-v2")
query_emb = model.encode("monthly sales by region")
dataset_embs = model.encode(dataset_descriptions)
scores = cosine_similarity([query_emb], dataset_embs)[0]
```

## Tuning notes

- Combine lexical and semantic search for recall and precision.
- Keep provenance and access controls with every discovered asset.
- Update indexes as new datasets and schemas are added.

## Verification

1. Search for a dataset and verify the top result matches intent.
2. Discover joinable columns across two datasets.
3. Compare a semantic search to a keyword baseline on real queries.

## References

- https://doi.org/10.1145/3626521
- https://doi.org/10.1007/s00778-019-00564-x
- https://doi.org/10.48550/arxiv.2509.00728
- https://doi.org/10.1002/pra2.1242
