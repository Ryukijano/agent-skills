---
name: xlsx
description: >-
  Create, edit, and analyze Excel spreadsheets. Use when the user wants to
  generate .xlsx files with formulas, build financial models, edit existing
  spreadsheets, or extract data from Excel files.
---

# XLSX Creation, Editing, and Analysis

## Overview
Create and edit Excel files using openpyxl and pandas.

## CRITICAL: Use Formulas, Not Hardcoded Values
- WRONG: `cell.value = 42` (hardcoded)
- CORRECT: `cell.value = "=SUM(A1:A10)"` (formula)

## Creating New Excel Files
```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill

wb = Workbook()
ws = wb.active
ws.title = "Sheet1"
ws['A1'] = "Header"
ws['A1'].font = Font(bold=True)
ws['A2'] = 10
ws['A3'] = 20
ws['A4'] = "=SUM(A2:A3)"
wb.save("output.xlsx")
```

## Editing Existing Excel Files
```python
from openpyxl import load_workbook
wb = load_workbook("existing.xlsx")
ws = wb["Sheet1"]
ws['B1'] = "New Value"
wb.save("modified.xlsx")
```

## Data Analysis with pandas
```python
import pandas as pd
df = pd.read_excel("data.xlsx", sheet_name="Sheet1")
print(df.describe())
df.to_excel("results.xlsx", index=False)
```

## Formula Verification Checklist
- Essential: Check for `#REF!`, `#VALUE!`, `#NAME?` errors
- Common Pitfalls: Relative vs absolute references ($A$1 vs A1)
- Test: Use `openpyxl` to read calculated values after save

## Best Practices
- Use `openpyxl` for formatting and formulas
- Use `pandas` for data analysis
- Professional font: Calibri 11pt default
- Color coding: Blue for inputs, black for formulas, green for links
