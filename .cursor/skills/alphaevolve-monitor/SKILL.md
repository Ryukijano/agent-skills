---
name: alphaevolve-monitor
description: >-
  Monitor running AlphaEvolve experiments: track progress, report metrics,
  detect issues, generate final reports. Use when an experiment is running and
  user wants status updates.
---

# AlphaEvolve Experiment Monitor

## Stage 1: Identify the Experiment
1. Get experiment identifier (nickname, ID, or resource name)
2. Verify experiment exists and is running:
```python
experiment = AlphaEvolveExperiment(client, eval_fn)
exp_info = experiment.get_experiment()
# Check status: RUNNING, COMPLETED, FAILED, CANCELLED, PAUSED
```

## Stage 2: Start the Control Loop
1. Determine the evaluator (from project directory)
2. Start the controller loop with dashboard:
```python
asyncio.run(run_controller_loop(experiment))
```
3. Monitor progress:
   - Best score per generation (should trend upward over time)
   - Score distribution (spread indicates exploration)
   - Failure rate (high failure rate may indicate evaluator issues)
   - Programs generated vs evaluated (should track together)

## Stage 3: Experiment Report
### When to post a full report
- Every N generations (e.g., every 10)
- When best score improves significantly
- When user asks "how's it going?"
- When experiment reaches terminal state

### Report Template
```
## Experiment: <name>
**Status**: RUNNING | COMPLETED | FAILED
**Generation**: N / MAX_PROGRAMS
**Best Score**: X.XXX (baseline: Y.YYY, improvement: Z%)
**Score Trend**: ↑ stable | plateau | jumping
**Failure Rate**: N% (M of N candidates failed)
**Top Insights**: 
  - <insight from best program>
  - <insight from recent failures>
```

### Handling "why did programs fail?"
- Check evaluator insights for common failure patterns
- Look for: syntax errors, timeout, NaN/Inf scores, constraint violations
- Failures are normal — they guide the search

## Stage 4: Final Report
1. Gather final data: `experiment.list_programs(params={"order_by": "<metric> desc"})`
2. Check for failures and error patterns
3. Present final report with:
   - Best program score and improvement over baseline
   - Score progression chart
   - Key insights from the evolution
   - Failure analysis
4. Offer next steps: post-experiment analysis, code integration, new experiment
