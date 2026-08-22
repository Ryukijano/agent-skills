---
name: literature-triage-matrix
description: Compare papers systematically across method, data, metrics, claims, and limitations in a single matrix to expose gaps and position new work.
---

## Literature Triage Matrix

Build one matrix per research question; it becomes your related-work table seed.

### Matrix columns
| Column | What goes in |
|---|---|
| id / venue+year | short cite key |
| task & setting | exactly what they solve, incl. assumptions |
| method family | backbone, pretraining, supervision signal |
| data | datasets, sizes, train/test protocol |
| metric + headline number | their best result, verbatim |
| claim | what they say it proves |
| limitation | theirs stated + yours observed |
| relevance H/M/L | to your question |

### Workflow
1. Collect 15-30 candidate papers (via `explore-sota` / `literature-search-arxiv`).
2. Skim abstract → figures → tables → conclusion (5 min/paper); fill matrix row.
3. Only papers scoring High/Medium relevance get a full read (`digest-paper`).
4. Sort by relevance; read top 5 deeply.

### Gap extraction
After filling, ask across columns:
- Which settings/data are never tried? (empty cells = gaps)
- Which claims lack a common metric/baseline? (incomparable = opportunity)
- Which limitations recur? (recurring pain = your intro's motivation)

### Output
`<slug>/triage_matrix.csv` + a 10-line synthesis of the 3 strongest gaps, each with supporting row references.

Related: `gap-to-topic`, `digest-paper`, `explore-sota`.
