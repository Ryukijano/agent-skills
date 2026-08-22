---
name: latex-paper-writer
description: Gated LaTeX paper pipeline — plan approval, issue-driven section writing, web-verified citations, BibTeX hygiene, and compile-or-it-is-not-done delivery.
---

## LaTeX Paper Writer

### Hard gates
1. **No prose before plan approval.** Draft `plan/<paper>.md` with title options, section skeleton, target venue template, and clarification questions. Wait for human approval.
2. **No unverified citations.** Every `\cite{}` is checked against a real source (arXiv/OpenAlex/CrossRef) before entering `ref.bib`. A claim without evidence becomes `% TODO` — never a fabricated reference.
3. **Compiles or it is not done.** Delivery requires clean `pdflatex` + `bibtex` with zero undefined citations/references:

```bash
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
grep -i "undefined\|multiply defined" main.log   # must be empty
```

### Issue-driven execution
- Maintain `issues/paper.csv`: section, description, target citations, acceptance criteria, status.
- Work issue by issue; mark DONE only when acceptance criteria hold. Split issues when scope grows.

### Hygiene
- Venue template from official source (IEEEtran for ISBI/ICRA-style, cvpr.sty for CV venues); never hand-edit .sty/.cls/.bst.
- `\label{}` after every float/equation; reference via `\ref`/`\cref` — no hardcoded "Figure 3".
- SI units via `siunitx`; tables via `booktabs` (`\toprule/\midrule/\bottomrule`, no vertical lines).
- Diff-friendly: one sentence per line where practical.

Related: `scientific-writing`, `manage-submission`, `claim-verification`.
