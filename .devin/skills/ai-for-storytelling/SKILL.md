# AI for Storytelling

## Description

Narrative generation, plot planning, character arcs, and worldbuilding with structured LLM workflows.

## When to use

You are building interactive fiction, game narratives, brand stories, or structured plots with multiple acts and characters.

## Key concepts

- **Narrative planning**: outlines, beat sheets, story graphs, and plot-point scaffolding.
- **Character and world consistency**: memory, character sheets, and knowledge graphs to preserve continuity.
- **Interactive storytelling**: branching choices, dynamic dialogue, and player or reader agency.
- **Long-form coherence**: recursive summarization and hierarchical generation.
- **Evaluation**: narrative coherence, engagement, originality, and human judgment.

## Code pattern

```python
from openai import OpenAI

client = OpenAI()

outline = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You are a narrative architect."},
        {"role": "user", "content": "Create a three-act outline for a sci-fi heist story."},
    ],
    temperature=0.7,
)
print(outline.choices[0].message.content)
```

## Tuning notes

- Decompose generation into premise, outline, scenes, and prose.
- Use structured output (JSON or YAML) to control acts and characters.
- Keep a persistent world and character store for multi-session stories.
- Test with readers for narrative engagement and coherence.

## Verification

1. Generate a complete story arc with premise, outline, and three scenes.
2. Track character consistency through a 2,000-word passage.
3. Run an A/B test comparing human vs. AI story continuations.

## References

- https://aclanthology.org/2025.findings-emnlp.750/
- https://aclanthology.org/2023.inlg-main.23.pdf
- https://www.mdpi.com/2227-7390/13/23/3885
- https://aclanthology.org/2024.findings-emnlp.824/
