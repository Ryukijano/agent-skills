# Digest Paper Run

One paper per run — atomic, all-or-nothing.

1. Resolve identity via Semantic Scholar (DBLP for CS); ask user only if genuinely ambiguous.
2. Resolve version: published venue > latest arXiv revision. Record DOI + arXiv ID.
3. Assign citekey `AuthorYearShortTitle`; verify unused.
4. Acquire legal full-text PDF to `sota/papers/<citekey>/paper.pdf`. No legal text → queue `unresolvable-via-mcp`, STOP (abstract-only forbidden).
5. Read cover-to-cover; write `synthesis.md` verifying exact numbers against PDF.
6. Append BibTeX to references.bib from MCP-sourced fields only.

Apply `digest-paper`.
