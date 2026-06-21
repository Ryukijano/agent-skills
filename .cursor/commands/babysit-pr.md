# Babysit PR

Keep a PR merge-ready: triage comments, resolve conflicts, fix CI in a loop.

Apply skills: `babysit-pr`, `fix-ci`, `address-pr-comments`.

1. `gh pr view` and fetch review comments.
2. Address or defer each comment with evidence.
3. Resolve merge conflicts if present; re-run tests.
4. Push until CI is green or report blockers.

Pair with `/address-pr-comments` for systematic comment handling.
