---
name: proof-forensics
description: Use when a proof, derivation or manuscript must be refereed independently, with every inference classified, gaps located, and invalid arguments told apart from false theorems.
---

# Proof Forensics

You are the referee, not the author. Your job is to find the first step that does not follow, or to certify that every step does. Elegance and length are not evidence.

## Workflow

1. **Freeze the claimed statement.** Write it out with every quantifier, domain, hypothesis and conclusion. Compare abstract, introduction and main theorem. If they disagree, that is finding #1 (statement drift).
2. **Build an obligation ledger.** Number each inference and give it exactly one status:
   - `Valid`: follows from earlier lines and named results whose hypotheses you checked.
   - `Valid-conditional-on-X`: follows if X holds, where X is a named, still-open obligation.
   - `Unjustified`: may be true, but no argument is given ("clearly", "standard", "by a similar argument").
   - `Invalid`: does not follow, and you can say why (wrong sign, failed hypothesis, counterexample to the step).
3. **High-risk sweep.** Check explicitly for:
   - Sign, orientation and index conventions, especially across branches, charts or summands.
   - Cancellation arguments: does the cited cancellation theorem's exact hypothesis (e.g. a count being zero) actually hold?
   - Interchanging limits, sums, integrals and derivatives (needs dominated or monotone convergence, uniformity, absolute convergence).
   - Uniformity: are constants independent of the parameters the proof later varies?
   - Quantifier order (∀ε∃δ versus ∃δ∀ε), "for some" quietly becoming "for all".
   - Edge cases: characteristic 2, dimension 0 or 1, empty set, boundary, degenerate cases.
   - Circularity: the result, or an equivalent, used through a companion paper.
   - Cited theorems: are all their hypotheses met here, in this generality?
   - Equality claimed where only an inclusion is proved (cones, closures, spans).
4. **Adversarial tests.** For every `Unjustified` or suspect step, hand a precise sub-claim to `counterexample-and-invariant-discovery`. Run small exact cases (symbolic or integer computation, not floating point) where possible.
5. **Separate the failure modes.** Is it a gap in the proof (the theorem may still be true), a false lemma (the proof is invalid, the theorem is unknown), or a false theorem (it needs a counterexample to the statement itself)? Never call a theorem false because its proof is incomplete.
6. **Propagate.** List every downstream result (same family, companion papers, citations) that relies on the broken step. Flag each one as `inherits-gap`.
7. **Repair and regression.** If you propose a fix (extra hypothesis, weaker conclusion, new lemma), re-run steps 2–3 on the repaired argument and state exactly what changed in the statement.
8. **Version discipline.** Name the version you refereed: path plus date, or commit. When a newer version exists, diff the claims, not just the prose.

## Output contract: the referee report

- Statement as frozen, with any drift noted.
- Verdict: `Correct` | `Correct-conditional-on {X}` | `Gap at step k` | `Invalid at step k` | `Statement false (counterexample attached)`.
- Ledger table: step, claim, status, justification or missing piece.
- First critical failure, with a minimal explanation (the equation, sign or hypothesis).
- Downstream impact list.
- Suggested repair, and what it costs (a stronger hypothesis or a weaker conclusion).
- Open questions for the author.

## Using the openai/math corpus

```bash
cd /workspace/openai-math
cat history.md                                   # every withdrawal and fix, with reasons
rg -il 'withdrawn' preprints --glob README.md    # withdrawal notices (3 as of 7 Oct 2026)
rg -l 'Version note' preprints --glob README.md  # revised manuscripts
ls preprints | grep -i taming                    # versions sit side by side as dated dirs
git show adc7f1241:preprints/<dir>/paper.pdf > /tmp/old.pdf   # pre-withdrawal / v1 PDF
pdftotext preprints/<dir>/paper.pdf - | less     # or read build/main.tex + build/sections/
```

Each `preprints/<Title>-<Month>-<D>-2026/` directory holds `README.md` (citation, version note or withdrawal notice), `paper.pdf` (or `manuscript.pdf`) and `build/` (LaTeX sources). Treat the newest dated directory as current and older ones as previous versions.

## Worked example 1: a sign error that kills a cancellation (real)

`preprints/Algebraicity-of-Weil-classes-on-split-abelian-eightfolds-September-18-2026/README.md`, withdrawn 6 Oct 2026.

- Step: with $I(f_1)=-m$, insert $m$ reverse stabilization traces, each claimed to have sign $+1$, so the signed double-point count becomes $0$.
- High-risk check (orientation across branches): the two branches of the standard cusp have opposite source orientations, so each trace has sign $-1$. Then $I_{new}=-m-m=-2m\neq0$.
- Cited theorem check: Eliashberg–Murphy cancellation requires a zero signed count. Its hypothesis fails, so the step is **Invalid**.
- Propagation: `Algebraicity-of-Kuga-Satake-Correspondences-for-K3-Surfaces-October-3-2026` and `The-rational-Hodge-conjecture-for-products-of-K3-surfaces-October-4-2026` adapt the same construction, so they are `inherits-gap` and were withdrawn too.
- Correct classification: the proof is invalid and the statement is **unknown**, not false. The notice says exactly that.

## Worked example 2: an equality that was only an inclusion (real)

`Taming-implies-compatibility-on-four-manifolds` exists as `-September-23-2026` and `-October-6-2026`. The version note says the revision "restricts the cone-sum equality to $h_J^-=b_2^+-1$, and adds a four-torus example of strict inclusion". Forensic lesson: a claimed set equality was true only under an extra numerical condition. The repair weakened the statement and added a counterexample to the general equality. Downstream, `Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples` dropped its now-unneeded cone-comparison dependency.

## Never

- Accept "standard", "similarly" or "it is easy to see" as `Valid`.
- Referee your own construction in the same pass.
- Treat a Lean file as covering the whole paper (check `lean/docs/NNN.md` scope).
