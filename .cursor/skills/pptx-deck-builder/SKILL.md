---
name: pptx-deck-builder
description: Generate conference talks, posters, and reports programmatically — python-pptx/pandoc workflows, 16:9 discipline, figure sizing, and speaker notes.
---

## Deck & Document Builder

### Tool choice
- **Slides**: `python-pptx` for full control; pandoc markdown → pptx for quick drafts.
- **Posters**: A0/A1 via PowerPoint template from the venue, or LaTeX beamerposter.
- **Docs/reports**: pandoc markdown → docx/pdf (`pandoc report.md -o report.docx --reference-doc=template.docx`).

```python
from pptx import Presentation
from pptx.util import Inches

prs = Presentation()                       # defaults to 16:9 (13.33 x 7.5 in)
slide = prs.slides.add_slide(prs.slide_layouts[6])   # blank
slide.shapes.add_picture("fig.pdf", Inches(1), Inches(1.5), width=Inches(8))
prs.save("talk.pptx")
```

### Slide rules
- One message per slide, stated as the title ("MPC dominates at low latency", not "Results 2").
- ≤ 6 bullets × ≤ 8 words, or one figure + 2 takeaway lines. No paragraph slides — ever.
- Figures sized to final placement (16:9 canvas 13.33×7.5in); regenerate plots with deck-sized fonts instead of scaling up.
- Speaker notes carry the narration; write them per slide.

### Talk skeleton (conference, 5 min)
Problem (30s) → gap (30s) → approach core idea (90s) → key result figure (90s) → limitations+honesty (45s) → takeaways (15s). Rehearse against a timer twice.

### Consistency
- Deck fonts/colors match the paper's figures; same terminology glossary.
- Store `make_deck.py` next to `make_figures.py` so both rebuild from the same result JSONs.

Related: `data-visualization-and-figures`, `scientific-writing`, `manage-submission`.
