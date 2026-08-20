# Agentic Loop Design

### Core loop
Observe → Plan (tools) → Act → Verify → (reflect / handoff)

### Tool design
- Pure-ish functions with clear contracts.
- Idempotent where possible.
- Rich error + partial result return for the agent to reason over.

### State & memory
- Short-term scratchpad in prompt.
- Long-term: persisted traces / JSON under outputs/ or a vector store.
- For privacy (benefits, clinical): minimize PII in logs; audit tool calls.

### Verification
- Every tool output that affects user-facing action should be checkable by a human or a second pass.
- Use the verification gate on the agent code itself.

Related: `nemotron-agent-loop`, Lifeline design docs.