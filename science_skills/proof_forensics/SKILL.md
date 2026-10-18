---
name: proof-forensics
description: >-
  Act as an independent referee for a mathematical proof or manuscript: check
  whether the conclusion follows from the stated assumptions, locate the
  earliest invalid or unjustified step, test critical inferences adversarially,
  and assess downstream impact of any repair. Use when asked to check, audit,
  referee, or find the gap in a proof, or to review a manuscript before relying
  on it. Follows math-rigor-standard.
---

# Proof Forensics

Mission: determine whether the conclusion follows from the stated assumptions.
Do not judge whether the proof sounds plausible. Assume the argument may contain
a fatal gap until each critical step has been checked.

Read `../math_rigor_standard/SKILL.md` first. Its verdict classes and
provenance rules apply.

## Protocol

### A. Statement integrity

- Rewrite the exact theorem being checked, including quantifiers, domains,
  regularity, dimension, characteristic, finiteness and boundary conditions.
- List every assumption imported from an earlier result, and check that each
  one is stated in the form the earlier result actually proves.
- Separate the intended theorem from stronger claims made in the prose or
  abstract. A proof of the intended theorem does not support the stronger
  claim.

### B. Step-by-step obligation tracking

For each step in the proof, record:

1. The premises the step uses.
2. The inference being drawn.
3. The definition or theorem that justifies the inference.
4. The hypotheses that justification requires.
5. Whether those hypotheses were established earlier in the text.

Assign each step one verdict:

- `Valid`: justified by the stated premises.
- `Valid-conditional-on(X)`: depends on an explicit missing or external
  assumption X.
- `Unjustified`: the conclusion may be true, but this argument does not
  establish it.
- `Invalid`: a concrete logical or mathematical error is present, shown by a
  specific computation or counterexample.

Only `Invalid` steps are errors in the argument. An `Unjustified` step is a
gap to fill, not a disproof.

### C. High-risk checks

Check the items that apply to the subject. Do not impose conditions that are
irrelevant to the problem.

- Sign, index, dimension and normalization errors.
- Cancellation of terms that depend on the limiting parameter.
- Division by a quantity that could be zero, or an unproved invertibility.
- Interchange of limits, derivatives, integrals or infinite sums.
- Compactness or convergence invoked without its hypotheses.
- Pointwise convergence used where uniform convergence is needed.
- Independence, conditional expectation, or almost-sure statements used
  without the required assumptions.
- Missing measurability, integrability or boundedness conditions.
- Circularity: the desired conclusion, or something that depends on it, is used
  in its own proof.
- Reductions or equivalences that hold in only one direction.

### D. Adversarial testing

Try to invalidate each critical inference:

- Test minimal and degenerate cases.
- Test equality and boundary cases.
- Construct an example that violates one hypothesis at a time.
- Decide whether a counterexample refutes the theorem or only the chosen proof
  strategy. Only the first changes the status of the statement.
- Computation may suggest failures. The failure is confirmed only by an exact
  argument, which `counterexample-invariant-discovery` produces.

### E. Repair and regression

When an error is found:

1. Identify the earliest invalid step.
2. Explain the mathematical reason it fails.
3. Determine which later steps depend on it.
4. Propose the weakest plausible repair, and state it as a changed hypothesis or
   a new lemma.
5. Recheck the repaired argument from the beginning, not just the repaired step.
6. List companion results that rely on the same faulty lemma.

Never patch a proof silently and report the original as valid. A repaired
proof is a new version that needs its own review.

### F. Revision and companion comparison

If several versions of a manuscript or companion papers exist, compare them.
Record every change to hypotheses, lemmas, dependencies and conclusions. Where
the versions differ, the newer one is the one to check; the older one is
evidence only of what was previously claimed.

## Limits of this review

- Never claim a theorem is false because its current proof is incomplete.
- Never report a manuscript as established because it has many companion
  papers or appears in a large catalogue. Count is not correctness.
- If a citation is used, check it: the cited statement, its hypotheses, and the
  source. A citation that was not checked goes in the remaining-unverified list.

## Deliverable: referee report

```
Verdict:            <one label from math-rigor-standard, with scope>
Statement checked:  <exact theorem>
Step audit:         <table: step | premises | inference | justification | hypotheses | verdict>
Critical failure:   <earliest Invalid or Unjustified step, or "none found">
Counterexample:     <explicit object, or "none constructed">
Repair options:     <weakest changed hypothesis or new lemma, with reason>
Downstream impact:  <results that depend on the failing step>
Unverified:         <citations, external theorems, and steps not checked>
```
