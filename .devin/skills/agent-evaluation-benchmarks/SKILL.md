# Agent Evaluation Benchmarks

## Description

Measure agent capability on coding, web, tool use, and open-ended reasoning benchmarks.

## When to use

You need to compare agents or track progress across real-world capabilities.

## Key concepts

- **SWE-bench / SWE-bench Verified**: resolve real GitHub issues.
- **WebArena / Mind2Web**: web browsing and form-filling.
- **ToolBench**: API calling and tool selection.
- **HumanEval / MBPP+**: coding proficiency.
- **GAIA**: general assistant tasks requiring reasoning and tools.

## Code pattern

```python
from datasets import load_dataset
from evaluate import load

swebench = load_dataset("princeton-nlp/SWE-bench", " Lite")
# Run your agent on each instance and compare to gold patch.
```

## Tuning notes

- Start with a small subset before running a full benchmark.
- Check that the environment and dependencies are exactly as expected.
- Separate pass@1 from pass with retries and compute budget.

## Verification

1. Run HumanEval on the agent's code generator.
2. Evaluate on a handful of SWE-bench Lite instances.
3. Track success rate per benchmark and per task category.

## References

- https://arxiv.org/abs/2310.06770
- https://www.swebench.com/
- https://arxiv.org/abs/2307.13854
- https://arxiv.org/abs/2311.08377
