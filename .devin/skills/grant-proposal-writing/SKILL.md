# Grant Proposal Writing with AI

## Description

Structure Specific Aims, research strategy, budget, and broader impact sections for NIH/NSF/ERC-style proposals with AI drafting support.

## When to use

You are preparing a fellowship, R01, NSF CAREER, Horizon Europe, or other competitive research proposal and need a clear, compelling narrative.

## Key concepts

- **Specific Aims**: a concise statement of goals, hypotheses, and expected outcomes.
- **Significance / Innovation / Approach**: the core review criteria for many funders.
- **Broader impacts**: training, dissemination, societal benefit, and reproducibility.
- **Budget justification**: link personnel, equipment, and travel directly to aims.
- **Funder compliance**: follow page limits, formatting, and required sections exactly.

## Code pattern

```python
import yaml
from datetime import datetime, timedelta


def build_proposal_outline(title, aims, duration_months=36):
    outline = {
        "title": title,
        "specific_aims": aims,
        "research_strategy": ["significance", "innovation", "approach"],
        "timeline": [
            (datetime.now() + timedelta(days=30 * i)).strftime("%Y-%m")
            for i in range(duration_months)
        ],
        "broader_impacts": [],
        "budget_justification": [],
    }
    with open("proposal_outline.yaml", "w") as f:
        yaml.safe_dump(outline, f, sort_keys=False)
    return outline
```

## Tuning notes

- Write for both expert and non-expert reviewers; clarity beats complexity.
- Align every aim with a budget line and a measurable milestone.
- Use figures and timelines to make the approach concrete.
- Avoid over-promising; funders value realistic, well-scoped work plans.

## Verification

1. Draft a one-page Specific Aims document and check it against funder guidelines.
2. Build a full proposal outline and cross-reference every section to the instructions.
3. Share with a mentor or prior awardee for feedback on significance and feasibility.

## References

- https://www.nigms.nih.gov/Research/application/Pages/default
- https://www.nigms.nih.gov/training/Pages/Grant-Writing-Webinar-Series-for-Institutions-Building-Research--and-Research-Training-Capacity
- https://www.nigms.nih.gov/Research/application/Pages/Submitting-an-Application
- https://www.nimh.nih.gov/funding/grant-writing-and-application-process/grant-writing-assistance
- https://blogs.nature.com/blog/beginnings-how-to-write-your-first-grant-proposal/
