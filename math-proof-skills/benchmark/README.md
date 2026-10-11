# Math-skills benchmark (openai/math)

10 real cases from https://github.com/openai/math (commit `fd4aeeb2e`, 7 Oct 2026). The cases are in `cases.yaml`.

## Protocol

1. Clone: `git clone https://github.com/openai/math /workspace/openai-math`.
2. For **corrected** and **withdrawn** cases, give the agent the *pre-fix* text only: `git show adc7f1241:preprints/<dir>/paper.pdf`, or the older dated directory. Never show the README version note, `history.md` or the withdrawal notice. Those are the hidden key.
3. Run the named skill. The agent must produce its standard output contract.
4. Score against `hidden_key`.

## Scoring

| Case type | Skill | Full credit (2) | Partial (1) | Fail (0) |
|---|---|---|---|---|
| withdrawn | proof-forensics | Locates the known failing step and its mechanism (e.g. the sign of the reverse traces), AND says "proof invalid, statement unknown" | Flags the right section as a gap, wrong mechanism | Misses it, or declares the theorem false |
| corrected | proof-forensics / counterexample | Finds the overclaim or gap that the revision fixed | Flags the area | Certifies the old version |
| formalized | lean-proof-bridge | The correspondence table matches the challenge statement, and scope exclusions match `lean/docs/NNN.md` | Statement right, scope wrong | Unfaithful statement |
| reasoning | proof-construction-lab | The lemma skeleton covers the key lemmas named in the summary | Half of them | Generic outline |

Also track **false alarms**: run forensics on 2 formalized cases (expected verdict: no Invalid steps in the formalized scope). Each Invalid flag there costs −1.

Report: score / max, per-skill breakdown, false alarms.
