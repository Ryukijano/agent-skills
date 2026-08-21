# AI for Storytelling

## Description

Use structured LLM workflows to generate plots, build character arcs, manage worldbuilding, and create interactive or branching narratives.

## When to use

You are building interactive fiction, game narratives, brand stories, or structured plots with multiple acts and characters.

## Usage

- Generate three-act outlines, beat sheets, and plot-point scaffolding.
- Maintain character and world consistency with memory and knowledge graphs.
- Build branching dialogue and choices for interactive fiction and games.
- Use recursive summarization to preserve coherence in long-form stories.

## Steps

1. Write a one-page premise and target genre for the story.
2. Generate a structured outline with acts, beats, and character arcs.
3. Create a persistent character/world store and use it in every generation.
4. Draft scenes and branch points, then check continuity against the store.
5. Test with readers for engagement and coherence, then iterate.

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
