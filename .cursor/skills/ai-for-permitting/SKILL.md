# AI for Permitting

## Description

Automated permit intake, plan review, code compliance checks, application completeness screening, and permit workflow optimization.

## When to use

You are streamlining building or development permits, automating intake screening, or supporting plan review.

## Usage

- **Application pre-screening**: check completeness and required documents.
- **Plan review**: detect code issues and compare against building/zoning codes.
- **Code compliance**: flag violations and cite relevant sections.
- **Workflow routing**: assign applications to reviewers by type and complexity.
- **Status and Q&A**: keep applicants informed and answer common questions.

## Steps

1. Map permit types, checklists, and review workflows.
2. Ingest application forms, drawings, and supporting documents.
3. Build rules and ML models for completeness and compliance checks.
4. Route flagged items to human reviewers with explanations.
5. Track cycle times, first-pass approval rates, and rework.

## Code pattern

```python
import pytesseract
from PIL import Image

# Extract text from a scanned permit drawing
img = Image.open("site_plan.pdf")
text = pytesseract.image_to_string(img)
print(text[:500])
```

## Tuning notes

- Preserve human approval authority and auditability.
- Train models on local codes and amendments.
- Handle scanned drawings and PDFs with OCR and computer vision.

## Verification

1. Run a sample of applications through pre-screening and compare to staff review.
2. Measure change in first-pass approval rate and cycle time.
3. Audit a sample of AI-flagged code issues for accuracy.

## References

- https://innovation-hub.seattle.gov/2026/06/17/ai-construction-permitting-seattle-civcheck-study/
- https://www.govtech.com/artificial-intelligence/honolulu-launches-ai-assisted-fast-track-permit-review
- https://www.archistar.ai/aiprecheck/ai-plan-review/
- https://iopscience.iop.org/article/10.1088/1755-1315/1648/1/012010
