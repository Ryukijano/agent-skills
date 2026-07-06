---
name: academic-plotting
description: >-
  Generate publication-quality figures for ML papers: architecture diagrams and
  data-driven charts with venue-specific styling. Use when creating figures for
  papers.
---

# Academic Plotting

## Figure Types
- **Architecture diagrams**: Block diagrams of model/pipeline
- **Quantitative plots**: Loss curves, accuracy bars, ablation tables
- **Qualitative results**: Visualizations, attention maps, t-SNE

## Style Guide
- Font: serif (Times) for text, sans-serif for labels
- Size: single column (3.25in), double column (6.75in)
- DPI: 300+ for raster, vector (PDF) preferred
- Color: colorblind-friendly palette (tab10, Set2)
- Bold legends, clear axis labels with units

## matplotlib/seaborn
```python
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid', {'font.family': 'serif'})
fig, ax = plt.subplots(figsize=(3.25, 2.5), dpi=300)
ax.plot(x, y, label='Ours', linewidth=2)
ax.set_xlabel('Epoch', fontweight='bold')
ax.legend(fontsize=8)
plt.tight_layout()
fig.savefig('fig1.pdf', bbox_inches='tight')
```

## Common Plots
- Training curves: epoch vs loss/accuracy, multiple runs
- Ablation bars: grouped bar chart with error bars
- Confusion matrix: heatmap with annotations
- t-SNE/UMAP: scatter with class colors
