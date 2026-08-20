# Long-Context LLM Methods

## Description

Architectures, position interpolation, and evaluation for language models with very long contexts.

## When to use

You need to process documents, videos, or conversations that exceed the model's native context window.

## Key concepts

- **Position interpolation**: scale RoPE bases or adjust frequencies to extend context.
- **Ring attention / sparse attention**: sub-quadratic attention for long sequences.
- **Needle-in-haystack**: benchmark for retrieving a fact buried in a long prompt.
- **RAG vs long context**: trade-off between retrieval augmentation and full-context feeding.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Use position-interpolated config if available
context = tokenizer(long_document, return_tensors="pt", truncation=False)
```

## Tuning notes

- RoPE rescaling to 2-8x often requires continued pre-training on long sequences.
- Sparse attention can speed inference but may alter the loss landscape.
- Evaluate with needle-in-haystack before deploying a long-context model.

## Verification

1. Run a needle-in-haystack benchmark at several context lengths.
2. Compare performance with and without position interpolation.
3. Measure perplexity on a long-document validation set.

## References

- https://arxiv.org/abs/2306.15595
- https://arxiv.org/abs/2402.17463
- https://github.com/lhao499/RingAttention
- https://arxiv.org/abs/2307.03172
