# Tool-Use Agents

## Description

Design LLM agents that call functions, APIs, and utilities to gather facts and take actions.

## When to use

You are building an agent that needs to interact with external APIs, calculators, databases, or code execution.

## Key concepts

- **Function calling**: the LLM emits structured JSON arguments for registered tools.
- **Tool definitions**: JSON schema describing name, description, and parameters.
- **Observation loop**: execute the tool, return the result, and let the LLM continue.
- **Tool selection**: retrieval over tool descriptions when many tools are available.

## Code pattern

```python
def get_weather(city: str) -> str:
    return f"Sunny, 22 C in {city}"

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        }
    }
}]
```

## Tuning notes

- Keep tool descriptions as clear as user-facing documentation.
- Validate and sanitize arguments before execution.
- Limit context by only returning compact observations.

## Verification

1. Register a calculator and a search stub; test the agent on a multi-step question.
2. Check that invalid tool calls are rejected safely.
3. Measure success rate on a small tool-use benchmark.

## References

- https://arxiv.org/abs/2402.12430
- https://platform.openai.com/docs/guides/function-calling
- https://github.com/anthropics/skills
- https://agentskills.io/
