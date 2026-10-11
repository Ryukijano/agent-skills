---
name: lean-proof-bridge
description: Use when an informal theorem must be turned into a faithful Lean 4 statement and proof, or when you must audit exactly what an existing Lean formalization does and does not verify.
---

# Lean Proof Bridge

Lean is the verification boundary, but only for the exact formal statement. Faithfulness comes first, then tactics. Compiling is not faithfulness.

## Workflow

1. **Translate the statement before any tactic.** Write the Lean `theorem`/`def` with `sorry`. Next to it, write a correspondence table: informal clause → Lean term → match notes (coercions ℤ→ℝ, `sSup` of an empty or unbounded set, `Fintype` vs `Finite`, `Group.FG`, a junk value like `x/0 = 0`, natural-number subtraction).
2. **Faithfulness review.** Have an independent reader (or `proof-forensics`) check the table. Common failures: a hypothesis made vacuous, an existential where the paper is universal, the wrong ε-quantifier order, a conclusion trivially true by junk values, a definition that differs from the literature.
3. **Dependency map.** Identify the Mathlib API you'll use, plus any external libraries. Split the work into lemmas that mirror the informal skeleton from `proof-construction-lab`.
4. **Prove incrementally.** Do one lemma at a time and build often (`lake build <Module>`), not the whole library.
5. **Trust audit.** Run `#print axioms <thm>`. Allow only `propext`, `Quot.sound` and `Classical.choice` unless declared otherwise. Check for `sorry`, `axiom`, `native_decide`/`ofReduceBool`, `implemented_by` and `opaque` tricks, extra assumptions hidden in `variable` blocks or typeclass instances, and redefinitions of standard notions.
6. **Report scope.** Say what is verified (the exact statement) and what in the paper is outside it.

## Output contract

The Lean statement; the correspondence table; the proof or the current `sorry` list; the `#print axioms` output; the scope statement ("verifies X; does not cover Y"); and build instructions (toolchain, commands).

## Using the openai/math corpus

Toolchain: `lean/lean-toolchain` = `leanprover/lean4:v4.34.1`. Lake project with Mathlib and about 20 external libraries (`lean/lakefile.lean`, `lean/lake-manifest.json`; patches for v4.34.1 are in `lean/patches/`).

```bash
cd /workspace/openai-math/lean
cat formalization.yaml           # catalogue v0.4: sources + status.main_results (comparator_config, declaration, file)
ls docs/                         # per-family scope notes NNN.md: what is and isn't formalized
ls ComparatorChallenges/*.json | wc -l   # 416 challenge configs
cat ComparatorChallenges/PiExponent.json # challenge_module, solution_module, theorem_names, permitted_axioms
# verify one result (needs comparator, landrun, lean4export on PATH):
lake update && lake exe cache get
lake env comparator ComparatorChallenges/PiExponent.json
```

How it fits together: a challenge file `ComparatorChallenges/X.lean` holds the trusted statement with `sorry` (that is the point: it is the spec). The solution lives under `OAI/<Area>/...`. Comparator checks that the solution proves the same statement using only `permitted_axioms`. So: review the challenge `.lean` for faithfulness and trust Comparator for the proof.

Caveats: build small portions only. A full build can hit `vm.max_map_count` (see `lean/README.md`). The catalogue's `status.main_results` lists 200 entries and `review: status: unchecked`, and some challenges (e.g. `PiExponent`, `KaplanskyDirectFiniteness`) are referenced from `docs/` but not listed there. Cross-check `docs/`, `ComparatorChallenges/` and `formalization.yaml`, not just one of them.

## Worked example: auditing a real formal statement (real)

Family 017. `ComparatorChallenges/PiExponent.lean`:

```lean
theorem main :
  (∀ ν : ℝ, 2 < ν → ∃ Q : ℤ, 2 ≤ Q ∧
    ∀ p q : ℤ, Q ≤ q →
      (q : ℝ) ^ (-ν) ≤ |Real.pi - (p : ℝ) / (q : ℝ)|) ∧
  sSup {ν : ℝ | 0 < ν ∧
    Set.Infinite {r : ℚ | 2 ≤ r.den ∧
      0 < |Real.pi - (r : ℝ)| ∧
      |Real.pi - (r : ℝ)| < (r.den : ℝ) ^ (-ν)}} = 2 := by sorry
```

Correspondence checks: (1) `q : ℤ` with `Q ≤ q`, `2 ≤ Q` forces q positive, so the real power is well defined ✔. (2) `sSup` over ℝ: the set must be nonempty and bounded above, or `sSup` returns junk (0). Here the set is nonempty (Dirichlet, any ν<2) and the first conjunct bounds it, so the conjunction is meaningful ✔. (3) `r.den ≥ 2` excludes integers, which is harmless for the exponent ✔. (4) Scope (`lean/docs/017.md`): the Flint–Hills series consequence is **not** verified.

Second exercise: the Kaplansky challenge (see `counterexample-and-invariant-discovery`) is `∃ … a * b = 1 ∧ b * a ≠ 1` with `Fintype K`, `CharP K 2`, `Group.FG G`. Is `Group.FG` faithful to the paper's "finitely generated"? Is finite presentability a separate statement (`KaplanskyFinitelyPresented`)?
