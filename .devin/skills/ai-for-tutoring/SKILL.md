# AI for Tutoring

## Description

Use AI to build or augment a one-on-one digital tutor that diagnoses misconceptions and gives step-by-step guidance without giving away the answer.

## When to use

You want to build or augment a one-on-one digital tutor that diagnoses misconceptions and gives step-by-step guidance without giving away the answer.

## Usage

- Load student model, expert model, and curriculum knowledge sources.
- Diagnose misconceptions from student responses.
- Generate Socratic hints that avoid answer leakage.
- Adapt difficulty and pedagogy in real time.

## Steps

1. Load student model, expert model, and curriculum knowledge sources.
2. Diagnose misconceptions from student responses.
3. Generate Socratic hints that avoid answer leakage.
4. Adapt difficulty and pedagogy in real time.
5. Validate learning gains against a worksheet or human-tutor baseline.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

## Code pattern

```python
import openai

# Socratic tutor prompt that avoids giving the answer
system_prompt = (
    "You are a patient math tutor. Ask one clarifying question at a time, "
    "guide the student to discover their own mistake, and never reveal the final answer."
)
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"I got {student_answer} for {problem}. What should I do?"},
    ],
)
```

## Tuning notes

- Evaluate tutor responses on pedagogical dimensions, not just fluency.
- Use the target curriculum and problem set to constrain model outputs.
- Keep a human escalation path for high-stakes or persistent errors.

## Verification

1. Build a small math tutoring dialog and rate hint quality against a rubric.
2. Compare learning gains between an AI tutor and a worksheet-only control.
3. Test error diagnosis accuracy on a labeled set of student misconceptions.

## References

- https://doi.org/10.1007/s40593-025-00505-6
- https://aclanthology.org/2025.naacl-long.57/
- https://arxiv.org/abs/2402.09216
- https://doi.org/10.1145/3701716.3715244
