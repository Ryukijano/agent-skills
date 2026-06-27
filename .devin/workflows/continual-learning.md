---
description: Maintain cross-session context persistence with progress files and handoff artifacts
---

## Continual Learning Session

1. **Session start**: Read progress files and recent git history:
   ```bash
   cat PROGRESS.md agent_context/SESSION_SUMMARY.md 2>/dev/null
   git log --oneline -20
   git status
   git branch --show-current
   ```

2. State the plan: summarize what you know and what you'll do next.

3. **During session**: Commit after each atomic unit. Update progress files at milestones.

4. **Session end**: Write handoff file:
   ```markdown
   # Session Handoff — YYYY-MM-DD
   ## What was done
   ## Current state (branch, uncommitted, last checkpoint)
   ## What's next
   ## Known issues
   ## Key decisions
   ```

5. Update memory DB with 3-6 high-signal facts.

6. Commit all changes. Never leave uncommitted work at session end.

7. Summarize: handoff file location, next session's first action.
