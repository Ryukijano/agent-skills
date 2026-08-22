---
name: data-visualization-and-figures
description: Publication-ready scientific figures — plot design, colorblind-safe palettes, multi-panel layouts, graphical abstracts, vector export, and venue spec compliance.
---

## Data Visualization & Figures

### Design rules
- One message per figure; state it in the caption's last sentence.
- Order categories by value (not alphabetically) unless order is semantic.
- Direct-label lines instead of legend boxes when feasible.
- Log scale for spanning >2 decades; annotate the threshold that matters.

### Style
- Colorblind-safe palettes: `viridis`/`cividis` for continuous, Okabe-Ito for categorical.
- Sans-serif fonts matching paper text (Helvetica/Arial); axis labels ≥ 7pt at print size.
- No chartjunk: drop unnecessary gridlines, 3D, dual axes, pie charts (>3 slices).

### Multi-panel figures
- Panel letters **(a)(b)(c)** top-left, consistent across all figures.
- Shared legends once per row; aligned axes within a column.
- Build with `matplotlib` subplots / `seaborn.objects` — never screenshot collages.

```python
import matplotlib.pyplot as plt
plt.rcParams.update({
    "figure.dpi": 300, "savefig.format": "pdf",
    "font.family": "sans-serif", "axes.spines.top": False,
    "axes.spines.right": False,
})
```

### Export & venue specs
- Vector (PDF/SVG) for plots; 300+ dpi PNG/TIFF only for raster imagery (endoscopy frames).
- Check target venue column width (~3.3in single / ~7in double for IEEE) and set `figsize` to final size — no rescaling in LaTeX.
- Keep a `figures/make_figures.py` that regenerates every paper figure from committed result JSONs.

Related: `scientific-writing`, `ablation-study`, `experiment-tracking`.
