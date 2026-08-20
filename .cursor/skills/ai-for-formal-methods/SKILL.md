# AI for Formal Methods

## Description

Neuro-symbolic verification, LLM-assisted autoformalization, and learned heuristics for theorem provers and model checkers.

## When to use

You want to translate informal specifications into formal models, guide proof search, or apply ML to model checking, program verification, and certified systems.

## Key concepts

- **Autoformalization**: converting natural language or code into formal specifications using LLMs.
- **Neuro-symbolic verification**: combining neural guidance with SAT/SMT/TLA+ and model checkers.
- **Proof search guidance**: premise selection, tactic prediction, and lemma synthesis.
- **Invariants and certificates**: using ML to discover loop invariants or safety certificates.

## Code pattern

```python
# Autoformalization sketch using an LLM and a proof checker
from transformers import pipeline

formalizer = pipeline("text2text-generation", model="t5-formalizer")

spec = "The array is sorted in non-decreasing order."
formal = formalizer(f"formalize: {spec}")[0]["generated_text"]
print(formal)

# Proof guidance with a learned premise ranker
premises = ["le_refl", "le_trans", "sorted_def"]
scores = predictor.predict(premises)  # trained on proof corpora
best = premises[int(np.argmax(scores))]
```

## Tuning notes

- Always verify LLM output with a trusted proof assistant or solver.
- Use smaller, domain-tuned models for autoformalization to reduce hallucination.
- Distinguish between sound automation and heuristic guidance.

## Verification

1. Formalize a small English specification and check it in a proof assistant.
2. Train a premise selector on a proof corpus and measure recall of used lemmas.
3. Compare a model-guided proof search to an unguided baseline on a benchmark.

## References

- https://doi.org/10.1007/s10664-025-10729-8
- https://doi.org/10.48550/arxiv.2404.09939
- https://aclanthology.org/2026.bigpicture-main.1/
- https://arxiv.org/abs/2606.08728v4
- https://doi.org/10.48550/arxiv.2403.04017
