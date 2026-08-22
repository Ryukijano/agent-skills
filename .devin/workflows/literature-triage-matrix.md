# Literature Triage Matrix Run

1. Define ONE research question for the matrix.
2. Collect 15-30 candidates via /explore-sota or arXiv/OpenAlex search.
3. Skim pass: abstract→figures→tables→conclusion, 5 min/paper; fill matrix row (method/data/metric+number/claim/limitation/relevance).
4. Full-read only High/Medium rows (top ~5) via digest-paper.
5. Gap extraction: empty cells = gaps; incomparable claims = opportunity; recurring limitations = intro motivation.
6. Output `<slug>/triage_matrix.csv` + 10-line synthesis of top-3 gaps.

Apply `literature-triage-matrix`, `explore-sota`, `digest-paper`.
