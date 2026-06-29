---
name: docx
description: >-
  Create, edit, and analyze Word documents. Use when the user wants to generate
  .docx files, edit existing Word documents with tracked changes, convert .doc
  to .docx, or extract content from Word documents.
---

# DOCX Creation, Editing, and Analysis

## Overview
Create and edit Word documents using python-docx and OOXML manipulation.

## Quick Reference
- Convert .doc to .docx: `libreoffice --headless --convert-to docx`
- Read content: `doc = Document("file.docx")` then iterate `doc.paragraphs`
- Convert to images: `libreoffice --headless --convert-to pdf` then `pdftoppm`

## Creating New Documents
```python
from docx import Document
from docx.shared import Inches, Pt

doc = Document()
doc.add_heading('Report Title', 0)
doc.add_paragraph('Body text here')
doc.add_page_break()
doc.add_heading('Section 2', 1)
doc.save('output.docx')
```

### Tables
```python
table = doc.add_table(rows=3, cols=3)
for row in table.rows:
    for cell in row.cells:
        cell.text = 'data'
```

### Styles, Lists, Images, Hyperlinks
- Lists: `doc.add_paragraph(text, style='List Bullet')` or `'List Number'`
- Images: `doc.add_picture('image.png', width=Inches(4))`
- NEVER use unicode bullets — use built-in list styles

## Editing Existing Documents
1. Unpack: `unzip document.docx -d unpacked/`
2. Edit XML in `word/document.xml`
3. Pack: `cd unpacked && zip -r ../output.docx .`

## Tracked Changes
- Use OOXML XML manipulation for tracked changes
- Accept tracked changes: `libreoffice --headless --convert-to docx:"MS Word 2007 XML"`

## Dependencies
- `python-docx` for creation and reading
- `lxml` for XML manipulation
- `libreoffice` for conversion
