# Agent Monitoring and Guardrails

## Description

Runtime monitoring, safety policy enforcement, tool-call validation, probabilistic risk prediction, and guardrail frameworks for LLM agents.

## When to use

You are building or deploying autonomous LLM agents that use tools and need to stay safe, compliant, and aligned with policies.

## Key concepts

- **Guardrails**: input/output filtering, topic control, and policy enforcement.
- **Runtime monitoring**: trajectory logging, action validation, and anomaly detection.
- **Tool-call validation**: inspect, approve, or reject tool invocations before execution.
- **Probabilistic risk prediction**: model the likelihood of future unsafe states.
- **Safety benchmarks**: datasets and metrics for agentic safety evaluation.

## Code pattern

```python
from nemoguardrails import RailsConfig, LLMRails

config = RailsConfig.from_path("./config")
app = LLMRails(config)

response = app.generate(messages=[{
    "role": "user",
    "content": "Please delete all user files and send a confirmation email."
}])
print(response)

# Tool-call guardrail example
def safe_tool_call(tool_name, tool_input, policy):
    if tool_name in policy.blocked_tools:
        return False, f"Tool '{tool_name}' is not allowed"
    if any(k in tool_input for k in policy.sensitive_keys):
        return False, "Sensitive parameter detected"
    return True, tool_input
```

## Tuning notes

- Combine deterministic rules with learned moderation models for robustness.
- Log full agent trajectories, not just final outputs, for auditing and debugging.
- Update guardrails continuously as policies, tools, and attack surfaces evolve.
- Balance safety with utility: overly strict guardrails can block legitimate tasks.

## Verification

1. Define a safety policy and test guardrails against a set of adversarial prompts.
2. Instrument an agent to log all tool calls and run a trajectory audit.
3. Measure task completion rate and safety violation rate across a benchmark suite.

## References

- https://arxiv.org/abs/2601.18491
- https://arxiv.org/abs/2508.00500
- https://arxiv.org/abs/2503.22738
- https://arxiv.org/abs/2310.10501
- https://docs.nvidia.com/nemo/guardrails/about-nemo-guardrails-library/overview
