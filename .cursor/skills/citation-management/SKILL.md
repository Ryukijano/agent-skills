# Citation Management

## Description

Organize references, manage PDFs, format bibliographies, and share libraries with Zotero, Mendeley, or BibTeX.

## When to use

You are building a literature library, collaborating on a manuscript, or switching between citation styles for different venues.

## Key concepts

- **Reference manager**: Zotero, Mendeley, EndNote, JabRef, or BibTeX-based tools.
- **Citation Style Language (CSL)**: format bibliographies in thousands of styles.
- **Metadata cleanup**: verify DOIs, author names, journal titles, and page numbers.
- **Group libraries and shared collections**: collaborate with co-authors.
- **Import/export formats**: RIS, BibTeX, CSL-JSON, and Zotero connectors.

## Code pattern

```python
import bibtexparser
from collections import Counter


def load_and_dedup(bib_path):
    with open(bib_path) as f:
        db = bibtexparser.load(f)
    seen = set()
    unique = []
    for entry in db.entries:
        key = (entry.get("doi") or "").lower() or (
            entry.get("title", "") + entry.get("year", "")
        )
        if key not in seen:
            seen.add(key)
            unique.append(entry)
    db.entries = unique
    return db


def style_counts(db):
    return Counter(entry.get("ENTRYTYPE", "unknown") for entry in db.entries)
```

## Tuning notes

- Always verify imported metadata; PDF metadata is often noisy or incomplete.
- Use DOIs as stable identifiers and link them to Crossref for updates.
- Back up your library and sync across devices.
- Keep one master library and create project-specific collections.

## Verification

1. Import 20 references and generate bibliographies in APA and Vancouver styles.
2. Identify and merge duplicate entries.
3. Verify that all citations resolve to real DOIs or URLs.

## References

- https://www.zotero.org/support/quick_start_guide/
- https://www.zotero.org/support/styles
- https://service.elsevier.com/app/answers/detail/a_id/29356/supporthub/mendeley/role/referencemanagement/
- https://doi.org/10.1371/journal.pcbi.1006036
- https://doi.org/10.1038/npre.2009.3867.1
