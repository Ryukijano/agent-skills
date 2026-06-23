---
name: nemotron-agent-loop
description: Using Nemotron 3 Nano Omni (multimodal) for agentic loops, document intelligence, and sub-agent orchestration on DGX Spark with vLLM. Core for Lifeline-style projects.
---

## Nemotron Agentic Work

### Env
Separate venv: `venv/nemotron`.

### Deployment
- Serve via vLLM on Spark.
- Runners: `scripts/serve_nemotron_spark.sh`.

### Typical loop (Lifeline pattern)
- Inputs as JSON under `inputs/`.
- Tools: eligibility check, nearest service, draft letter, etc.
- Traces under `outputs/`.
- Use LangGraph or NAT-style orchestration when possible.

### Best practices
- Keep Cosmos3 (video) completely separate.
- For document understanding: feed PDFs/images via the multimodal path.
- Log full prompts + tool calls for audit (privacy-first for benefits use case).

Related: Lifeline hackathon docs, `agentic-loop-lifeline`, `dgx-spark-cosmos3`.
