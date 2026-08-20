# AI for Product Requirements

## Description

Draft, validate, and track product requirements documents (PRDs) with user stories, assumptions, and success metrics.

## When to use

You are scoping a new feature or product, aligning engineering and design, or need a single source of truth for what to build and why.

## Key concepts

- **PRD (Product Requirements Document)**: defines purpose, features, behavior, and success criteria.
- **User stories and acceptance criteria**: who, what, and why for each capability.
- **Success metrics**: measurable outcomes tied to user and business goals.
- **Assumptions and out-of-scope**: manage risk and prevent scope creep.
- **Prioritization**: rank features by value, effort, and strategic fit.

## Code pattern

```python
import yaml
from datetime import date


def draft_prd(problem, solution, audience, metrics):
    prd = {
        "problem": problem,
        "solution_vision": solution,
        "target_audience": audience,
        "success_metrics": metrics,
        "assumptions": [],
        "out_of_scope": [],
        "user_stories": [],
        "last_updated": date.today().isoformat(),
    }
    with open("prd.yaml", "w") as f:
        yaml.safe_dump(prd, f, sort_keys=False)
    return prd


def add_user_story(prd, role, want, so_that, acceptance=[]):
    prd["user_stories"].append({
        "role": role,
        "want": want,
        "so_that": so_that,
        "acceptance_criteria": acceptance,
    })
    return prd
```

## Tuning notes

- Start with the problem and the user, not the implementation.
- Keep PRDs concise and living; update them as discovery progresses.
- Align engineering, design, and stakeholders before writing detailed specs.
- Tie each requirement to a success metric or user outcome.

## Verification

1. Write a one-page PRD for a feature.
2. Run it by an engineer, a designer, and a potential user.
3. Trace each user story to at least one design mock-up and one test.

## References

- https://www.atlassian.com/agile/product-management/requirements
- https://www.atlassian.com/software/confluence/templates/product-requirements
- https://www.atlassian.com/software/confluence/templates/requirements
- https://confluence.atlassian.com/doc/blog/2015/08/how-to-document-product-requirements-in-confluence
- https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf
