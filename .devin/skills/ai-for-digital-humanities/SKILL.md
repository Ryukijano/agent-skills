# AI for Digital Humanities

## Description

Machine learning, NLP, and network analysis for historical texts, archives, languages, and multimodal humanities collections.

## When to use

You are working with digitized historical texts, multilingual archives, ancient languages, or multimodal humanities corpora that require scalable computational analysis.

## Key concepts

- **Text mining and NLP for DH**: OCR, spelling normalization, named entity recognition, and semantic search.
- **Historical and ancient languages**: transfer learning, low-resource adaptation, and digitization pipelines for classical and endangered texts.
- **Corpus curation and thematic modeling**: word embeddings, topic models, and expert-in-the-loop curation platforms.
- **Intertextuality and semantic search**: paraphrase detection, passage alignment, and reception studies.

## Code pattern

```python
from transformers import pipeline

# Named-entity recognition on a historical text
ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
entities = ner("Dr. Livingstone explored the Zambezi river in 1855.")
```

## Tuning notes

- Historical language is non-standard; use domain-adapted models or fine-tune on period corpora.
- OCR errors propagate downstream; add post-correction and confidence filtering.
- Interpretability and transparency matter; document model choices and limitations for humanities scholars.

## Verification

1. Run OCR on a historical page and measure character/word error rate.
2. Build a semantic search index for a historical corpus and evaluate retrieval relevance.
3. Fine-tune a language model on a low-resource ancient language and compare to a general baseline.

## References

- https://arxiv.org/pdf/2307.16217
- https://doi.org/10.1007/978-3-030-36599-8_31
- https://aclanthology.org/2025.nlp4dh-1.35/
- https://aclanthology.org/2026.nlp4dh-1.20/
- https://aclanthology.org/anthology-files/pdf/cl/2023.cl-3.5.pdf
