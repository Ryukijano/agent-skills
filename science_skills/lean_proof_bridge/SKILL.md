---
name: lean-proof-bridge
description: >-
  Connect an informal mathematical claim to a Lean 4 formalization and check
  what is actually proved. Use when formalizing a theorem, auditing a Lean
  development for sorry, custom axioms or weakened statements, mapping
  informal proof steps to Lean lemmas, or working with the openai/math Lean
  library. Distinguishes successful compilation from a faithful formalization.
  Follows math-rigor-standard.
---

# Lean Proof Bridge

Mission: establish a reliable correspondence between the intended mathematical
claim and the proposition Lean accepts. Compilation is evidence that Lean
accepted an artifact. It is not evidence that the artifact states the intended
theorem.

Read `../math_rigor_standard/SKILL.md` first.

## Environment check (do this first)

Lean may not be installed. Check before claiming anything compiled:

```bash
command -v lean lake elan || echo "no Lean toolchain on PATH"
```

If no toolchain is present, run in **design-only mode**. Report every
compilation step as `NOT RUN`, never as passed. Installing a toolchain (elan
into the user's HOME, which is quota-limited) is a decision for the user.

For a Lake project such as the openai/math `lean/` directory, read its
`lean-toolchain` file for the version to install, and its README for build
instructions. Two notes from that README: compile small portions rather than
the whole library, and if the full build fails with a memory-map error, the
README suggests building with `-DMMAP=OFF` and setting
`GLIBC_TUNABLES=glibc.malloc.mmap_max=0:glibc.malloc.arena_max=1`.

## Stage 1: Statement translation

Before any tactic:

1. Define the mathematical objects and their Lean types.
2. Encode quantifiers, hypotheses and the conclusion explicitly.
3. Check that the chosen types model the intended domain. Is `ℕ` meant, or
   `ℝ`? Is a finite-dimensional space being replaced by an arbitrary module?
4. Identify implicit coercions, typeclass instances and notation that could
   change the meaning.
5. Compare the formal proposition with the informal theorem in both directions:
   does every formal instance match an informal one, and vice versa?

Do not simplify the proposition to make it easier to prove. If the formal
statement is weaker, say so and label the result `FORMALIZED(weaker: <what>)`.

## Stage 2: Dependency mapping

Break the theorem into lemmas with small, meaningful interfaces. For each lemma:

- its mathematical purpose
- its Lean type
- its dependencies, classified as axiom, library theorem, project definition,
  or newly proved result
- whether an existing library result already supplies it (check the exact
  statement and hypotheses, not the name)

## Stage 3: Proof development

1. Define helper objects and lemmas.
2. Prove local algebraic or logical steps.
3. Assemble the main argument.
4. Compile the smallest relevant module.
5. Return to the informal proof whenever formalization shows a missing
   condition. A proof that needs an extra hypothesis is a different theorem.

Use tactics to discharge justified obligations, not to hide unresolved
mathematics. A `sorry` is an open obligation and must be reported as one.

## Stage 4: Trust and verification audit

For the declaration you intend to report, inspect:

- **Sorry**: search the file and its imports. Any `sorry`, `admit`, or
  `sorryAx` dependency means the result is incomplete.
- **Axioms**: run `#print axioms <declaration>` in Lean. The output should
  show only the standard axioms. Anything else (for example a custom axiom)
  is an extra assumption.
- **Auxiliary assumptions**: check for hypotheses added to the statement that
  the informal theorem does not have.
- **Environment**: record the Lean version, the Mathlib or library revision, and
  the build command.

Grep helpers that work without a toolchain:

```bash
grep -rnE '\b(sorry|admit)\b' <dir> --include='*.lean'
grep -rnE '^\s*axiom\b' <dir> --include='*.lean'
```

These find candidates. Only `#print axioms` confirms the dependency set.

A theorem proved under extra assumptions does not establish the unconditional
claim. A theorem about a weaker statement does not establish the stronger
informal theorem.

## Stage 5: Informal-to-formal correspondence

Produce a table:

| Informal step | Lean declaration | Hypotheses used | Machine-checked? | Status |
|---|---|---|---|---|

Mark any step with no machine-checked counterpart as `UNRESOLVED(informal)`.

## Stage 6: Repository-aware workflow

For the openai/math repository:

- The formalization catalogue and `formalization.yaml` map Lean declarations to
  manuscripts. Use them to locate the entry for a result.
- Confirm from the catalogue whether the top-line result or only supporting
  results are formalized. The README reports about 42% of top-line results
  formalized in total; that figure says nothing about any single result.
- Check the `ComparatorChallenges/` and `patches/` directories and the
  Comparator instructions referenced in the Lean README before relying on any
  specific verification configuration. These were not reviewed when this skill
  was written.
- Inspect related formalizations for reusable lemmas, and record exact
  declaration names.
- Never assume the whole library builds because one module does.

## Output contract

1. Formal statement, exactly as Lean has it.
2. Lean implementation location and declarations.
3. Compilation status: `PASSED`, `FAILED`, or `NOT RUN`, with the command and
   the environment.
4. Axiom and sorry audit results.
5. Assumptions and dependency audit.
6. Informal-to-formal correspondence table.
7. Remaining gaps, each as `UNRESOLVED(...)`.
8. Exact scope: `FORMALIZED(scope)` using the wording of the formal statement.

Never label a theorem formalized because a nearby lemma compiles. Never call a
result complete while `sorry` or an extra axiom is in its dependencies.
