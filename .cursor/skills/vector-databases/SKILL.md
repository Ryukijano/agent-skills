# Vector Databases for Machine Learning

## Description

Approximate nearest neighbor search, dense-embedding storage, metadata filtering, hybrid search, and vector indexing for RAG and recommendation.

## When to use

You need to store, search, and retrieve high-dimensional embeddings at scale, often with metadata constraints and low latency.

## Key concepts

- **Vector embeddings**: dense representations from encoders, LLMs, or multimodal models.
- **Approximate nearest neighbor (ANN)**: HNSW, IVF, PQ, LSH for fast search.
- **Metadata filtering**: combine vector similarity with attribute constraints.
- **Hybrid search**: combine dense vector and sparse/keyword retrieval.
- **Operational features**: replication, sharding, persistence, and multi-tenancy.

## Code pattern

```python
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="docs",
    vectors_config=VectorParams(size=128, distance=Distance.COSINE),
)

client.upsert(
    collection_name="docs",
    points=[
        PointStruct(id=1, vector=[0.1] * 128, payload={"doc_id": "A1"}),
        PointStruct(id=2, vector=[0.9] * 128, payload={"doc_id": "B2"}),
    ],
)

results = client.search(
    collection_name="docs",
    query_vector=[0.1] * 128,
    limit=5,
    query_filter={"must": [{"key": "doc_id", "match": {"value": "A1"}}]}
)
```

## Tuning notes

- Choose the distance metric and indexing algorithm that match your embedding model.
- Tune HNSW `ef_construct`, `ef_search`, and `M` for recall vs. latency trade-offs.
- Pre-filtering reduces recall if the vector index is not built on the filtered subset.
- Monitor index build time and memory as dimensionality and cardinality grow.

## Verification

1. Index 10k vectors and measure Recall@10 against exact brute-force search.
2. Run hybrid queries combining vector and metadata filters; verify result relevance.
3. Benchmark latency and throughput under a representative query load.

## References

- https://arxiv.org/abs/2608.12812
- https://arxiv.org/abs/2310.11703
- https://arxiv.org/abs/2602.11443
- https://www.pinecone.io/research/ICML_2025.pdf
- https://arxiv.org/abs/2502.16931
