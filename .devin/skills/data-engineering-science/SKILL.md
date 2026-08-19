# Data Engineering for Scientific ML

## Description

ETL pipelines, feature stores, vector databases, RAG, and embeddings for scientific data.

## When to use

You are building data pipelines, feature stores, or retrieval systems for scientific ML.

## Key concepts

- **ETL**: Apache Spark, DuckDB, Polars, RAPIDS cuDF, dask-cuda.
- **Feature stores**: Feast for online/offline features; vector DB support.
- **Vector DBs**: FAISS, Milvus, Qdrant, pgvector, Pinecone.
- **RAG**: chunk, embed, retrieve, generate.
- **Embeddings**: sentence-transformers, ESM, Prithvi, CLIP for science.

## Code pattern

```python
import polars as pl

df = pl.read_parquet("s3://bucket/data/*.parquet")
df = df.with_columns(pl.col("x").log().alias("log_x"))
```

RAG:

```python
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(docs)
```

## Tuning notes

- Use Parquet/Zarr/TensorStore for large scientific arrays.
- For RAG, chunk size should match the embedding model's context window.
- Feature stores decouple training and serving features to avoid skew.

## Verification

1. Ingest 1M scientific records and measure ETL throughput.
2. Build a small FAISS index and run nearest-neighbor queries.
3. Verify RAG retrieval improves LLM answer quality on a scientific Q&A task.

## References

- https://docs.feast.dev/
- https://milvus.io/
- https://docs.pola.rs/
- https://rapids.ai/
