# AI for Educational Assessment

## Description

Automated essay scoring, conversational assessment, LLM rubric grading, feedback generation, and validity and fairness of AI-driven evaluation.

## When to use

You need to score open-ended work, generate formative feedback, or design assessments at scale while preserving validity, reliability, and fairness.

## Key concepts

- **Automated Essay Scoring (AES)**: models that predict holistic or trait-level writing scores.
- **Conversational assessment**: LLM-driven dialogs that probe understanding aligned with learning outcomes.
- **Rubric generation and calibration**: derive scoring criteria and align AI scores with human raters.
- **Fairness and validity**: check for subgroup score differences and construct validity across populations.

## Code pattern

```python
from transformers import pipeline

# Zero-shot LLM scoring with a rubric
rubric = "Score the essay on argumentation, evidence, and clarity from 1 to 5."
prompt = f"{rubric}\n\nEssay: {essay}\n\nScore:"

# Use a local or API-based text-generation model
scorer = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")
result = scorer(prompt, max_new_tokens=10)
```

## Tuning notes

- Evaluate against human raters using quadratic weighted kappa (QWK) or intraclass correlation (ICC).
- Validate on demographically diverse samples to detect score bias.
- Combine LLM scores with structured rubrics rather than relying on raw outputs.

## Verification

1. Score a benchmark essay set and compare AI-human agreement.
2. Generate rubrics for an assignment and validate them with instructors.
3. Audit subgroup score parity and correlation with final course grades.

## References

- https://doi.org/10.1145/3702163.3702169
- https://arxiv.org/abs/2403.06149
- https://arxiv.org/abs/2405.18632
- https://arxiv.org/abs/2404.04941
