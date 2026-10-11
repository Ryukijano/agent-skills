---
name: theorem-family-cartographer
description: Use when you need a typed, versioned map of how a set of theorems relate (dependencies, generalizations, alternative proofs, corrections), to plan study or research or to trace how an error propagates.
---

# Theorem Family Cartographer

Build a graph in which every edge has a defined logical meaning and a piece of evidence. Thematic similarity is not a dependency.

## Workflow

1. Identify the central theorem and its exact version (dated path or commit).
2. Gather related manuscripts, companion results, formalizations and reasoning summaries.
3. Extract each node's definitions, hypotheses, key lemmas and conclusion.
4. Classify edges, each with a quote or line reference as evidence:
   - `depends-on` (uses as a lemma)
   - `stronger-than` / `weaker-than`
   - `special-case-of` / `generalizes`
   - `alternative-proof-of`
   - `corollary-of` / `application-of`
   - `conjectural-link` (explicitly unproven)
   - `supersedes` (version) / `withdrawn-by`
5. Read the history: revisions, corrections, withdrawals. Mark nodes `inherits-gap` along `depends-on` edges from any broken node.
6. Compare proof architectures across `alternative-proof-of` edges. Which key lemma makes the difference?
7. Find shared proof obligations and reusable formal lemmas (the same Mathlib or `OAI/` file used by several nodes).
8. Rank what to study next: high fan-out, formally verified, robust under revision.

## Node schema (YAML)

```yaml
- id: F017-pi-exponent
  statement: "irrationality exponent of π equals 2"
  hypotheses: []
  source: preprints/The-irrationality-exponent-of-pi-is-2-September-24-2026/paper.pdf
  version: "2026-09-24 @ fd4aeeb2e"
  strategy: "<one line>"
  formalization: {status: formalized, challenge: lean/ComparatorChallenges/PiExponent.lean, scope: lean/docs/017.md, outside_scope: ["Flint–Hills consequence"]}
  depends_on: []
  corrections: []
  open_obligations: []
```

## Deliverable

The node list and typed edge list (YAML, plus a Mermaid diagram), a comparison of proof architectures, a dependency audit (`inherits-gap` and version-stale citations), and a ranked study list.

Never infer correctness from the number of companion manuscripts or a node's centrality.

## Using the openai/math corpus

```bash
cd /workspace/openai-math
less CONTENTS.md                     # "**NNN. Title.** description" then member manuscripts + abstracts
grep -n '^\*\*[0-9]\{3\}\.' CONTENTS.md | wc -l   # family headers
grep -n 'result 032' CONTENTS.md     # cross-family references are written as "result NNN"
cat lean/docs/NNN.md                 # formal scope for family NNN (lists every linked paper)
cat history.md                       # supersedes / withdrawn-by edges
ls preprints | grep -i '<keyword>'   # all versions of a title (dated dirs)
```

## Worked example: a dependency removed by a revision (real)

- `Taming-implies-compatibility-on-four-manifolds` (Sep-23 → Oct-6). The Oct-6 version note narrows a cone equality to $h_J^-=b_2^+-1$ and adds a four-torus strict inclusion: a `supersedes` edge, with the statement weakened.
- `Deforming-hypersymplectic-four-manifolds-to-hyperkahler-triples` (Sep-23 → Oct-7). Its version note "removes an unnecessary cone-comparison citation", so the old `depends-on` edge to Taming becomes a plain citation. Lesson: a correction upstream did not create an `inherits-gap` downstream because the edge was cut. Check this from both version notes, not from title similarity.
- Family 001 (Milne's rationality) cites "result 032": add a `depends-on`/`corollary` edge only after reading the exact usage.

Second example: family 197 (Kaplansky). `lean/docs/197.md` links three papers: char 2, the group-ring determinant counterexample, and odd characteristic. Classify the edges (is odd characteristic a `generalizes` or an `alternative` construction?) and record that the formal statements are weaker than the papers (nonsoficity and the spectral-measure integral are outside scope).
