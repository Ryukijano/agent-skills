# AI for Infographics

## Description

Generating data-rich infographics and visual stories from documents, tables, and natural-language prompts.

## When to use

You want to turn reports, data tables, or articles into shareable infographics, data stories, or social-media explainers.

## Key concepts

- **Text-to-infographic**: generate metadata, chart code, and layout from natural language or documents.
- **Chart composition**: combine multiple sub-charts (bar, line, pie, maps) into a coherent layout.
- **Data faithfulness**: ensure values, labels, and visual proportions match the source data.
- **Visual hierarchy and accessibility**: guide the eye, use alt text, and maintain color-blind safe palettes.
- **Evaluation benchmarks**: use benchmarks like IGENBENCH to assess reliability of generated infographics.

## Code pattern

```python
import matplotlib.pyplot as plt

# Example: generate a chart component for later infographic assembly
categories = ["A", "B", "C"]
values = [12, 19, 8]
fig, ax = plt.subplots(figsize=(4, 3))
ax.bar(categories, values)
plt.savefig("chart_component.png")
```

## Tuning notes

- Verify every number and label against the source data table.
- Keep brand colors, fonts, and layout grids consistent.
- Avoid chart junk; prioritize the story over decoration.
- Test generated infographics with both data experts and general readers.

## Verification

1. Generate an infographic from a small table and verify every value and label.
2. Evaluate the output on a reliability benchmark or with a rubric for data faithfulness.
3. Compare engagement and comprehension between the infographic and the original table.

## References

- https://aclanthology.org/2025.acl-long.1003.pdf
- https://aclanthology.org/2026.acl-long.1713.pdf
- https://aclanthology.org/anthology-files/anthology-files/pdf/acl/2023.acl-demo.11.pdf
- https://arxiv.org/abs/2401.13245
- https://arxiv.org/abs/2505.18668v3
