# AI for Data Discovery

## Description

Intelligent dataset search, metadata enrichment, schema inference, and conversational data catalog exploration to find the right data quickly.

## When to use

Users cannot find the right data in a lake, catalog, or open repository, and keyword search is insufficient.

## Usage

- **Dataset search and recommendation**: match needs by metadata, content, or examples.
- **Schema and semantic inference**: auto-extract columns, types, and relationships.
- **Data profiling and summarization**: surface distributions, coverage, and quality.
- **Conversational exploration**: use LLMs to answer natural-language data requests.
- **Similarity and join discovery**: identify related datasets and linkable keys.

## Steps

1. Collect and index datasets with metadata, schema, and samples.
2. Build embeddings and similarity indexes over metadata and content.
3. Deploy search and recommendation APIs or chat interfaces.
4. Let users explore lineage, quality, and usage statistics.
5. Refine ranking from user feedback and query logs.

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
