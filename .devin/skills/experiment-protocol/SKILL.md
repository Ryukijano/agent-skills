---
name: experiment-protocol
description: >-
  Design reproducible experiments: define design and controls, complete
  pre-registration checklist, then execute. Use when planning ablation studies,
  benchmarking, empirical validation, or pre-registering experimental protocols
  before running code.
---

# Experiment Protocol

Iterative loop: **design → controls → pre-register checklist → execute → verify results → refine**.

## Verification Loop

**Design → synthesize protocol → verify against hypothesis canvas and controls checklist → refine before execution.**

## Read First

- `research/hypothesis-canvas.md` — primary hypothesis and predictions
- [references/checklist.md](references/checklist.md) — pre-registration checklist
- Existing codebase and data manifests

## Procedure

### 1. Design

Document in `experiments/<exp-id>/protocol.md`:

- **Objective** — which hypothesis H<n> this tests
- **Primary outcome** — single pre-specified metric
- **Secondary outcomes** — exploratory; labeled as such
- **Unit of analysis** — sample, trial, model run, etc.
- **Sample size** — power rationale or budget constraint

### 2. Controls

Define explicitly:

| Control type | Specification |
|--------------|---------------|
| Baseline | What is the comparison? |
| Ablations | What components are removed/varied? |
| Random seeds | How many? Fixed seed list? |
| Hyperparameters | Search space or fixed values |
| Hardware | GPU type, batch size, precision |
| Data splits | Train/val/test protocol; leakage checks |

### 3. Pre-register checklist

Complete every item in [references/checklist.md](references/checklist.md) **before** any results-producing run. Record completion date in protocol.

### 4. Environment manifest

Create `experiments/<exp-id>/environment.lock`:

- Python/CUDA versions
- Package lockfile or conda export
- Git commit hash
- Data snapshot IDs

### 5. Execute

1. Run baseline first; verify metric pipeline on known subset.
2. Run treatment conditions in documented order.
3. Log every run: config hash, start/end time, output paths, exit status.
4. No post-hoc condition additions without protocol amendment.

### 6. Verify & refine

- Compare results to pre-registered predictions.
- If pipeline fails, fix and re-run from clean state — do not patch results.
- Amend protocol with dated amendment note if design must change.

## Protocol Template

```markdown
# Experiment: <exp-id>

## Hypothesis & Prediction
## Design
## Primary Outcome
## Conditions
| ID | Description | Seeds |
## Controls & Ablations
## Data
## Analysis Plan
[Pre-specified tests; no p-hacking]
## Stopping Rules
## Pre-registration Status
- [ ] Checklist complete (date: )
```

## Rules

- One primary outcome per experiment; others are exploratory.
- Checklist complete before first results run.
- Protocol amendments logged; never rewrite history silently.
- Failed runs logged, not discarded.

## Done When

- `protocol.md` and `environment.lock` exist
- Pre-registration checklist signed off
- All conditions executed per protocol or amendments documented
- Results logged under `experiments/<exp-id>/outputs/`
