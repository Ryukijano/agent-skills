# AI for White Papers

## Description

Author long-form, evidence-based white papers and thought-leadership documents that define problems, survey evidence and present solutions while establishing credibility.

## When to use

You are producing a B2B or technical white paper that defines a problem, surveys evidence, presents a solution, and establishes thought leadership.

## Usage

- **State the problem, quantify the cost, and present an evidence-based approach.**
- **Write the executive summary last, place it first, and make it self-contained.**
- **Support claims with benchmarks, peer-reviewed studies, and real customer outcomes.**
- **Include practical guidance on cost, benefits, and adoption.**
- **Maintain a consistent, professional tone and visual format.**

## Steps

1. Define the audience, objective, and key evidence sources before drafting.
2. Research and synthesize industry data, benchmarks, peer-reviewed studies, and customer case studies.
3. Build a structured outline with problem, evidence, solution, implementation, and ROI sections.
4. Draft the body section by section, feeding the model verified sources and avoiding invented citations.
5. Write the executive summary as a self-contained synthesis of the full paper.
6. Fact-check all claims, align with brand voice and design, and export to editable formats.

## Code pattern

```python
from jinja2 import Template

# Example: fill a white-paper outline template from structured evidence
template = Template(open("whitepaper_template.md").read())
doc = template.render(
    title="Edge AI for Manufacturing",
    problem="High latency and cloud costs",
    evidence=evidence_list,
)
```

## Tuning notes

- Decouple evidence retrieval from drafting; never let the model invent sources.
- Define audience, length, and sections before generating text.
- Use a second model or human reviewer to challenge unsupported claims.
- Export to editable formats (DOCX, PDF) with consistent styles and branding.

## Verification

1. Produce an executive summary and confirm it accurately reflects the full paper.
2. Spot-check every statistic and citation against its original source.
3. Compare the AI-assisted white paper to a prior human-written one for tone and structure.

## References

- https://journals.sagepub.com/doi/10.1177/00472816251332208
- https://doi.org/10.1007/978-981-95-4632-9_10
- https://specswriter.com/blog/ai_white_papers_how_to_write_one_people_actually_finish.php
- https://www.qwe.edu.pl/tutorial/how-to-use-ai-to-write-white-papers/
