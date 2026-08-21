# AI for Infographics

## Description

Turn reports, data tables and articles into data-rich infographics and visual stories using natural-language prompts and chart-composition tools.

## When to use

You want to turn reports, data tables, or articles into shareable infographics, data stories, or social-media explainers.

## Usage

- **Generate metadata, chart code, and layout from natural language or documents.**
- **Combine multiple sub-charts (bar, line, pie, maps) into a coherent layout.**
- **Ensure values, labels, and visual proportions match the source data.**
- **Guide the eye, use alt text, and maintain color-blind safe palettes.**
- **Use benchmarks like IGENBENCH to assess reliability of generated infographics.**

## Steps

1. Extract the key data, insights, and narrative from the source document or table.
2. Choose the chart types and layout that best communicate the story for the target channel.
3. Generate chart code and metadata, then verify every value and label against the source.
4. Compose sub-charts into an on-brand layout with clear visual hierarchy and alt text.
5. Evaluate the infographic for data faithfulness with a rubric or benchmark like IGENBENCH.
6. Test engagement and comprehension with both data experts and general readers.

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
