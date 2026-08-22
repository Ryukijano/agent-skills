---
name: research-strategy-project-design
description: Research project strategy — problem triage, hypothesis framing with falsifiable predictions, risk/kill criteria, milestone planning, and minimal viable experiments.
---

## Research Strategy & Project Design

### Problem triage
For each candidate idea score 1-5: novelty, feasibility, impact, learning value, fit with your agenda. Pursue the Pareto front, not the max-novelty point.

### Hypothesis framing
- Format: "If we do X under conditions Y, then Z will happen, measurable by M."
- Every hypothesis gets a falsifiable prediction and a metric defined **before** running.
- Distinguish: exploratory ("what happens if...") vs confirmatory ("we predict...") — label runs accordingly.

### Kill criteria (decide before starting)
- Time-box: e.g., "if pilot < baseline by week 2, stop or pivot."
- Metric-box: e.g., "if val mAP@50 < 0.20 after Stage-1 full training, revisit architecture."
- Killing early is a result. Write it down; it feeds `gap-to-topic` for the next idea.

### Milestone ladder
1. Smoke test (tiny data, tiny model, 1 GPU-hour) — pipeline works end to end.
2. Pilot (one dataset fold) — signal exists.
3. Full run + ablation matrix (`ablation-study`).
4. Robustness (seeds, OOD split) → paper-ready.

### Risk register
| risk | likelihood | mitigation |
e.g., "annotation quality" / high / dual-label 10% subset + kappa check.

Related: `gap-to-topic`, `experiment-protocol`, `hypothesis-canvas`.
