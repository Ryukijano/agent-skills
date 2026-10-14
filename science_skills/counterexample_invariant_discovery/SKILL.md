---
name: counterexample-invariant-discovery
description: >-
  Turn uncertainty about a mathematical claim into a structured search for
  either a proof strategy or an obstruction. Use when testing a conjecture,
  searching for counterexamples, finding which hypotheses are necessary,
  discovering invariants or monotone quantities, or deciding whether a finite
  computation supports a universal claim. Follows math-rigor-standard.
---

# Counterexample and Invariant Discovery

Objective: decide whether a claim has a proof strategy, a counterexample, or an
identifiable missing hypothesis. Computation is used to search and to suggest.
Exact mathematics establishes the final result.

Read `../math_rigor_standard/SKILL.md` first.

## Phase 1: Normalize the claim

Rewrite the claim symbolically. Record what kind of statement it is:

- universal property
- existence of an object
- uniqueness or classification
- inequality or bound
- convergence or asymptotic statement
- equivalence or reduction

Identify the smallest admissible instances. These are the first cases to
check by hand.

## Phase 2: Hypothesis-removal matrix

For each hypothesis H_i:

1. State the role H_i plays in the intended proof, if one exists.
2. Form the theorem with H_i removed or weakened.
3. Search for an object satisfying the other hypotheses but violating the
   conclusion.
4. If the search finds one, verify it exactly (Phase 5). If not, record
   "no example found in search space S". This is an open search, not evidence
   that H_i is necessary.

## Phase 3: Search strategy

Choose a representation suited to the domain:

- Finite combinatorics: enumerate small graphs, sets, configurations or
  incidence structures. Use canonical forms to avoid duplicates.
- Linear algebra: inspect rank deficiency, nullspaces, repeated eigenvalues,
  singular and degenerate matrices.
- Analysis: examine endpoints, discontinuities, non-uniform convergence and
  extreme scales.
- Algebra: test zero divisors, units, characteristic dependence, degenerate
  structures.
- Probability: test dependence, rare events, heavy tails, failure of
  integrability.
- Geometry: inspect symmetry, degenerate configurations, dimension thresholds,
  boundary cases.
- Optimization: examine feasibility boundaries, duality gaps, non-attainment.

Computation rules:

- Use exact arithmetic for anything that will be reported: `fractions.Fraction`,
  integer arithmetic, or a computer algebra system with exact rationals. Floats
  are used only to rank candidates. Never report a float-based result as exact.
- Record the search space, the enumeration method, and the seed or ordering, so
  the search can be repeated.
- A search that finds nothing proves nothing about the unrestricted statement.

## Phase 4: Discover invariants

Look for quantities preserved or constrained by the relevant transformations:

- rank, dimension, parity, cardinality
- energy, norm, entropy, conserved quantities
- monotone functions and order relations
- symmetry classes and equivalence classes
- topological or algebraic obstructions
- potential functions that decrease along an iterative process

For each candidate invariant, state its domain and prove the preservation or
monotonicity property. A property that held in every test case is a candidate
until proved.

## Phase 5: Turn observations into mathematics

When a computation flags a suspicious case:

1. Minimize the example.
2. Write its exact mathematical description.
3. Verify every hypothesis, exactly.
4. Compute the claimed conclusion exactly.
5. Identify which inference or assumption fails.
6. Decide whether it counterexamples the theorem or only one proof strategy.

Report the verified counterexample as `COUNTEREXAMPLE(verified)` only after
steps 3 and 4 are done by hand or by exact computation that is included in the
output.

## Phase 6: Turn failure into a new strategy

When a conjecture survives testing:

- identify the structural feature shared by all tested cases
- propose a lemma that explains that feature
- look for a proof by induction, an extremal choice, decomposition, compactness
  or a suitable invariant
- state precisely what remains unproved

## Limits

- A finite search can disprove a universal statement if it finds a valid
  counterexample.
- A finite search cannot establish an unrestricted universal statement unless
  an independent argument covers the whole domain.
- Small-case agreement is `NUMERICALLY-SUPPORTED` at most.

## Output contract

```
Claim and hypotheses:  <symbolic statement>
Search space and method: <domain, enumeration, exactness, seed>
Minimal candidates:    <smallest instances checked, with results>
Exact verification:    <hand or exact computation for each reported case>
Necessary hypotheses:  <only those shown necessary by a verified example>
Candidate invariants:  <statement, domain, status of its proof>
Revised conjecture:    <lemma or corrected statement>
Next obligation:       <single concrete next step>
```
