# LaTeX Paper Writer Run

1. GATE: draft `plan/<paper>.md` (title options, section skeleton, venue template) — wait for human approval. No prose before this.
2. Scaffold from official venue template; never hand-edit .sty/.cls/.bst.
3. Create `issues/paper.csv` with per-section acceptance criteria + target citations.
4. Work issue by issue; every `\cite{}` verified against arXiv/OpenAlex/CrossRef BEFORE entering ref.bib.
5. Unverifiable claim → `% TODO` comment, never a fabricated reference.
6. Tables via booktabs; units via siunitx; labels + \cref everywhere (no hardcoded "Figure 3").
7. Compile loop until clean: pdflatex → bibtex → pdflatex ×2; grep log for undefined/multiply-defined — must be empty.

Apply `latex-paper-writer`, `claim-verification`, `scientific-writing`.
