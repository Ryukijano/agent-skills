---
name: proof-construction-lab
description: >-
  Construct a mathematical proof with explicit dependencies, sufficient
  hypotheses, and independently checkable steps. Use when asked to prove a
  theorem or lemma, find a proof strategy, build a proof skeleton, or turn an
  idea into a rigorous argument. Hands off to proof-forensics for review and
  to lean-proof-bridge for formalization. Follows math-rigor-standard.
---

# Proof Construction Lab

Goal: a proof whose logical dependencies are explicit, whose hypotheses are
sufficient, and whose critical steps can be checked one by one. Optimize for a
correct argument, not a convincing one.

Read `../math_rigor_standard/SKILL.md` first. Its status labels and
non-negotiable rules apply here.

## Workflow

### 1. Freeze the statement

- Write the theorem with every quantifier, domain, hypothesis and conclusion.
- Classify it: universal, existential, uniqueness or classification,
  asymptotic, probabilistic, equivalence or reduction, or conditional.
- Separate three kinds of input: established results, cited but unverified
  results, and the conjecture itself.
- If the statement is ambiguous, list the candidate readings and pick one
  explicitly. Do not silently choose the easiest one.

### 2. Build the dependency graph

- Unpack every definition the proof needs.
- List candidate lemmas and known results. For each one, record the exact
  hypotheses it requires.
- Mark which hypotheses are essential and which might be removable. A hypothesis
  is only marked removable after `counterexample-invariant-discovery` or a
  direct argument supports that.

### 3. Choose a proof architecture

Pick strategies that fit the setting. Name the choice and the reason for it.

| Strategy | Use when |
|---|---|
| Direct construction or derivation | The conclusion is an explicit object or formula. |
| Contradiction or contrapositive | The negation gives extra structure to exploit. |
| Induction, well-founded induction, minimal counterexample | A parameter decreases or the objects are built recursively. |
| Compactness, limiting argument, approximation | Existence follows from finite approximations or a limit of solutions. |
| Invariant, monotonicity, extremal argument | A quantity is preserved or optimized. |
| Reduction or equivalence | The problem maps to a known solved case. |
| Duality, decomposition, classification | Structure theory applies. |
| Probabilistic or analytic method | Used only when its own hypotheses (measurability, integrability, independence) are verified. |

Record at least one rejected strategy and why it fails. This is the cheapest
way to avoid circular reasoning.

### 4. Write the skeleton

Use the chain form:

```
Theorem  <- Lemma A (inputs: H1, H2; supplies: X)
         <- Lemma B (inputs: X, H3; supplies: Y)
         <- Final implication (uses Y and the conclusion)
```

For each lemma, state its inputs and the exact statement it supplies. Each
arrow is a claim that still needs its own proof.

### 5. Prove every bridge

For each inference, state why the previous statement implies the next one.

- Expand every non-trivial application of a definition.
- For each cited theorem, write out its hypotheses and show they hold in the
  current setting.
- Check boundary cases: empty sets, zero, equality conditions, degenerate
  objects, and the smallest admissible instance.

### 6. Challenge the construction

Before presenting the result, try to break it:

- Test small and limiting cases by hand. Use computation only to find cases
  worth checking; the proof itself must be exact.
- Remove one hypothesis at a time and see which step fails.
- Hand the complete argument to `proof-forensics`. Do not mark the proof
  finished until that review has been run or it is listed as an open obligation.

### 7. Present the result

Use the output contract below.

## Mandatory invariants

- Never silently strengthen a hypothesis.
- Never infer existence from a construction that does not establish existence.
- Never infer uniqueness from existence.
- Never exchange limits, integrals, sums or derivatives without justification.
- Never treat numerical evidence as a proof of a universal statement.
- Never cite a theorem without checking that its hypotheses apply.
- Label every conditional result `PROVED-CONDITIONAL(X)`.
- If a proof cannot be completed, name the precise missing lemma. Do not
  write "it follows that" over a gap.

## Using repository manuscripts

When a manuscript from `openai/math` is the starting point, treat its argument
as `UNVERIFIED-MANUSCRIPT`. Use it for the proof strategy and the list of
lemmas, but re-derive each bridge yourself. Reasoning summaries are the
model's chosen route, not a justification. Do not claim a result was verified
because a manuscript exists for it.

## Output contract

1. Formal theorem statement, with the status label.
2. Strategy and rationale, including rejected strategies.
3. Dependency graph (lemmas, inputs, outputs).
4. Complete proof, with every bridge written out.
5. Verification of critical steps and the boundary cases checked.
6. Failure modes and remaining gaps, each as `UNRESOLVED(obligation)`.
7. Optional: a Lean formalization plan for `lean-proof-bridge`.

A proof is complete only when every nontrivial obligation is discharged, or
when each remaining one is named as unresolved in the output.
