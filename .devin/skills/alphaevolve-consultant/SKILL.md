---
name: alphaevolve-consultant
description: >-
  Expert consultant on AlphaEvolve concepts: architecture, suitability,
  evaluator design, EVOLVE-BLOCK placement, model mixture, troubleshooting. Use
  when user has questions about AlphaEvolve.
---

# AlphaEvolve Expert Consultant

## What is AlphaEvolve?
AlphaEvolve is a Gemini-powered evolutionary coding agent for general-purpose algorithm discovery and optimization. You provide a seed program and a scoring function; AlphaEvolve uses Gemini to propose code changes, evaluates each candidate, and evolves the population toward better solutions.

## Architecture
The managed service runs three components:
1. **Prompt Sampler** — selects and formats prompts for the LLM ensemble
2. **LLM Ensemble** — mixture of Gemini models (Flash for breadth, Pro for depth)
3. **Program Database** — stores and tracks candidate programs and solutions

You own the **Evaluator** — a deterministic function that scores candidates.

## The Evolutionary Loop
```
[Seed Program] → LLM generates mutations → Evaluator scores → 
  Program Database stores → Next generation uses best programs → Repeat
```

## Suitability Assessment
**Good candidates for AlphaEvolve:**
- Problems where you can define a clear scoring function
- Algorithmic optimization (sorting, packing, routing, scheduling)
- Hyperparameter optimization (LoRA configs, training params)
- Code where multiple valid approaches exist
- Problems with large search spaces that are hard to enumerate

**Poor candidates:**
- Problems without measurable metrics
- One-shot code generation (no optimization needed)
- Problems where correctness cannot be verified automatically
- Extremely fast problems where LLM latency dominates

## EVOLVE-BLOCK Placement
- Wrap the code region you want to optimize in `# EVOLVE-BLOCK-START` / `# EVOLVE-BLOCK-END`
- Keep interfaces stable — don't wrap function signatures, only implementations
- Multiple EVOLVE-BLOCKs are supported for multi-region optimization
- Include `ORIGIN` comments to track original code for diffing

## Evaluator Design (Three-Tier)
1. **Fast checks**: syntax, imports, basic correctness (always run)
2. **Functional tests**: does it produce correct output? (usually run)
3. **Performance metrics**: speed, memory, quality (run on survivors)

### Multi-Objective Scoring
Return multiple metrics: `{"speed": 1.2, "memory": 0.8, "accuracy": 0.95}`
AlphaEvolve optimizes the primary metric while tracking others.

### Reward Hacking Prevention
- Use held-out test cases the evaluator doesn't see
- Add constraint checks (timeouts, memory limits)
- Verify outputs are semantically correct, not just numerically high
- Use multi-objective scoring to prevent over-optimizing one metric

## Model Mixture
- `gemini-3.5-flash` (weight 0.7): breadth — explores many ideas quickly
- `gemini-3.1-pro-preview` (weight 0.3): depth — provides insightful suggestions
- Adjust weights based on problem complexity

## Troubleshooting
| Issue | Solution |
|-------|----------|
| Score plateau | Normal — wait, or increase budget |
| All programs failing | Check evaluator, EVOLVE-BLOCK syntax |
| Experiment PAUSED | Check API quota, billing |
| LLM throttling | Reduce concurrency |
| Reward hacking | Add constraint checks, held-out tests |
| Context window pollution | Reduce problem description length |

## Key Config Parameters
| Parameter | Default | Description |
|-----------|---------|-------------|
| MAX_PROGRAMS_GENERATED | 100 | Total candidates to generate |
| MAX_PROGRAMS_EVALUATED | 100 | Total candidates to evaluate |
| CONCURRENCY | 4 | Parallel API calls |
| WORKER_CONCURRENCY | 4 | Parallel evaluations |
| PARALLEL_EVALUATION | True | Run evaluations in parallel |
