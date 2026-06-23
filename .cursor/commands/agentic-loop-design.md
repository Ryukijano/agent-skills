# Design / Extend an Agentic Loop

1. Read existing agent graph and tool contracts.
2. Define the new capability as a tool with typed input/output and error model.
3. Add the tool to the graph with clear routing / conditions.
4. Add a regression test (sample input → expected behavior class).
5. Run a full trace on a canonical input; review the trace.
6. Update handoff / docs.
7. Verify with the broader project tests + any domain-specific checks (eligibility, letter draft, etc.).

Apply `agentic-loop-design`, `nemotron-agent-loop`, `reproducibility`.
