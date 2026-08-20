# Context Engineering

## Context Hierarchy
1. **Rules Files**: AGENTS.md, .devin/skills/ — always loaded
2. **Specs/Architecture**: Load when starting new features
3. **Relevant Source**: Only load related files, use line ranges
4. **Error Output**: Full stack traces, not just last line
5. **Conversation**: Summarize for cross-session continuity

## Strategies
- Selective Include (preferred): only relevant files
- Hierarchical Summary: summary first, details on demand

## Anti-Patterns
- Loading entire codebases
- Stale documentation
- Truncated error context
