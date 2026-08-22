---
name: prisma-systematic-review
description: >-
  Conduct a PRISMA-style systematic review: search multiple databases, screen
  titles/abstracts and full text, extract data, and synthesize findings. Use
  when performing structured literature reviews, meta-reviews, evidence
  synthesis, or reproducible survey methodology with PRISMA reporting.
---

# PRISMA Systematic Review

Iterative loop: **search → screen → extract → synthesize → verify → refine**.

## Verification Loop

Each phase ends with reconciliation: **search → synthesize candidate set → verify against inclusion criteria → refine queries or criteria**.

## Read First

- [references/checklist.md](references/checklist.md) — PRISMA 2020 checklist
- `reviews/<topic>/` workspace (create if missing):
  - `protocol.md` — question, criteria, databases
  - `search-log.md` — queries and hit counts
  - `screening.csv` — one row per record
  - `extractions/` — one file per included study
  - `synthesis.md` — narrative + PRISMA counts

## Procedure

### Phase 1: Protocol

1. Define PICO/SPIDER elements (Population, Intervention, Comparison, Outcome).
2. Write inclusion/exclusion criteria before searching.
3. Pre-register search strategy in `protocol.md`.
4. Select databases: arXiv, Semantic Scholar, PubMed, IEEE Xplore as appropriate.

### Phase 2: Search

1. Build Boolean/keyword queries per database.
2. Log each query, date, database, and raw hit count in `search-log.md`.
3. Export deduplicated records to `screening.csv` with columns:
   `id, title, authors, year, source, doi, abstract, phase, decision, reason, reviewer`.

### Phase 3: Screen (title/abstract)

1. Two-pass when possible: independent screen, then reconcile disagreements.
2. Mark each row: `include`, `exclude`, `uncertain`.
3. Exclusions require reason code from protocol.
4. Update PRISMA counts: identified, deduplicated, screened, excluded.

### Phase 4: Screen (full text)

1. Retrieve PDFs for `include` from title/abstract phase.
2. Apply full-text criteria; record exclusion reasons.
3. Unresolvable PDFs → `excluded: full-text-unavailable`.

### Phase 5: Extract

For each included study, create `extractions/<id>.md`:

- Study design, sample, methods, outcomes, effect sizes
- Quality assessment (Cochrane ROB, CASP, or domain-appropriate tool)
- Data needed for synthesis tables

### Phase 6: Synthesize

1. Narrative synthesis grouped by theme or outcome.
2. Summary tables: study characteristics, findings, quality.
3. Assess heterogeneity; note gaps and publication bias risks.
4. Write `synthesis.md` with PRISMA flow diagram counts.

### Phase 7: Verify & refine

1. Spot-check 10% of extractions against source PDFs.
2. Reconcile count arithmetic in PRISMA diagram.
3. If gaps found, refine search and repeat from Phase 2.

## PRISMA Count Template

```
Identified: N
Deduplicated: N
Screened (title/abstract): N → Excluded: N
Full-text assessed: N → Excluded: N (reasons: ...)
Included in synthesis: N
```

## Rules

- Criteria fixed before screening; changes logged with justification.
- Every exclusion has a coded reason.
- No study enters synthesis without full-text review.
- Conflicts of interest and funding noted per extraction.

## Done When

- PRISMA checklist in [checklist.md](references/checklist.md) addressed
- `screening.csv` complete with no orphan `uncertain` rows
- `synthesis.md` includes flow counts and evidence tables
- Spot-check verification passed or discrepancies resolved
