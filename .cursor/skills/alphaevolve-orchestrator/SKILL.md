# AlphaEvolve Orchestrator

## Overview
Coordinates the 4-phase AlphaEvolve workflow. Detects where the user is and routes to the appropriate sub-skill.

## Entry Point Detection

### Start at Phase 1 (Design) if:
- User describes a problem in natural language ("make this faster", "optimize this packing")
- User provides source code but no evaluator
- User says "set up an experiment" or "optimize my code at `<path>`"
- No experiment artifacts exist yet

### Start at Phase 2 (Runner) if:
- User has `initial_program.py` AND `evaluator.py` ready
- User says "launch this experiment" or "run this"

### Start at Phase 3 (Monitor) if:
- User provides an experiment nickname, ID, or resource name
- User says "how is my experiment doing" or "show results"
- An experiment is already running

### Start at Phase 4 (Post-Experiment) if:
- User says "show me results", "analyze", "integrate the evolved code"
- Experiment is in terminal state (COMPLETED, FAILED, CANCELLED)

## Phases
1. **Design** → `alphaevolve-experiment-design` skill
2. **Runner** → `alphaevolve-runner` skill
3. **Monitor** → `alphaevolve-monitor` skill
4. **Post-Experiment** → `alphaevolve-post-experiment` skill

## Critical Rules
- Never skip a required gate — each phase has a completion gate
- Track state across phases — record handoff artifacts explicitly
- Never execute user code directly — delegate to sub-skills with sandboxed evaluation
- Never initiate version control workflows unless explicitly asked
- When user says "optimize my code at `<path>`" — proceed directly to Phase 1

## Phase Diagram
```
[User input] → Detect entry point
       ↓
Phase 1: Design (experiment_description.json, initial_program.py, evaluator.py)
       ↓ Gate: uv run pytest passes
Phase 2: Runner (create experiment, start, run controller loop)
       ↓ Gate: experiment is RUNNING
Phase 3: Monitor (dashboard, progress reports)
       ↓ Gate: experiment reaches terminal state
Phase 4: Post-Experiment (results, code review, integration)
       ↓ Gate: user has results report
[Done]
```

## Error Recovery
- Phase 1 fails → fix design issues, regenerate files
- Phase 2 fails → check GCP config, connectivity, evaluator
- Phase 3 fails → check experiment state, retry monitoring
- Phase 4 fails → check data availability, retry analysis
