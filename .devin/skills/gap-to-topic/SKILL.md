---
name: gap-to-topic
description: Three-gate go/no-go dossier for a candidate research topic — is the gap open, is there a contribution, is it feasible — before committing months of work.
---

## Gap to Topic

Run before starting any multi-month project (thesis chapter, paper, grant aim). Output: `topic_dossier.md` with a verdict per gate.

### Gate 1 — Open? (`open: yes/no`)
- Search arXiv/OpenAlex/Semantic Scholar for direct prior art on the exact question.
- Check recent proceedings (2 years) of your 3 target venues, not just journals.
- A paper "close but not quite" is fine; a paper that did it kills the topic.
- Record the 5 closest papers and one-line delta each.

### Gate 2 — Contribution? (`contribution: yes/no/unclear`)
- State the delta in one sentence a reviewer would accept: "Unlike X, we Y, which enables Z."
- Contribution types that count: new method with evidence, new benchmark/dataset, strong negative result with analysis, significant efficiency gain.
- If the only delta is "+2% on one dataset", contribution = unclear → iterate or drop.

### Gate 3 — Feasible? (`feasible: yes/no`)
- **Data**: exists? accessible? license/ethics clear? (e.g., Cholec80 available; clinical video needs approval)
- **Compute**: rough GPU-hours vs what you have (AIRE allocation / Spark); can the pilot run in <1 week?
- **Skill/time**: does it need expertise you lack? deadline realistic?
- Define the **minimal viable experiment**: smallest run that would prove/disprove the core hypothesis.

### Verdict
`GO` (all yes) / `PIVOT` (1-2 gates weak, propose fix) / `NO-GO` (gate 1 no, or gate 3 no without workaround). Always record `verdict_reason`.

Related: `research-strategy-project-design`, `literature-triage-matrix`, `hypothesis-canvas`.
