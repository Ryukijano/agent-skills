# AI for Competency Development

## Description

Use AI to design competency-based learning where demonstrated mastery, not seat time, drives progression and credentials.

## When to use

You are designing competency-based learning where demonstrated mastery, not seat time, drives progression and credentials.

## Usage

- Map roles to competency frameworks such as ESCO or O*NET.
- Assess current skills and identify gaps.
- Recommend micro-credentials and learning resources.
- Build portfolios and mastery evidence.

## Steps

1. Map roles to competency frameworks such as ESCO or O*NET.
2. Assess current skills and identify gaps.
3. Recommend micro-credentials and learning resources.
4. Build portfolios and mastery evidence.
5. Compare credential outcomes to employer or academic requirements.
6. Integrate with LMS and virtual-teaching-assistant telemetry, then A/B test AI scaffolds and engagement interventions (JELAI-style).

## Code pattern

```python
import pandas as pd

# Simple skill gap matrix for a learner against a role profile
required = {"python": 4, "sql": 3, "communication": 3}
learner = {"python": 3, "sql": 2, "communication": 4}

gaps = {skill: max(0, required[skill] - learner.get(skill, 0)) for skill in required}
```

## Tuning notes

- Define competencies as observable and assessable behaviors.
- Combine formative evidence, summative assessments, and authentic tasks.
- Ensure credentials are portable and aligned with employer or academic standards.

## Verification

1. Map a course or program to a competency framework.
2. Assess learner mastery with a rubric and compare to a traditional grade.
3. Recommend targeted resources based on identified skill gaps.

## References

- https://doi.org/10.1016/j.caeai.2025.100485
- https://doi.org/10.66053/aillce.v1i1.29
- https://doi.org/10.1111/bjet.13556
- https://link.springer.com/article/10.1007/s44366-025-0039-x
