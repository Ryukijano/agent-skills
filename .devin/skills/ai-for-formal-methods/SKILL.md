# AI for Formal Methods

## Description

Use machine learning and LLMs to translate informal specifications into formal models and guide theorem provers and model checkers.

## When to use

You want to translate informal specifications into formal models, guide proof search, or apply ML to model checking, program verification, and certified systems.

## Usage

- Autoformalize natural-language or code specifications into formal logic using LLMs and domain-tuned models.
- Combine neural guidance with SAT/SMT/TLA+ solvers and model checkers for neuro-symbolic verification.
- Predict the next proof step, relevant premises, and useful tactics from the current proof state.
- Discover loop invariants and safety certificates from data and program structure.

## Steps

1. Collect a corpus of informal specifications, code, and corresponding formal models for the target domain.
2. Train or prompt an LLM to autoformalize specifications and validate outputs with a trusted checker.
3. Build a premise selector or tactic predictor from a proof corpus and integrate it with the proof assistant.
4. Run model-checking or verification tasks with learned guidance and compare proof search effort.
5. Use the system to synthesize invariants or certificates for safety-critical programs.
6. Iterate with human experts to correct formalizations and maintain soundness guarantees.

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
