---
name: proof-construction-lab
description: Use when you must produce a rigorous proof of a precise mathematical statement, with explicit lemmas, checked hypotheses and every remaining gap isolated, rather than a persuasive explanation.
---

# Proof Construction Lab

Optimise for a correct argument with explicit dependencies, not for a convincing story. Your output always goes to `proof-forensics`, run as a separate pass.

## Workflow

1. **Freeze the statement.** Spell out every quantifier, domain, hypothesis and conclusion, plus the conventions (signs, normalisations, characteristic, which category or topology). Record which hypotheses you expect each part of the proof to use.
2. **Sanity-check before proving.** Test small or degenerate cases exactly, and look for a quick counterexample (`counterexample-and-invariant-discovery`). If the statement fails, stop and report.
3. **Dependency graph.** List the known results you might use, each with its exact hypotheses. Mark which ones are standard (with a reference) and which are new obligations.
4. **Strategy search.** Write 2–4 candidate routes (direct, contradiction, induction or descent, compactness, extremal choice, transfer or invariance, a construction, reduction to a known case, probabilistic). For each, name the one step most likely to fail. Pick the route whose hardest step is the best understood.
5. **Skeleton.** Theorem ⇐ Lemmas L1…Ln, with each lemma's statement frozen to the same standard as the theorem. Mark each lemma `known` (with a citation), `routine` or `core`.
6. **Prove every bridge.** Write each lemma's proof in full. Cover each limit interchange, uniform constant and edge case explicitly.
7. **Self-challenge.** For each step ask: which hypothesis is used here? Is the cited theorem's hypothesis actually met? Would the step survive in characteristic 2, dimension 1, or on the boundary? Delete any hypothesis and find where the proof breaks. If it never breaks, either the hypothesis is redundant or the proof is wrong.
8. **Isolate what's missing.** If one step resists, state it as a precise standalone lemma and deliver a conditional theorem: `Theorem (conditional on Lemma X)`.

## Invariants

- Never silently strengthen hypotheses or weaken conclusions. Any change goes in a "Statement changes" section.
- Never swap a limit, sum, integral or derivative without naming the justification.
- Numerics are not proof. They can guide you or refute a claim, never certify one.
- Check every hypothesis of every cited theorem, in this generality.
- Label conditional results as conditional, everywhere they are used.
- Track sign and orientation conventions in one place and cite them on every use.

## Output contract

1. Frozen statement, plus any statement changes.
2. Strategy chosen, and why the others were rejected.
3. Dependency list: known results with exact hypotheses.
4. Lemmas with full proofs; the main proof assembled from them.
5. Hypothesis-usage table: each hypothesis and the step(s) that use it.
6. Open obligations, if any, and the conditional status.
7. Handoff: "send to proof-forensics", and suggest `lean-proof-bridge` if the statement can be formalized.

## Using the openai/math corpus

Use it to study proof architecture, not to copy proofs.

```bash
cd /workspace/openai-math
less CONTENTS.md                    # 372 families: each result + its manuscripts + abstracts
ls preprints/<dir>/build/sections   # LaTeX source split by section: read the skeleton
ls reasoning_traces/                # 10 abridged reasoning summaries (PDF; one .tex)
pdftotext reasoning_traces/irrationality-exponent-of-pi.pdf - | less
```

Reasoning summaries (families 007, 017, 087, 102, 159, 197, 221, 271, 287, 362) show strategy search in practice: abandoned routes, the lemma that unlocked the problem. Read them for step 4.

## Worked example: skeleton reading (real)

Family 017, `preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/`, formal scope in `lean/docs/017.md`.

- Frozen statement (from the Lean scope note): for every $\nu>2$, all sufficiently large $q$ satisfy $|\pi-p/q|\ge q^{-\nu}$ for every integer $p$, plus the supremum characterization.
- Exercise: read `build/main.tex` and the sections, extract the lemma skeleton (L1…Ln), and mark each lemma known, routine or core. Compare with `reasoning_traces/irrationality-exponent-of-pi.pdf` to see which routes were tried first. Note that the Flint–Hills consequence is outside the formal statement, so it stays a separate, unverified obligation.

## Counter-example to imitate: how not to construct

The withdrawn Weil-classes paper (see `proof-forensics`) built a long construction on one unchecked sign. Invariant violated: a cited theorem's hypothesis (zero signed count) was never re-checked after the construction step.
