# Deep-math proof skills

Five skills for doing real mathematics with an agent: building proofs, refereeing them, breaking them, formalizing them, and mapping how results depend on each other. They are not tutoring prompts.

The reference corpus is [openai/math](https://github.com/openai/math), cloned at `/workspace/openai-math` (`git clone https://github.com/openai/math`). It holds model-written manuscripts, a Lean 4 library, Comparator challenges, reasoning summaries and a public correction history. The skills work on any proof. The corpus supplies worked examples and the benchmark.

## The pack

| Skill | Owns | Hands off to |
|---|---|---|
| `proof-construction-lab` | Turning a frozen statement into a proof with explicit dependencies | `proof-forensics` |
| `proof-forensics` | Refereeing the proof independently, step by step | `counterexample-and-invariant-discovery` when a step is suspect |
| `counterexample-and-invariant-discovery` | Testing which hypotheses do real work, and finding minimal, exactly verified counterexamples | back to the constructor (repair) or on to `lean-proof-bridge` |
| `lean-proof-bridge` | Writing a faithful formal statement, the proof, and a trust audit | `theorem-family-cartographer` |
| `theorem-family-cartographer` | A typed, versioned graph of how results relate | feeds the next construction |

Pipeline: **constructor → forensics → counterexample → lean bridge → cartographer**. A skill never certifies work it produced itself. The constructor's output always goes to forensics, run as a fresh pass.

## Trust rules (shared by every skill)

1. A manuscript is a research artifact to examine, not an established theorem. The openai/math README itself says "Some of the unformalized results could have issues."
2. Only Lean-checked statements count as machine-verified, and only the exact formal statement. Anything in the paper beyond it is unverified (see the "outside this selected statement" lines in `lean/docs/NNN.md`).
3. Compiling is not faithfulness. A statement must be checked against the informal claim by hand, and the Comparator `permitted_axioms` must be audited.
4. An incomplete or invalid proof does not make the theorem false. openai/math withdrawals say so explicitly: "This withdrawal concerns the proof; it does not assert that the mathematical statement is false."
5. Numerics, plots and a large number of companion papers are evidence, not proof.
6. Errors propagate along dependency edges. One sign error withdrew three papers on 7 Oct 2026, and companion fixes forced citation updates to 13 more.
7. Results are tied to a version. Cite the dated directory, or the commit for archived PDFs.

## Layout

```
.cursor/skills/<skill>/SKILL.md   the skill (YAML frontmatter: name, description)
.cursor/skills/<skill>/references.md  corpus paths
math-proof-skills/benchmark/README.md       protocol and scoring
math-proof-skills/benchmark/cases.yaml      10 real cases from openai/math
```
