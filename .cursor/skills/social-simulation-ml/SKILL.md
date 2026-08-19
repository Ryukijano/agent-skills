# Social Simulation and Agent-Based Modeling with ML

## Description

AgentTorch, LLM-based agents, differentiable ABM, and causal discovery for social and economic systems.

## When to use

You are simulating social, economic, or policy scenarios with agent-based models and ML.

## Key concepts

- **Agent-based models (ABM)**: agents, rules, emergent behavior.
- **LLM agents**: AgentTorch, GASim, CAMO; agents with LLM reasoning.
- **Differentiable ABM**: gradient-based calibration and optimization.
- **Causal discovery**: infer micro-to-macro mechanisms.

## Code pattern

```python
import agent_torch

# Define agents, environment, policy
cfg = agent_torch.Config(...)
runner = agent_torch.Runner(cfg)
runner.execute()
```

## Tuning notes

- Validate ABMs against real-world aggregate data.
- LLM agents can be expensive; use smaller models or caching.
- Use sensitivity analysis to understand parameter effects.

## Verification

1. Reproduce a known social phenomenon (e.g., market bubble) in simulation.
2. Compare aggregate ABM output to real data.
3. Calibrate ABM parameters with gradient descent or ABC.

## References

- https://github.com/AgentTorch/AgentTorch
- https://aclanthology.org/2026.acl-long.569/
- https://aclanthology.org/2026.findings-acl.1224.pdf
