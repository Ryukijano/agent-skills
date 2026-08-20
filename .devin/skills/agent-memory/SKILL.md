# Agent Memory Systems

## Description

Short-term and long-term memory for agents: vector stores, summaries, entity tracking, and memory hierarchies.

## When to use

Your agent must remember facts, user preferences, or prior interactions across a long session or multiple sessions.

## Key concepts

- **Working memory**: current conversation context.
- **Long-term memory**: stored facts, summaries, and embeddings.
- **Entity and event memory**: track objects, people, and occurrences.
- **Memory retrieval**: recency, relevance, and importance scoring.
- **MemGPT / MemoryBank**: example architectures for managing memory.

## Code pattern

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "My name is Alice"}, {"output": "Nice to meet you, Alice"})
print(memory.load_memory_variables({}))
```

## Tuning notes

- Combine embedding retrieval with recent-message injection.
- Summarize old conversation to compress context.
- Protect privacy: do not persist sensitive data without consent.

## Verification

1. Build a simple agent that remembers a user's name and preferences.
2. Test memory recall after many conversational turns.
3. Measure latency of vector-store retrieval vs in-memory summary.

## References

- https://arxiv.org/abs/2403.12039
- https://github.com/Stanford-ILIAD/MemGPT
- https://arxiv.org/abs/2312.03689
- https://python.langchain.com/docs/modules/memory/
