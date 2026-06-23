---
name: continual-learning
description: >-
  Session-to-session continuity: handoff notes, uncommitted work discipline,
  state files, resuming complex tasks cleanly.
---

## Continual Learning / Handoff

### Rules
- Commit (or at least stash + note) all changes before ending a session. Never leave uncommitted work that the next "you" will trip over.
- Create a short `handoff-<date>.md` or update `AGENTS.md` / run notes with:
  - What was done
  - Next concrete action
  - Any open questions or context needed
- Use `.cursor/hooks/state/` or project `state/` for machine-readable continuity (e.g. continual-learning-index.json).

### Resuming
- Read the latest handoff + AGENTS.md first.
- Run any smoke or verify to re-establish ground truth.
- Only then continue the plan.

Related: verification gate, git-branch-workflow.
