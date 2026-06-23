# Nemotron Agent Loop (Spark)

1. Activate nemotron venv.
2. Start vLLM server if not running (see serve script).
3. Prepare session JSON under inputs/.
4. Launch the agent runner (e.g. `scripts/run_lifeline_agent.sh` or equivalent).
5. Inspect trace in outputs/.
6. For new tools: implement, add to agent graph, test with sample input.
7. Always separate from cosmos3 work.

Apply `nemotron-agent-loop` + read Lifeline design docs.
