# AI for Creative Writing

## Description

Use large language models to co-write fiction and long-form prose, brainstorm outlines, calibrate voice, and run human-AI revision workflows.

## When to use

You are drafting fiction, scripts, or long-form prose and want an AI collaborator for ideation, continuation, style calibration, and revision.

## Usage

- Brainstorm premises, outlines, and character sheets for novels and scripts.
- Generate first drafts and continuations in a controlled voice and style.
- Use few-shot examples and style guides to keep output on-brand.
- Audit generated prose for stereotypes, toxicity, and hallucinations.

## Steps

1. Define the genre, audience, and style guide for the project.
2. Create an outline, character sheet, and world bible to maintain long-context coherence.
3. Generate scenes with structured prompts and a calibrated temperature.
4. Review and rewrite with a human-in-the-loop, checking voice consistency.
5. Run a toxicity, bias, and fact-check audit before finalizing the draft.

## Code pattern

```python
from transformers import pipeline

# A simple continuation pipeline for a fiction scene
generator = pipeline("text-generation", model="openai-community/gpt2")

prompt = """Continue the noir detective scene in first person, raining, 1920s Chicago:

The alley was a river of shadows..."""

output = generator(
    prompt,
    max_new_tokens=200,
    temperature=0.8,
    do_sample=True,
)
print(output[0]["generated_text"])
```

## Tuning notes

- Tune temperature for creativity (0.7-0.9) vs. coherence (lower).
- Constrain outputs with a style guide or constrained decoding to preserve voice.
- Chunk long manuscripts and feed context incrementally to avoid loss of continuity.
- Evaluate with human readers; use LLM-as-judge only as a secondary metric.

## Verification

1. Generate a 1,000-word scene from a provided outline and compare it to a style guide.
2. Maintain character consistency across three generated chapters using a shared character sheet.
3. Run a toxicity and bias audit on generated prose.

## References

- https://arxiv.org/abs/2209.14958
- https://doi.org/10.1145/3544548.3581225
- https://doi.org/10.48550/arxiv.2310.08433
- https://link.springer.com/article/10.1007/s00146-024-02127-3
