# Citation Format Reference

## Citekey Convention

```
<firstauthor><year><shorttitle>
```

- Lowercase, no spaces (use camelCase or hyphens sparingly)
- First author family name + 4-digit year + 1–3 distinctive words
- Examples: `vaswani2017attention`, `he2016resnet`, `brown2020gpt3`

Resolve collisions with suffix: `smith2020survey`, `smith2020surveyb`.

## BibTeX Entry Types

| Source | Entry type |
|--------|------------|
| Journal | `@article` |
| Conference | `@inproceedings` |
| arXiv only | `@misc` with `eprint` and `archivePrefix={arXiv}` |
| Book | `@book` |

## Required Fields

### @article
`author`, `title`, `journal`, `year`, `volume`, `pages`, `doi`

### @inproceedings
`author`, `title`, `booktitle`, `year`, `pages`, `doi` (if available)

### @misc (arXiv)
`author`, `title`, `year`, `eprint`, `archivePrefix`, `primaryClass`

## Version Resolution Priority

1. Published peer-reviewed version (venue page or DOI)
2. Latest arXiv revision
3. Other preprints

When both exist, bib entry uses published metadata; note arXiv ID in `note` or `eprint`.

## Cross-Validation Rules

- Author list: match Semantic Scholar or publisher page
- Title: exact casing from source; use `{Braces}` for proper nouns
- Year: publication year, not first-arXiv year unless unpublished
- DOI: verify resolves; never invent
- Pages: from published version only

## Index Row Format

```markdown
| citekey | year | title | venue | status | tags |
|---------|------|-------|-------|--------|------|
| vaswani2017attention | 2017 | Attention Is All You Need | NeurIPS | digested | transformers |
```

## Verified Block (metadata.yaml)

```yaml
verified:
  date: YYYY-MM-DD
  sources: [semantic-scholar, arxiv]
  pdf_sha256: <hash if computed>
  full_text_read: true
```
