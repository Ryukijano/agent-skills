# Math-skills benchmark (openai/math)

10 real cases from https://github.com/openai/math, pinned at `fd4aeeb2e` (old versions from `adc7f1241`). None of these cases is used as a worked example in the skills.

## Protocol

1. `./setup.sh`: clones openai/math, checks out `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, and writes **text-only** inputs to `run/inputs/<id>/`. PDFs go through `pdftotext`; withdrawn cases come from the pre-withdrawal commit `adc7f1241`; reasoning cases get only the Lean statement file (no proof).
2. Give the tested agent only `run/inputs/<id>/` and the skill. No corpus, no `answers/` (see `answers/README.md`).
3. The agent produces the skill's output contract. Freeze it.
4. Separate scorer step: compare against `answers/key.yaml`.

## Scoring (0/1/2 per case)

| Type | Skill | 2 | 1 | 0 |
|---|---|---|---|---|
| withdrawn | proof-forensics | Locates the decisive failing step and its mechanism, and classifies it as "proof invalid, statement unknown" | Flags the right section, wrong mechanism | Misses it, or declares the theorem false |
| corrected | proof-forensics | Finds the gap or overclaim that the revision addressed | Flags the area | Certifies the old version |
| formalized | lean-proof-bridge | Correspondence table faithful to the paper, and scope exclusions match the key | Statement right, scope wrong | Unfaithful statement |
| reasoning | proof-construction-lab | A mathematically valid proof skeleton: each lemma correct and sufficient, all gaps isolated. **Any valid route counts**; the reasoning summary is only an aid for the grader, not a required lemma set | Valid skeleton with an unacknowledged gap | Invalid or generic |

False alarms: also run forensics on F1–F2. Each `Invalid` flag inside the formalized scope costs −1.

Report: score / 20, per-skill breakdown, false alarms.
