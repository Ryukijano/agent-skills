# Fix CI

Find failing PR checks, inspect logs, apply focused fixes.

Apply skills: `fix-ci`, `loop-on-ci`, `iterative-test-loop`.

1. `gh pr checks` or CI watcher for the active branch.
2. Open failing job logs; fix one failure class per iteration.
3. Push and re-check until required checks pass.
