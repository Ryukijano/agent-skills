# Code Review

Systematic ML code review checklist for the current branch or PR.

1. `git diff main...HEAD` — review correctness, performance, safety, style.
2. Check tensor shapes, EMA in `no_grad`, DataLoader settings, no hardcoded secrets.
3. Run `pytest tests/test_mot_smoke.py -q` if tests exist.
4. Summarize: critical bugs, improvements, suggestions.

Full checklist: `.windsurf/workflows/code-review.md` · Skill: `review-bugbot`
