# AI for Disability Inclusion

## Description

Accessible AI, disability-aware bias evaluation, inclusive design, and assistive technologies that respect the rights and agency of people with disabilities.

## When to use

You are building AI systems used by, or about, people with disabilities and want to avoid ableism and improve accessibility.

## Key concepts

- **Disability-aware evaluation**: benchmark models for stereotypes, factual errors, and sentiment drift on disability-related queries.
- **Assistive AI**: speech-to-text, image captioning, sign-language recognition, and real-time captioning.
- **Inclusive co-design**: involve people with disabilities in data collection, model design, and deployment.
- **Algorithmic harm taxonomy**: representational, allocative, quality-of-service, and interpersonal harms.

## Code pattern

```python
from transformers import pipeline

# Generate image captions for screen-reader users
captioner = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
caption = captioner("https://example.org/accessible-sign.jpg")
```

## Tuning notes

- Use representative, consent-based data that captures diverse disability experiences.
- Audit for bias against specific disability types (mobility, sensory, cognitive, psychosocial).
- Provide human override and explainability, especially for high-stakes decisions.
- Follow CRPD principles: autonomy, inclusion, participation, and non-discrimination.

## Verification

1. Evaluate an LLM on a disability-bias benchmark and compare neutral vs. disability-aware prompts.
2. Build a sign-language or speech-recognition demo and measure word/sign error rates with disabled users.
3. Conduct a co-design session and document how feedback changed model or UI decisions.

## References

- https://ojs.aaai.org/index.php/AIES/article/download/36745/38883/40820
- https://aclanthology.org/2025.emnlp-main.1653/
- https://link.springer.com/article/10.1007/s00146-025-02642-x
- https://cdt.org/wp-content/uploads/2025/03/2025-03-11-CDT-Building-A-Disability-Inclusive-AI-Ecosystem-report-final.pdf
