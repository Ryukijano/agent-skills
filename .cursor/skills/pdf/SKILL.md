---
name: pdf
description: >-
  Use this skill whenever the user wants to do anything with PDF files. This
  includes reading or extracting text/tables from PDFs, combining or merging
  multiple PDFs into one, splitting PDFs apart, rotating pages, adding
  watermarks, creating new PDFs, filling PDF forms, encrypting/decrypting PDFs,
  extracting images, and OCR on scanned PDFs.
---

# PDF Processing Guide

## Overview
This guide covers essential PDF processing operations using Python libraries and command-line tools.

## Quick Start
```python
from pypdf import PdfReader, PdfWriter

reader = PdfReader("document.pdf")
print(f"Pages: {len(reader.pages)}")

text = ""
for page in reader.pages:
    text += page.extract_text()
```

## Python Libraries

### pypdf - Basic Operations
- Merge PDFs: `writer.add_page(page)` from multiple readers
- Split PDF: One page per file using PdfWriter
- Extract Metadata: `reader.metadata.title`, `.author`, etc.
- Rotate Pages: `page.rotate(90)`

### pdfplumber - Text and Table Extraction
- Extract text with layout: `page.extract_text()`
- Extract tables: `page.extract_tables()`
- Advanced: Convert tables to pandas DataFrames

### reportlab - Create PDFs
- Basic: `canvas.Canvas("hello.pdf", pagesize=letter)`
- Multi-page: `SimpleDocTemplate` with `Paragraph`, `Spacer`, `PageBreak`
- **IMPORTANT**: Never use Unicode subscript/superscript in ReportLab. Use `<sub>` and `<super>` tags in Paragraph objects.

## Command-Line Tools
- `pdftotext input.pdf output.txt` — extract text
- `pdftotext -layout input.pdf output.txt` — preserve layout
- `qpdf --empty --pages file1.pdf file2.pdf -- merged.pdf` — merge
- `qpdf input.pdf --pages . 1-5 -- pages1-5.pdf` — split
- `pdfimages -j input.pdf output_prefix` — extract images

## Common Tasks
- OCR scanned PDFs: `pytesseract` + `pdf2image`
- Add watermark: merge watermark page with each page
- Password protection: `writer.encrypt("userpassword")`

## Quick Reference
| Task | Best Tool |
|------|-----------|
| Merge PDFs | pypdf |
| Split PDFs | pypdf |
| Extract text | pdfplumber |
| Extract tables | pdfplumber |
| Create PDFs | reportlab |
| Command line merge | qpdf |
| OCR scanned PDFs | pytesseract |
