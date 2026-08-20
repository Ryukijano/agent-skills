# Multi-Agent Orchestration

## Description

Coordinate multiple specialist agents to decompose tasks, debate, and synthesize solutions.

## When to use

A single agent is not enough; you need several agents with different roles collaborating on a complex task.

## Key concepts

- **Role-based agents**: planner, coder, reviewer, verifier.
- **Conversation patterns**: sequential, round-robin, hierarchical, group chat.
- **Task decomposition**: break a problem into subtasks assigned to agents.
- **Consensus and aggregation**: voting, merging, or meta-agent summarization.

## Code pattern

```python
# Pseudo-code for a two-agent round-robin
coder = Agent(name="Coder", instructions="Write Python functions.")
reviewer = Agent(name="Reviewer", instructions="Review for bugs.")

debate = GroupChat(agents=[coder, reviewer], messages=[])
result = debate.run("Implement a function that returns prime numbers up to N.")
```

## Tuning notes

- Define clear roles and stopping conditions.
- Limit the number of turns to avoid runaway costs.
- Use a shared scratchpad for intermediate results.

## Verification

1. Set up a coder-reviewer pair and run on a small coding task.
2. Compare multi-agent output to a single agent on the same task.
3. Measure how often the conversation reaches a useful consensus.

## References

- https://arxiv.org/abs/2402.16820
- https://github.com/microsoft/autogen
- https://arxiv.org/abs/2401.08507
- https://arxiv.org/abs/2402.16672
