# AI for Copywriting

## Description

Draft and A/B-test personalized marketing emails that match brand voice and lift conversion rates by double digits.

## When to use

You are creating ads, emails, landing pages, product descriptions, or calls to action that must convert and match a brand voice.

## Usage

- Draft ads, emails, landing pages, and product descriptions in brand voice.
- Apply copy frameworks such as AIDA, PAS, BAB, and Hook-Promise-Proof.
- Generate variants for A/B testing and rank them by predicted CTR.
- Verify claims, avoid fabricated specifics, and run brand-safety QA.

## Steps

1. Load the brand voice guide, audience profile, and copy framework.
2. Prompt for several variants with constraints on tone and length.
3. Score variants against brand voice and predicted performance.
4. Run a human QA pass for claims, safety, and platform limits.
5. Launch an A/B test and iterate based on CTR or conversion lift.

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

- https://arxiv.org/abs/2402.13667
- https://www.chicagobooth.edu/review/ai-is-coming-marketing-department
- https://doi.org/10.1016/j.jbusres.2024.114984
- https://www.deloittedigital.com/us/en/insights/research/genai-human-marketing-operations.html
