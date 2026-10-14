---
name: math-rigor-standard
description: >-
  Shared standard for all mathematical research skills (proof construction,
  proof forensics, counterexample search, Lean formalization, theorem
  cartography). Defines the status vocabulary, the provenance rules for
  manuscripts from openai/math, and the rule that a proof-producing agent
  never certifies its own work. Load alongside any math-* skill.
---

# Math Rigor Standard

This is the reference the other math skills point to. It is not a workflow on
its own. Every mathematical claim produced or audited under these skills must
carry one of the statuses below.

## Status vocabulary

Use these exact labels. Do not invent intermediate ones such as "mostly proved".

| Label | Meaning |
|---|---|
| `PROVED` | Every nontrivial step is justified from stated premises, with each cited result's hypotheses checked. |
| `PROVED-CONDITIONAL(X)` | Proof is valid assuming X, where X is named explicitly (an external theorem, an unproved lemma, a stronger hypothesis). |
| `FORMALIZED(scope)` | A Lean artifact compiles and the scope of the formal statement is stated. Never shortened to "formalized" alone. |
| `NUMERICALLY-SUPPORTED` | Computation agrees with the claim on the tested cases. Says nothing about the unrestricted statement. |
| `COUNTEREXAMPLE(verified)` | An explicit object violates the claim, and every hypothesis and the failing conclusion were checked exactly. |
| `UNRESOLVED(obligation)` | The precise missing lemma or step is named. |
| `UNVERIFIED-MANUSCRIPT` | A claim taken from a source document that has not been checked under these skills. |

Verdicts for individual proof steps (used by `proof-forensics`):
`Valid`, `Valid-conditional-on(X)`, `Unjustified`, `Invalid`.

An `Unjustified` step does not mean the conclusion is false. Only `Invalid`
steps, or a verified counterexample to the statement, show the claim fails.

## Non-negotiable rules

1. **Separate the statement from the proof.** A correct-looking proof of a
   misstated theorem proves nothing about the intended theorem.
2. **No self-certification.** The agent that constructs a proof must not be the
   only one to declare it complete. Hand the result to `proof-forensics` or an
   independent check, and record that it happened.
3. **Numerical evidence is not proof.** Finite checks, floating-point runs and
   plots support conjectures; they do not establish universal statements.
4. **Never silently strengthen or weaken a hypothesis.** If the argument needs
   a stronger hypothesis, label the result `PROVED-CONDITIONAL`.
5. **Compilation is not faithfulness.** A Lean file that builds may still
   formalize a weaker or different statement. See `lean-proof-bridge`.
6. **Relationship is not dependency.** Thematic similarity between results is
   not a logical edge. See `theorem-family-cartographer`.
7. **Say what was not checked.** Every output ends with unresolved obligations,
   even when they are empty.

## Provenance rules for openai/math manuscripts

The repository at `github.com/openai/math` is a collection of research
artifacts. Its README states that they were produced by an internal OpenAI
model, that not every result has been formally verified, and that some
unformalized results may contain issues. Verified facts about the repository:

- 719 manuscripts in 372 families (README).
- About 42% of top-line results formalized (README); Lean library in `lean/`.
- Reasoning summaries exist for 10 families (README table), in
  `reasoning_traces/` mostly as PDFs, with at least one `.tex` source
  (`mezard-parisi-formula.tex`), covering subjects such as the irrationality exponent of
  pi, Mahler conjectures, free group factor isomorphism, Kaplansky's
  direct-finiteness problem in characteristic two, the Mezard-Parisi formula, and
  the relativistic Vlasov-Maxwell system.
- The README says corrections and revisions will be recorded as new versions.

Rules for using these materials:

- Treat every manuscript as `UNVERIFIED-MANUSCRIPT` until audited.
- Do not cite a specific correction, sign error or withdrawn result from the
  repository unless you have read that exact entry. The repo's `history.md`
  could not be retrieved during the review that produced this skill (HTTP 503),
  so the specific correction examples in older drafts are unconfirmed.
- Do not treat the number of companion manuscripts in a family as evidence of
  correctness.
- Reasoning summaries show a proof strategy the model chose. They are not
  authoritative justification of the result.

## Output header

Start every proof, audit or search report with:

```
Claim:        <exact statement, quantifiers and hypotheses>
Status:       <one label from the vocabulary>
Source:       <user input | manuscript path + version | own derivation>
Verification: <what was checked, by what method, and what was not>
```
