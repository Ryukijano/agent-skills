# AI for Law

## Description

Legal document analysis, case law retrieval, contract review, and legal reasoning benchmarks.

## When to use

You are processing contracts, statutes, case law, or legal queries with NLP.

## Key concepts

- **Legal NLP**: NER, classification, summarization, question answering.
- **Case law retrieval**: dense and sparse retrieval over court opinions.
- **Contract review**: clause extraction, risk flagging, comparison.
- **Benchmarks**: LegalBench, COLIEE, Law School Admission Test tasks.
- **Hallucination**: citations and claims must be verifiable.

## Code pattern

```python
from transformers import pipeline

qa = pipeline("question-answering", model="pile-of-law/legalbert-large-1.7M-2")
result = qa(question="What is the governing law?", context=contract_text)
```

## Tuning notes

- Legal language is domain-specific; use legal-domain pretrained models.
- Ground outputs in cited sources; never fabricate citations.
- Bias and jurisdictional differences can affect model behavior.

## Verification

1. Fine-tune a legal document classifier on a public dataset.
2. Build a clause-extraction pipeline and compare to manual annotations.
3. Test a legal QA system on a fact-based question with a known case.

## References

- https://arxiv.org/abs/2403.03873
- https://huggingface.co/papers/2404.05279
- https://case.law/
- https://huggingface.co/pile-of-law/legalbert-large-1.7M-2
