# AI for Disability Inclusion

## Description

Use accessible, disability-aware AI to improve assistive technologies and reduce algorithmic harm for people with disabilities.

## When to use

You are building AI systems used by, or about, people with disabilities and want to avoid ableism and improve accessibility.

## Usage

- Benchmark models for stereotypes, factual errors, and sentiment on disability-related queries.
- Build assistive AI such as speech-to-text, image captioning, and sign-language recognition.
- Involve people with disabilities in co-design, data collection, and deployment.
- Detect representational, allocative, quality-of-service, and interpersonal harms.

## Steps

1. Identify the disability community and use case and establish CRPD-aligned governance.
2. Collect representative, consent-based data that captures diverse disability experiences.
3. Train or adapt speech, vision, or language models for the assistive task.
4. Audit for bias against mobility, sensory, cognitive, and psychosocial disability groups.
5. Build human override and explainability into high-stakes decisions.
6. Pilot with disabled users and iterate on model and UI decisions.

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
