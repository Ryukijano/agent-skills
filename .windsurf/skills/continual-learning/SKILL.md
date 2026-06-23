---
name: continual-learning
description: Maintain cross-session context persistence for AI-assisted coding on long-running multi-project work. Use when starting a new session on a previously-worked-on project, ending a session with unfinished work, creating handoff artifacts, or rebuilding context after a context reset. Covers progress files, decision logs, memory database usage, and repo-native continuity patterns.
---

## Continual Learning for Cross-Session Context

### Core principle

**The repo remembers, not the chat window.** Sessions are disposable working memory; durable state lives in files on disk. A new session should rebuild context in under 3 minutes from artifacts alone — no re-explanation needed.

### Three layers of persistence

| Layer | Storage | Lifetime | Purpose |
|-------|---------|----------|---------|
| **Memory DB** | `create_memory` tool | Permanent | User preferences, project facts, technical decisions |
| **Repo artifacts** | Files in the repo | Until deleted/overwritten | Progress, decisions, handoff notes |
| **Git commits** | Commit history | Permanent | Atomic checkpoints of completed work |

### Session start protocol

When beginning work on a project you've worked on before:

1. **Read progress files** (if they exist):
   - `PROGRESS.md` or `agent_context/SESSION_SUMMARY.md` — what was done, what's next
   - `agent_context/AGENTS.md` — learned user preferences and workspace facts
   - Any `CHAT_HANDOFF_*.md` files in the project root

2. **Check recent git history**:
   ```bash
   git log --oneline -20
   git diff HEAD~3 --stat  # see recent changes
   git status              # see uncommitted work
   ```

3. **Check memory DB**: System-retrieved memories are auto-loaded. Verify relevance to the current task before acting on them — they may be stale.

4. **Identify the active branch and its purpose**:
   ```bash
   git branch --show-current
   ```

5. **Scan for TODO markers** in recently modified files:
   ```bash
   grep -rn "TODO\|FIXME\|HACK\|XXX" --include="*.py" --include="*.js" --include="*.ts" | head -20
   ```

6. **State the plan**: Briefly summarize what you know and what you'll do next before taking action.

### Session midpoint practices

- **Commit after each atomic unit of work** — small green commits are the backbone of continuity
- **Update progress files** when completing a milestone, not just at session end
- **Use `tqdm` for long-running operations** (user preference)
- **Write decisions to decision log** when making non-obvious architectural choices
- **Compact aggressively** when the conversation gets long — don't let context drift

### Session end protocol

When a session is wrapping up or context is getting large:

1. **Write a handoff file** if work is unfinished. Place it at:
   - `agent_context/SESSION_SUMMARY.md` (general)
   - Or `CHAT_HANDOFF_YYYY-MM-DD.md` in the project root (project-specific)

2. **Handoff file template**:
   ```markdown
   # Session Handoff — YYYY-MM-DD

   ## What was done
   - [Completed items with file references]

   ## Current state
   - Branch: <branch-name>
   - Uncommitted changes: [yes/no, what]
   - Last checkpoint: <path>

   ## What's next
   - [ ] [Next action with enough detail to execute without re-explanation]
   - [ ] [Following action]

   ## Known issues
   - [Any bugs, blockers, or things to watch out for]

   ## Key decisions made
   - [Non-obvious choices and why]
   ```

3. **Update memory DB** for durable facts:
   - User preferences that emerged during the session
   - Project conventions discovered
   - Technical decisions with long-term impact
   - Environment setup details (conda envs, paths, exports)
   - Use `create_memory` with appropriate tags (snake_case)
   - Check for existing semantically related memories first — update rather than duplicate

4. **Commit all work** — never leave uncommitted changes at session end

5. **Update `agent_context/AGENTS.md`** if new durable preferences or workspace facts were learned

### Repo artifact conventions

| Artifact | Location | When to create | When to delete |
|----------|----------|----------------|----------------|
| `PROGRESS.md` | Project root | Multi-session tasks | When task is fully complete |
| `DECISIONS.md` | Project root | Non-obvious architectural choices | Never (historical record) |
| `SESSION_SUMMARY.md` | `agent_context/` | End of each session | Overwrite each session |
| `CHAT_HANDOFF_*.md` | Project root | Session ends with unfinished work | Next session reads & can delete |
| `AGENTS.md` | `agent_context/` | Learned preferences/facts | Never (living document) |

### Memory DB best practices

- **Store structured facts, not raw transcripts** — "Conda env endofm-lv requires LD_LIBRARY_PATH export" not "the user said to export LD_LIBRARY_PATH..."
- **3-6 high-signal facts per session** — not every exchange warrants storage
- **Use tags** for retrieval: `pytorch`, `conda_env`, `surgical_video`, `ddp_training`, etc.
- **Expiration awareness** — project facts older than 90 days should be re-verified; stale memories can mislead
- **Deduplicate** — always check for existing related memories before creating new ones
- **Scope correctly** — user facts are global; project facts are scoped to a CorpusName

### Cross-project context

This workspace spans multiple projects:
- `Cholec_Vjepa-2/` — Surgical video SSL pretraining (TDV, DINOv2)
- `Conditional-GQE_materials/` — Quantum circuit synthesis
- `anatomical_classification/` — Endoscopic anatomy classification
- `TRACK_JEPA/` — Surgical tracking with JEPA
- `Temporal_Difference-Vision/` — TDV original repo
- `Ryukijano.github.io/` — Personal website

When switching projects mid-session:
1. Commit or stash current work
2. Read that project's progress files
3. Check that project's recent git log
4. Note the switch in the session summary

### Common failure modes and fixes

| Failure | Cause | Fix |
|---------|-------|-----|
| Agent undoes previous work | Didn't read git log/progress | Always check recent commits before editing |
| User re-explains context | No handoff file | Write handoff at session end |
| Stale memory misleads | Old facts, codebase evolved | Re-verify before acting; update or delete |
| Context bloat | Too many memories recalled | Cap at 10 per type; expire old ones |
| Lost decision rationale | No decision log | Write to DECISIONS.md for non-obvious choices |
| Duplicate memories | Didn't check existing | Always search before creating |

### Quick-start checklist for a new session

```
[ ] Read PROGRESS.md / SESSION_SUMMARY.md / handoff files
[ ] Check git log --oneline -20 and git status
[ ] Review system-retrieved memories for relevance
[ ] Identify active branch and its purpose
[ ] State the plan before taking action
```

### Quick-start checklist for session end

```
[ ] Commit all changes
[ ] Write/update handoff file with current state + next steps
[ ] Update memory DB with 3-6 high-signal facts
[ ] Update AGENTS.md if new preferences/facts learned
[ ] Note any blockers or known issues for next session
```
