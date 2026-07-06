# antigravity-ide-workflow

## Description

Leverage Antigravity IDE for orchestrating multi-agent AI workflows with background execution, parallel task management, and seamless integration with Cursor and Codex. Antigravity enables running long-horizon research pipelines while maintaining an interactive local development session.

## Background

Antigravity is a next-generation AI IDE designed for research engineers who need to run multiple AI agents concurrently. Unlike traditional IDEs, it treats agent execution as a first-class citizen - you can spawn background agents, monitor their progress, and integrate their outputs without interrupting your primary coding flow.

## Core Capabilities

- **Background Agent Execution**: Run long-running agents (training, data processing) without blocking local work
- **Multi-Pane Agent Views**: Monitor multiple agent streams (logs, diffs, tool calls) side by side
- **Context Sharing**: Share codebase context across agents; changes from one agent are immediately visible to others
- **Checkpoint Integration**: Pause, resume, and fork agent runs at any point
- **NotebookLM Bridge**: Push agent outputs (summaries, findings) directly to NotebookLM sources
- **HPC Job Integration**: Submit SLURM jobs from within the IDE; monitor GPU utilization in real-time

## Workflow Pattern for Research Projects

### Setup

1. Open project root in Antigravity
2. Configure agent profiles in `antigravity.config.json`:
   - background-trainer: GPU job submission agent
   - research-assistant: Literature search + NotebookLM updates
   - code-reviewer: Continuous quality monitoring
3. Set up context sources: codebase, recent papers, experiment logs

### Daily Research Loop

1. **Morning**: Review overnight agent outputs (training curves, PR drafts, paper summaries)
2. **Active coding**: Use foreground Cursor-style agent for interactive development
3. **Background**: Keep research-assistant agent running to index new papers matching your domains
4. **Evening**: Trigger eval-harness agent to benchmark the day's changes
5. **Async**: Codex agents handle documentation and test generation overnight

### Integration with DGX Spark / HPC

- Configure Antigravity's SLURM integration to submit H100/H200 jobs directly from task prompts
- Monitor job status and GPU utilization within IDE panels
- Automatically pull training logs back into the IDE context when jobs complete

## Key Tips

- Use Antigravity for orchestration, Cursor for focused editing - they complement each other
- Keep background agents scoped: one agent per concern (training, research, review)
- Enable auto-checkpoint every 30 minutes for long-running agents to enable recovery
- Use the NotebookLM bridge to build a persistent knowledge base from agent discoveries
- Tag important agent outputs with #research or #insight for retrieval later

## Configuration Example

```
# antigravity.config.json
{
  "agents": [
    {"name": "researcher", "mode": "background", "context": "notebooklm"},
    {"name": "trainer", "mode": "hpc", "cluster": "arc4-gpu"},
    {"name": "reviewer", "mode": "foreground", "context": "codebase"}
  ],
  "integrations": {
    "notebooklm": true,
    "slurm": true,
    "codex": true
  }
}
```

## References

- Antigravity IDE: https://antigravity.ai
- Related skills: codex-agent-orchestration, agentic-loop-design, notebooklm-research-workflow
