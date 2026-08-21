# AI for Pedagogy

## Description

Use AI to support teachers in planning, deliver, and improve instruction while keeping educators at the center of the learning process.

## When to use

You want to support teachers in planning, delivering, and improving instruction while keeping educators at the center of the learning process.

## Usage

- Co-design lesson plans and activities with teachers.
- Generate standards-aligned materials and differentiation options.
- Provide formative feedback on student work.
- Reduce administrative load while preserving teacher agency.

## Steps

1. Co-design lesson plans and activities with teachers.
2. Generate standards-aligned materials and differentiation options.
3. Provide formative feedback on student work.
4. Reduce administrative load while preserving teacher agency.
5. Pilot in classrooms and gather teacher and student feedback.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

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
