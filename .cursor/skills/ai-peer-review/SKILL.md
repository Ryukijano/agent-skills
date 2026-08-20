# AI-Assisted Peer Review

## Description

Use AI tools and structured checklists to write constructive, ethical peer reviews for manuscripts and proposals.

## When to use

You are reviewing a manuscript, preprint, or conference submission and want to produce a fair, structured, and actionable review.

## Key concepts

- **COPE guidelines**: ethical standards for reviewers, editors, and authors.
- **Novelty, significance, rigor**: core dimensions of scientific evaluation.
- **Confidentiality and conflict of interest**: protect unpublished work and declare biases.
- **Constructive critique**: separate major concerns from minor suggestions.
- **Responsible AI use**: disclose any AI assistance and verify generated claims.

## Code pattern

```python
from pathlib import Path


def review_checklist(manuscript_text):
    checklist = {
        "novelty_and_significance": False,
        "methods_and_rigor": False,
        "data_availability": False,
        "ethical_approval": False,
        "conflict_of_interest": False,
        "ai_assistance_disclosed": False,
        "constructive_tone": False,
    }
    # Use keyword checks as a starting point; human judgment is required.
    if "data availability" in manuscript_text.lower():
        checklist["data_availability"] = True
    if "ethical" in manuscript_text.lower() or "irb" in manuscript_text.lower():
        checklist["ethical_approval"] = True
    return checklist


with open("manuscript.txt") as f:
    print(review_checklist(f.read()))
```

## Tuning notes

- Never upload a confidential manuscript into a public AI tool without permission.
- Use AI to organize your own notes, not to replace domain judgment.
- Be specific: cite line numbers, figures, or equations when raising issues.
- Distinguish required revisions from optional suggestions.

## Verification

1. Write a review of a sample paper using the checklist.
2. Compare your review against the journal's reviewer guidelines.
3. Have a colleague read it and confirm the tone is constructive and fair.

## References

- https://www.nature.com/nature/for-referees
- https://www.nature.com/nature/for-referees/how-to-write-a-report
- https://www.nature.com/nm/editorial-policies/ai
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.0020110
- https://www.nature.com/articles/s41565-026-02177-2
