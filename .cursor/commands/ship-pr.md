# Ship PR

Ship local work end-to-end: verify tests, commit, push, open or update PR, watch CI.

Apply skills: `ship-pr`, `iterative-test-loop`, `ci-watcher`, `babysit-pr`.

1. `git status` and `git diff` — no secrets in diff.
2. Run targeted tests (`impact-aware-testing` or project default).
3. Commit only when user asked; use conventional commit message.
4. `git push -u origin HEAD` and `gh pr create` or update existing PR.
5. Watch CI until green or report failures with links.

Full skill: `~/.cursor/skills/ship-pr/SKILL.md` (or install from agent-skills personal bundle).
