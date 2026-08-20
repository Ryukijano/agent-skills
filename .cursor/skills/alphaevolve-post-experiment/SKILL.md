# AlphaEvolve Post-Experiment Processing

## Stage 1: Quick Results Overview
```python
best = experiment.list_programs(params={"order_by": "<metric> desc", "limit": 1})
all_programs = experiment.list_programs(params={"order_by": "<metric> desc"})
```
Present: best score, baseline score, improvement %, total programs evaluated.

## Stage 2: Code Review & Validation
1. Fetch the best program's code
2. Show the diff between seed and evolved code
3. Explain the changes (what was optimized and why)
4. **Reward hacking check**: Verify the score improvement is genuine:
   - Did the code exploit a loophole in the evaluator?
   - Does the optimized code actually solve the problem?
   - Are there edge cases where it fails?
5. Present code review summary

## Stage 3: Report
1. Generate score progression chart (best-so-far per generation)
2. Analyze the evolution journey (key breakthroughs, plateaus)
3. Analyze failures (common patterns, what was tried and discarded)
4. Compute practical impact (speedup, memory reduction, etc.)
5. Write markdown report with:
   - Problem description
   - Seed vs evolved code
   - Score progression
   - Key insights
   - Failure analysis
   - Recommendations
6. Generate interactive HTML report (optional)

## Stage 4: Code Integration (optional)
1. Offer code integration — ask user if they want to apply the evolved code
2. Load the source map (`.evolve/source_map.json`) to find original file locations
3. Extract the evolved code from the best program
4. Apply changes to the original source files
5. Validate integration:
   - Run existing tests: `uv run pytest`
   - Run the evaluator on the integrated code
   - Check for regressions
6. Present completion summary with before/after metrics

## Artifacts Produced
- `report/evolution_progress.png` — Best-so-far score per generation
- `report/score_distribution.png` — Score distribution across candidates
- `evolved_program/program.py` — Best evolved program
- `result.json` — Full results JSON
- `report/experiment_report.md` — Full markdown report
