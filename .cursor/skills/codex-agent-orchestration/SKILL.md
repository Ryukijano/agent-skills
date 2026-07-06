# codex-agent-orchestration


## Description

Orchestrate parallel cloud-based coding agents using OpenAI Codex to autonomously implement, test, and iterate on research codebases. Codex agents run in sandboxed cloud environments with full repo access, enabling concurrent multi-task execution without blocking local development.

## Background

OpenAI Codex (2025) enables spinning up multiple autonomous coding agents in the cloud, each working on isolated branches simultaneously. Unlike local Cursor sessions, Codex agents can run 24/7 unattended - ideal for long-running ML training experiments, refactoring tasks, and CI-driven code generation.

## Core Concepts

- **Cloud Sandboxes**: Each agent runs in an isolated container with full repo clone and shell execution
- **Parallel Branches**: Multiple agents work on separate git branches concurrently; merge via PR
- **Task Delegation**: Decompose large features into subtasks; assign each to a separate Codex agent
- **Verification Gates**: Each agent run produces a diff + test report for human review before merge
- **Context Injection**: Provide AGENTS.md at repo root to give all agents project-level instructions

## Orchestration Workflow

1. Decompose project into 3-5 parallel subtasks (data pipeline, model architecture, eval harness)
2. Write task specs - concise natural language with acceptance criteria
3. Launch agents via Codex UI or API, one per subtask, pointing to main branch
4. Monitor agent progress in the Codex dashboard (diffs, shell logs, test results)
5. Review PRs - each agent opens a PR; review diff + CI results
6. Merge sequentially - merge non-conflicting PRs; rebase conflicting ones
7. Iterate - re-task agents on failing tests or follow-up features

## Integration with Cursor + Antigravity

- **Cursor**: local interactive development and debugging
- **Codex**: batch/unattended tasks (training script refactors, test generation, documentation)
- **Antigravity**: orchestrate the overall pipeline (trigger Codex tasks, monitor outputs)
- Pattern: Cursor prototype locally -> delegate to Codex agents -> review PRs in Cursor

## Key Tips

- Keep task specs under 200 words; Codex works best with focused, scoped instructions
- Include file paths in task specs to reduce ambiguity
- Use AGENTS.md to encode project conventions once rather than repeating in every task
- For ML projects: always specify GPU requirements and expected runtime in task spec

## References

- OpenAI Codex: https://openai.com/codex
- Related skills: agentic-loop-design, agentic-context-engineering
Orchestrate parallel cloud-based coding agents using OpenAI Codex.
