---
name: code-review
description: ML-focused code review checklist covering correctness, performance, safety, and style for surgical video, MOT, pretraining, and related research code. Use for PRs, branches, or before merging.
---

## Code Review for ML Research (Surgical Video / MOT focus)

### Core principles
- Correctness first (shapes, no leaks, proper EMA, loss semantics).
- Performance second (GPU util, no Python hot loops, DDP efficiency).
- Safety & reproducibility (no secrets, pinned deps, config capture, verification gate).
- Clarity (no debug left, good names, docs on public surface).

### High-signal checks
- **Data leakage**: CT20 test/val videos excluded from any pretraining or training that feeds the reported numbers.
- **EMA & no_grad**: teacher updates must be under no_grad; `ema_update()` must be called.
- **Tracker config**: birth_score / min_hits / max_age explained; not magic numbers.
- **Checkpoint hygiene**: training-only state (optimizer, scaler, ema) stripped before deployment artifacts.
- **Logging**: WandB config logged fully; rank-0 only in DDP; step passed explicitly.

### Quick commands to run during review
```bash
git diff main...HEAD --name-only
pytest tests/test_mot_smoke.py -q
python -m core_app.mot.main --fname <config> --max_steps 2   # smoke
```

### Output
Use the structured format from the `/code-review` command:
Critical bugs / Improvements / Suggestions.

See also: `reproducibility`, `code-quality`, `testing-strategy`, `debug-pytorch-gpu`.
