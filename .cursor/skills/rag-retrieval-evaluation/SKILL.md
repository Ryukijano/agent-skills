# RAG Retrieval Evaluation

## Description

Evaluate retrieval quality, answer relevance, and end-to-end RAG pipeline performance.

## When to use

You are building or improving a retrieval-augmented generation pipeline and need to measure its components.

## Key concepts

- **Retrieval metrics**: MRR, Recall@k, NDCG, hit rate.
- **Generation metrics**: faithfulness, answer relevance, context precision.
- **RAGAS**: framework with context relevance, answer correctness, etc.
- **LLM-as-judge**: evaluate generated answers against retrieved context.

## Code pattern

```python
from ragas import evaluate
from ragas.metrics import context_recall, faithfulness, answer_relevancy

result = evaluate(
    dataset=eval_dataset,
    metrics=[context_recall, faithfulness, answer_relevancy],
)
print(result)
```

## Tuning notes

- Evaluate retrieval and generation separately before end-to-end.
- Bad retrieval is a common root cause of RAG failures.
- Use domain-specific test questions for realistic benchmarks.

## Verification

1. Build a small Q&A benchmark with gold documents and answers.
2. Compute retrieval Recall@5 and generation faithfulness.
3. A/B test two retrievers and measure end-to-end answer accuracy.

## References

- https://arxiv.org/abs/2404.01037
- https://docs.ragas.io/
- https://huggingface.co/papers/2403.18131
- https://python.langchain.com/docs/guides/evaluation/
