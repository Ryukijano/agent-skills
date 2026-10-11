---
name: counterexample-and-invariant-discovery
description: Use when you need to test whether a claim or proof step is actually true, find which hypotheses do real work, or produce a minimal, exactly verified counterexample or a proved invariant.
---

# Counterexample and Invariant Discovery

The goal is the structure of a claim: which hypotheses matter, where it breaks, and what is preserved. A counterexample only counts if it is minimal and checked in exact arithmetic.

## Workflow

1. **Normalise the claim.** Write it as `∀ x ∈ D, H1(x) ∧ … ∧ Hk(x) → C(x)`. Identify the target: the theorem, a lemma, or one proof step. (A counterexample to a step refutes the proof, not the theorem.)
2. **Hypothesis-removal matrix.** For each Hi, drop it and look for a counterexample, then weaken it (strict→non-strict, compact→closed, finite→countable, char 0→char p). Record a table: Hi, its status when dropped (`needed`, with the witness | `redundant`, with a proof | `unknown`).
3. **Domain-specific search heuristics.**
   - Algebra: small fields (𝔽2, 𝔽3), char 2 specifically, non-commutative or non-reduced rings, group algebras of torsion groups, matrices of size 2–3.
   - Combinatorics and graphs: exhaustive search on n ≤ 8–10 vertices, extremal and Turán-type constructions, random constructions with a fixed seed, SAT or ILP encodings.
   - Analysis: functions that are oscillatory, unbounded or non-uniform; sequences that defeat interchange (moving bumps); boundary and endpoint cases.
   - Geometry and topology: low dimension, non-orientable, singular or degenerate configurations, tori (the four-torus in the Taming revision).
   - Number theory: small primes, p = 2, squares, Liouville-type numbers.
   - Probability: heavy tails, dependence, degenerate distributions.
4. **Invariants.** When a search finds nothing, look for the quantity the hypotheses preserve (a sign, parity, degree, energy, rank, index, monovariant). State it and prove it. A proved invariant is a lemma for `proof-construction-lab`.
5. **Minimise and verify exactly.** Shrink the witness (fewer elements, smaller field, lower degree). Verify it with exact arithmetic (integers, rationals, finite fields, symbolic CAS), never floats alone. Give a check script and its output.
6. **Classify the result.** `counterexample-to-theorem` | `counterexample-to-step k` (the theorem may survive) | `counterexample-to-converse` | `hypothesis Hi shown necessary` | `invariant proved`.

## Output contract

The normalised claim; the hypothesis matrix; each witness with its exact verification script and output; any invariants with proofs; a classification; and a handoff (repair goes to the constructor, a formalizable witness goes to `lean-proof-bridge`, which is ideal for concrete counterexamples).

## Using the openai/math corpus

```bash
cd /workspace/openai-math
ls preprints | grep -i counterexample          # 38 counterexample manuscripts (incl. versions)
ls lean/ComparatorChallenges | grep -i -E 'counter|kaplansky'
cat lean/docs/197.md                             # scope note for the Kaplansky family
```

Counterexample results are the best targets for formal verification: an existential statement with an explicit witness.

## Worked example 1: a famous conjecture fails in characteristic 2 (real)

Family 197: `preprints/A-Counterexample-to-Kaplanskys-Direct-Finiteness-Conjecture-in-Characteristic-Two-September-23-2026/`. Reasoning summary: `reasoning_traces/kaplansky-direct-finiteness-characteristic-two.pdf`. Lean challenge: `lean/ComparatorChallenges/KaplanskyDirectFiniteness.lean`:

```lean
def MainClaim : Prop :=
  ∃ (K : Type) (_ : Field K) (_ : Fintype K) (_ : CharP K 2),
    ∃ (G : Type) (_ : Group G) (_ : Group.FG G),
      ∃ a b : MonoidAlgebra K G, a * b = 1 ∧ b * a ≠ 1
```

Lessons: (a) the heuristic "try char 2 and finite fields first" was the winning one; (b) the odd-characteristic sequel uses a field of order $p^4$, where p is the smallest prime factor of $(\binom{1200}{600}!)^2+1$. That witness is explicit but not small, so "minimal" means minimal in structure, not in numbers; (c) the formal statement is weaker than the paper's: nonsoficity is outside it (`lean/docs/197.md`).

## Worked example 2: counterexample to a general equality (real)

The Taming revision (`Taming-implies-compatibility-on-four-manifolds-October-6-2026/README.md`) "adds a four-torus example of strict inclusion" and restricts the cone equality to $h_J^-=b_2^+-1$. That is a hypothesis-removal matrix in action: without the numerical condition, the equality fails on T⁴.
