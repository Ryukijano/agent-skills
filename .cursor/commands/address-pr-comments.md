# Address PR Comments

Apply `git-branch-workflow` skill. Systematically address pull request review comments.

1. Check out the PR branch: `gh pr checkout <PR_ID>`
2. Fetch inline comments via `gh api` (see skill for jq filters).
3. Address one comment at a time; run `pytest tests/test_mot_smoke.py -q` after each fix.
4. Commit and push with a descriptive message referencing the PR.

Full procedure: `.windsurf/workflows/address-pr-comments.md`
