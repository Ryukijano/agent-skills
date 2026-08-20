# AI for Copywriting

## Description

Marketing and advertising copy, email and landing-page text, conversion frameworks, and brand-voice calibration with LLMs.

## When to use

You are creating ads, emails, landing pages, product descriptions, or calls to action that must convert and match a brand voice.

## Key concepts

- **Copy frameworks**: AIDA, PAS, BAB, FAB, 4U, and Hook-Promise-Proof.
- **Brand voice calibration**: few-shot examples, tone descriptors, and style guides.
- **A/B testing and uplift**: generate variants, rank them, and test in the field.
- **CRO integration**: align copy with audience, channel, and funnel stage.
- **Hallucination and claim control**: verify claims and avoid fabricated specifics.

## Code pattern

```python
from openai import OpenAI

client = OpenAI()

prompt = (
    "Using the Problem-Agitate-Solution framework, write 3 email subject lines "
    "and opening lines for a sustainable running-shoe launch. "
    "Tone: bold but warm."
)

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.8,
)
print(response.choices[0].message.content)
```

## Tuning notes

- Provide 3-5 brand voice examples for consistent tone.
- Generate many variants, then rank with historic CTR data or a reward model.
- Keep within platform character limits.
- Always run a human QA pass for claims and brand safety.

## Verification

1. Generate 5 email subject lines and test open rate against a baseline.
2. Apply a brand-voice scorecard to 20 copy samples.
3. Run a small A/B test on a landing-page headline.

## References

- https://arxiv.org/html/2402.13667
- https://www.chicagobooth.edu/review/ai-is-coming-marketing-department
- https://doi.org/10.1016/j.jbusres.2024.114984
- https://www.deloittedigital.com/us/en/insights/research/genai-human-marketing-operations.html
