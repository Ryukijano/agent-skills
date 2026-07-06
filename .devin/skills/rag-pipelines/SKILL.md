---
name: rag-pipelines
description: >-
  Build RAG (Retrieval-Augmented Generation) pipelines with vector databases,
  embeddings, and LLMs. Use when building Q&A systems, knowledge bases, or
  document chat.
---

# RAG Pipelines

## Architecture
1. **Index**: Chunk documents → embed chunks → store in vector DB
2. **Retrieve**: Embed query → search vector DB → top-k chunks
3. **Generate**: LLM generates answer using retrieved chunks as context

## Vector Databases
- **Chroma**: Open-source, local, easy setup
- **FAISS**: Facebook's library, billion-scale, GPU support
- **Qdrant**: Rust-powered, hybrid search, filtering
- **Pinecone**: Managed, auto-scaling, <100ms latency

## Embedding Models
- `sentence-transformers/all-MiniLM-L6-v2` (fast, 384-dim)
- `BAAI/bge-large-en-v1.5` (high quality, 1024-dim)
- `text-embedding-3-large` (OpenAI API, 3072-dim)

## Code Example
```python
from sentence_transformers import SentenceTransformer
import chromadb

embedder = SentenceTransformer('all-MiniLM-L6-v2')
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.create_collection("docs")

# Index
collection.add(
    embeddings=embedder.encode(chunks).tolist(),
    documents=chunks, ids=[str(i) for i in range(len(chunks))]
)

# Retrieve
results = collection.query(
    query_embeddings=embedder.encode([query]).tolist(),
    n_results=5
)
```

## Best Practices
- Chunk size: 500-1000 tokens, 100-200 overlap
- Use hybrid search: vector + keyword (BM25)
- Rerank with cross-encoder for better precision
- Include metadata for filtering (source, date, type)
- Evaluate with RAGAS or TruLens
