# AI for Competency Development

## Description

Competency-based education, skill gap analysis, adaptive credentialing, and AI-driven mastery and portfolio assessment.

## When to use

You are designing competency-based learning where demonstrated mastery, not seat time, drives progression and credentials.

## Key concepts

- **Competency frameworks and skills taxonomies**: ESCO, O*NET, or institutional competency maps.
- **Skill gap analysis**: compare current abilities to role or course requirements.
- **Mastery assessment**: evaluate observable performances and artifacts.
- **Portfolio and credentialing**: recognize competence through badges, micro-credentials, or transcripts.

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
