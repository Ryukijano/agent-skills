---
name: pptx
description: >-
  Create, edit, and analyze PowerPoint presentations. Use when the user wants to
  generate slide decks, pitch decks, or presentations, or extract text from
  .pptx files.
---

# PPTX Skill

## Quick Reference
- Reading: `from pptx import Presentation; prs = Presentation("file.pptx")`
- Creating: `prs = Presentation(); slide = prs.slides.add_slide(prs.slide_layouts[1])`
- Converting to images: `libreoffice --headless --convert-to pdf` then `pdftoppm`

## Creating from Scratch
```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()
slide_layout = prs.slide_layouts[1]  # Title and Content
slide = prs.slides.add_slide(slide_layout)
title = slide.shapes.title
title.text = "Slide Title"
content = slide.placeholders[1]
content.text = "Bullet point 1\nBullet point 2"
prs.save("presentation.pptx")
```

## Design Ideas
- Color Palettes: Use 2-3 complementary colors max
- Typography: Sans-serif for headers, serif for body (or consistent sans-serif)
- Spacing: Leave breathing room — don't cram slides
- Avoid: Too much text per slide, tiny fonts, low contrast

## QA (Required)
- Content QA: Check spelling, factual accuracy, consistent terminology
- Visual QA: Check alignment, font sizes, image quality, color contrast
- Verification: Convert to images and visually inspect each slide

## Converting to Images
```bash
python scripts/office/soffice.py --headless --convert-to pdf output.pptx
pdftoppm -jpeg -r 150 output.pdf slide
```

## Dependencies
- `python-pptx` for creation and editing
- `libreoffice` for conversion
- `pdftoppm` (poppler-utils) for image extraction
