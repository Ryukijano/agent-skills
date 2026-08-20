# AI for Creative Writing

## Description

Co-writing novels, screenplays, and long-form fiction with LLMs, prompt engineering for voice and style, and human-AI revision workflows.

## When to use

You are drafting fiction, scripts, or long-form prose and want an AI collaborator for ideation, continuation, style calibration, and revision.

## Key concepts

- **Human-AI co-writing**: treat the LLM as a brainstorming partner, outline generator, first-drafter, or revision assistant.
- **Voice and style control**: use few-shot examples, persona prompts, tone descriptors, and style guides to keep output on-brand.
- **Long-context planning**: maintain coherence across chapters or scenes with outlines, character sheets, and worldbuilding bibles.
- **Retrieval and memory**: use vector stores or note systems to ground the model in characters, settings, and prior events.
- **Bias and safety**: audit for stereotypes, toxicity, and hallucinations; respect copyright and cultural context.

## Code pattern

```python
from transformers import pipeline

# A simple continuation pipeline for a fiction scene
generator = pipeline("text-generation", model="gpt2")

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
