---
name: theorem-family-cartographer
description: >-
  Build an evidenced map of how mathematical results relate: direct
  dependencies, stronger or weaker statements, special cases, alternative
  proofs, corollaries, and conjectural connections. Use when studying a body of
  results, comparing proof architectures across manuscripts or families, or
  building a theorem graph from a collection such as openai/math. Thematic
  similarity is never recorded as a logical edge. Follows math-rigor-standard.
---

# Theorem Family Cartographer

Objective: a reliable map of how results relate, where every edge has a
defined meaning and cited evidence. A family of related papers is a starting
point for the map, not a claim that its members depend on one another.

Read `../math_rigor_standard/SKILL.md` first.

## Edge types

Each edge must carry exactly one type. If none fits, the edge is not recorded.

| Edge | Meaning | Evidence required |
|---|---|---|
| `depends-on` | Proof of A uses B as a stated input. | The line or step in A where B is used. |
| `stronger-than` / `weaker-than` | A implies B (or the reverse) as a statement. | The implication, with proof or a checked reference. |
| `special-case-of` / `generalizes` | A is B with extra hypotheses or specialized objects. | Explicit specialization. |
| `alternative-proof-of` | A and B prove the same statement by different routes. | Both statements matched exactly, including hypotheses. |
| `corollary-of` / `application-of` | A follows from B with a short argument. | The argument. |
| `conjectural-connection` | A plausibly relates to B, not established. | Stated as conjecture; status `UNRESOLVED`. |

Thematic similarity, shared keywords, the same discipline label, and membership
in the same family are not edges. A family is a grouping only.

## Procedure

1. **Fix the central theorem.** Record its exact version: the manuscript, the
   version or commit, and the statement with all hypotheses.
2. **Gather material.** Retrieve related manuscripts, companion results and
   available formalizations. For openai/math, the manuscript map and the
   per-manuscript `preprints/` directory are the sources. Do not take a
   manuscript's family or citation list as proof that a relation holds.
3. **Extract structure.** For each result, record definitions, hypotheses,
   lemmas used, and conclusions.
4. **Classify relationships** using the edge table above, with evidence for each.
5. **Compare proof architectures.** For results with the same conclusion, list
   the main lemmas each proof relies on, and identify the lemma responsible for
   any difference in method or hypotheses.
6. **Check revision history.** Look for recorded corrections, revisions or
   withdrawals of each node. The openai/math README says corrections are
   recorded as new versions with old versions kept. The specific history file
   could not be retrieved during the review that produced this skill, so do not
   report specific corrections until the history has been read.
7. **Identify shared obligations.** Note any unproved lemma that several nodes
   rely on, and any formal lemma that could be reused (see
   `lean-proof-bridge`).

## Node record

Each node in the graph contains:

- statement and domain
- hypotheses
- source and version
- proof strategy
- formalization status, as `FORMALIZED(scope)` or `NOT FORMALIZED`
- dependencies (with edge type and evidence)
- known counterexamples or corrections (with source)
- open obligations

Missing fields are written as `UNKNOWN`, not left blank.

## Using a family structure

When a family in a collection is large, check whether its members are:

- a principal result with companions
- consequences of the principal result
- alternative proofs of the same statement

Only the last category is a direct comparison of proofs. The others are
dependency questions, to be answered from the text.

## Ranking what to study next

When asked which concepts are most useful to study, rank by the number of
verified dependency edges into the concept, weighted by how many distinct
nodes rely on it, and flag concepts whose proofs are unverified. A high count
of incoming edges that have not been checked is not a reason to prioritize.

## Output contract

1. Theorem-family graph: nodes and typed, evidenced edges.
2. Comparison of proof architectures, with the responsible lemmas.
3. Dependency audit: every unchecked edge and every `UNKNOWN` field.
4. Shared obligations and reusable formal lemmas.
5. Ranked list of concepts to study next, with the ranking basis stated.
