# Research Presentation Design

## Description

Build clear, compelling slides and posters for seminars, conferences, and outreach using narrative structure and visual hierarchy.

## When to use

You are preparing a conference talk, seminar, thesis defense, poster session, or public outreach presentation.

## Key concepts

- **One idea per slide**: keep each slide focused on a single message.
- **Assertion-Evidence structure**: state a claim and support it with a visual.
- **Visual hierarchy**: use size, color, and position to guide attention.
- **Data-ink ratio**: remove unnecessary chart elements and decoration.
- **Accessibility**: use readable fonts, high contrast, and alt text.

## Code pattern

```python
from pptx import Presentation
from pptx.util import Inches, Pt


prs = Presentation()
slide = prs.slides.add_slide(prs.slide_layouts[5])  # blank slide
title_box = slide.shapes.add_textbox(
    Inches(0.5), Inches(0.5), Inches(9), Inches(1)
)
tf = title_box.text_frame
tf.text = "One clear message per slide"
p = tf.paragraphs[0]
p.font.size = Pt(32)
p.font.bold = True

# Add a placeholder for a figure
left = Inches(1)
top = Inches(1.8)
slide.shapes.add_picture("plot.png", left, top, height=Inches(4.5))
prs.save("presentation.pptx")
```

## Tuning notes

- Design for the back of the room: large fonts, simple figures, minimal text.
- Practice timing; a 15-minute talk needs a tight narrative arc.
- Use consistent colors, fonts, and alignment across all slides.
- Include a take-home slide with the main conclusion and contact info.

## Verification

1. Build a 10-slide deck and test it on a projector or large screen.
2. Critique a peer's slides for visual hierarchy and data-ink ratio.
3. Deliver the talk to a practice audience and gather feedback.

## References

- https://doi.org/10.1371/journal.pcbi.0030077
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1009554
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005373
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1007163
