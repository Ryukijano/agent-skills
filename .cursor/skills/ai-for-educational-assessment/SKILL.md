# AI for Educational Assessment

## Description

Score open-ended student work and generate targeted feedback at scale while monitoring fairness and validity.

## When to use

You need to score open-ended work, generate formative feedback, or design assessments at scale while preserving validity, reliability, and fairness.

## Usage

- Build or select rubrics aligned with learning outcomes.
- Fine-tune or prompt an LLM/AES model to score open-ended work.
- Compare AI scores to human raters using QWK and ICC.
- Audit subgroup score parity and construct validity.

## Steps

1. Build or select rubrics aligned with learning outcomes.
2. Fine-tune or prompt an LLM/AES model to score open-ended work.
3. Compare AI scores to human raters using QWK and ICC.
4. Audit subgroup score parity and construct validity.
5. Iterate with teachers to align generated assessments to the curriculum.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

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
