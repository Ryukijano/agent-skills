# AI for Pedagogy

## Description

Teacher-AI collaboration, lesson planning, instructional design, feedback generation, and evidence-based teaching practice augmentation.

## When to use

You want to support teachers in planning, delivering, and improving instruction while keeping educators at the center of the learning process.

## Key concepts

- **Teacher-AI co-design**: generative AI as a collaborator, not a replacement, for educators.
- **Lesson and activity generation**: create standards-aligned plans, materials, and assessments.
- **Formative feedback**: provide teachers with insights on student understanding.
- **TPACK and professional development**: build the knowledge needed to integrate AI responsibly.

## Code pattern

```python
import openai

# Co-create a differentiated lesson plan with a local or API LLM
prompt = (
    "Design a 45-minute middle-school science lesson on photosynthesis. "
    "Include learning objectives, a hands-on activity, and two differentiation options."
)
lesson = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an experienced instructional coach."},
        {"role": "user", "content": prompt},
    ],
)
```

## Tuning notes

- Preserve teacher agency and local curriculum context.
- Verify accuracy of AI-generated content, especially in specialized subjects.
- Use AI to reduce administrative load, not to deskill teaching.

## Verification

1. Generate a lesson plan and have a teacher review it for quality and fit.
2. Adapt a plan for two different learner profiles and collect feedback.
3. Measure time saved and teacher satisfaction with an AI-assisted planning tool.

## References

- https://link.springer.com/article/10.1007/s10956-024-10174-0
- https://dl.acm.org/doi/10.1145/3788074
- https://link.springer.com/article/10.1007/s40751-024-00168-3
- https://link.springer.com/article/10.1007/s10639-025-13699-y
