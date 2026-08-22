---
name: digest-paper
description: >-
  Digest one paper atomically: PDF to synthesis, BibTeX entry, and index row.
  Use when ingesting a single paper by title, DOI, arXiv ID, URL, or PDF into
  a literature collection. One paper per run; all-or-nothing completion.
---

# Digest Paper

Atomic unit of literature work: **PDF → synthesis → bib entry → index row**. One paper per run; completes fully or not at all.

## Verification Loop

**Resolve identity → read full text → synthesize → verify every claim/number against PDF → refine synthesis → lock artifacts.**

## Read First

- `sota/README.md` or project synthesis format spec
- [references/citation-format.md](references/citation-format.md) — citekeys and BibTeX rules
- `references.bib` and `sota/index.md` — avoid duplicates

## MCP / API Preflight

Confirm arXiv and Semantic Scholar respond before starting. If lookup fails, STOP. No model-memory citations.

## Procedure

1. **Resolve identity** — Match via Semantic Scholar (DBLP for CS). Ask user only if genuinely ambiguous.
2. **Resolve version** — Published venue > latest arXiv revision > other preprint. Record DOI and arXiv ID when both exist.
3. **Assign citekey** — `AuthorYearShortTitle` lowercase; verify unused in bib and `sota/papers/`.
4. **Acquire PDF** — Download to `sota/papers/<citekey>/paper.pdf`. If no legal full text, stop and queue as `unresolvable-via-mcp`. Abstract-only forbidden.
5. **Read cover-to-cover** — Full PDF, not abstract alone.
6. **Write synthesis.md** — Follow project section order. Verify exact numbers and quotations against PDF.
7. **Write BibTeX** — Append to `references.bib` from MCP-sourced fields per [citation-format.md](references/citation-format.md).
8. **Write metadata.yaml** — IDs, verified block, selected cites/cited_by (citekeys for known papers).
9. **Append index row** — `sota/index.md` with status `digested`.
10. **Queue leads** — Add in-scope citation leads to `sota/queue.md` as `pending` with provenance.
11. **Verify** — Cross-check synthesis claims against PDF; fix before locking.

## Synthesis Template

```markdown
# <Title> (<Year>)

## TL;DR
[2–3 sentences]

## Problem & Motivation
## Method
## Key Results
[Numbers verified against PDF]
## Limitations
## Relevance to Our Work
## Citation Leads
- [citekey or external id] — why relevant
```

## Rules

- All-or-nothing: partial folder → delete and record in queue instead.
- One paper = one folder = one bib entry = one index row.
- Never write bib fields from memory; MCP cross-check required.
- While digesting, only cross-paper edit allowed: upgrade external IDs to citekeys in other papers' citation lists.

## Done When

- `sota/papers/<citekey>/` contains `paper.pdf`, `synthesis.md`, `metadata.yaml`
- Exactly one new bib entry and one index row
- All quantitative claims in synthesis verified against PDF
