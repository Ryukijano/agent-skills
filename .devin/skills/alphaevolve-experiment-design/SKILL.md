# AlphaEvolve Experiment Design

## Preconditions
- User has a problem description (natural language, may be vague)
- Optional: existing code to optimize
- Optional: target directory path (ask if not provided)

## Postconditions
A project directory containing:
- `.evolve/experiment_description.json` — Complete experiment specification
- `.evolve/source_map.json` — Maps code regions to original source (when optimizing existing code)
- `initial_program.py` — Seed program with `EVOLVE-BLOCK` markers and `ORIGIN` comments
- `evaluator.py` — CLI-compatible evaluator script
- `problem_description.md` — Detailed technical problem description
- `example_evaluation.json` — Sample evaluator output
- `test_program.py` — Pytest tests for the initial program
- `test_evaluator.py` — Pytest tests for the evaluator
- `pyproject.toml` — uv project configuration
- `README.md` — Experiment documentation

All pytest tests pass via `uv run pytest`.

## Phase 1 — Clarify
**Objective**: Fill the ExperimentDescription through conversation with the user.
**Gate**: `experiment_description.json` is written to `project_dir/.evolve/`.

Key questions to clarify:
- What metric(s) should be optimized? (higher = better, AlphaEvolve always maximizes)
- What are the constraints? (time, memory, correctness)
- What is the search space? (which code regions can evolve)
- What language? (Python, C++, Verilog, etc.)

## Phase 2 — Implement
**Objective**: Generate all project files and verify they work.
**Input**: The ExperimentDescription is the ONLY input. If info is missing, Phase 1 was incomplete.
**Gate**: `uv run pytest` passes in the project directory.

### EVOLVE-BLOCK Markers
```python
# EVOLVE-BLOCK-START
def function_to_optimize(...):
    ...  # AlphaEvolve rewrites everything inside this block
# EVOLVE-BLOCK-END
```

### Evaluator Requirements
- Must be CLI-compatible: `uv run python evaluator.py --output-file <path> --program-dir <path>`
- Must export `evaluate_program(code, timeout_seconds=30) -> dict` returning `{"score": float|None, "insights": [...]}`
- AlphaEvolve always maximizes — negate scores for minimization problems
- Handle NaN/Inf scores: return null with error insight (NaN in JSON is invalid)
- Insights: list of `{"label": str, "text": str}` dicts (stdout, stderr, errors, tracebacks)

## Critical Rules
1. Phase 1 is conversation only — no code files, only `experiment_description.json`
2. Phase 2 requires no user interaction — ExperimentDescription has everything
3. Tests first — write tests before the code they test
4. Never execute user code directly — syntax-check with `uv run python -c "import ast; ast.parse(...)"`
5. Always use `uv run` — NEVER bare `python3`
6. Validate EVOLVE-BLOCK markers before declaring Phase 2 complete
7. Use `uv` for all project management — `pyproject.toml`, `uv run pytest`
