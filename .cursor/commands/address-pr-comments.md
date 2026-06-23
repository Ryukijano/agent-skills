# Address PR Comments

Systematically address review feedback on a PR or branch.

## 1. Checkout & orient
```bash
gh pr checkout <PR_NUMBER>
git pull --rebase origin <branch>
```
Read the PR description and the full diff.

Apply skill: `git-branch-workflow`.

## 2. Triage comments
```bash
gh api repos/:owner/:repo/pulls/<PR_NUMBER>/comments | jq '.[] | {id, path, line, body}'
```
Group into:
- Critical (behavior, correctness, data leak, security)
- Important (perf, testing, clarity)
- Nit / style

Create a local `pr-<number>-tasks.md` checklist.

## 3. Fix loop (one at a time)
For each item:
- Make the minimal change.
- Run the narrowest verification: `pytest ... -q` or smoke train/eval.
- `git add -A && git commit -m "fix: address PR #<n> comment: <short>"`
- Rebase if needed to keep history clean.

Never leave uncommitted state at end of session.

## 4. Push & update
```bash
git push origin <branch>
```
Reply to each resolved comment on GitHub with what was done + link to commit or test output.

## 5. Final checks
- Full `code-review` command on the branch.
- Verification gate: targeted tests + linter pass.
- Update PR description with "All comments addressed" summary if appropriate.

## 6. If blocked
If a comment needs design decision or user input, note it clearly in the task list and in the PR comment. Do not guess.

Apply skills: `git-branch-workflow`, `code-quality`, `code-review`.
