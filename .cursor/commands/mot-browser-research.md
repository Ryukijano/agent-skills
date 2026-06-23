# MOT Browser Research

Use browser + web search to answer MOT / surgical video / tracking questions and map back to this repo.

## 1. Context first
Read `AGENTS.md` (current status, known blockers) and `mot-repo-orientation` skill.

## 2. Query
Use web search or `@web` for:
- Recent SOTA on surgical tool tracking / CholecTrack20
- GOT-JEPA / OccuSolver variants
- DINOv2 + temporal adaptation papers 2024–2026
- Tracker hyperparameters for low-FPS or smoky scenes

## 3. Map to pipeline
Explicitly say which stage (1–4) or component (ReID, motion, depth, tracker gates) would be affected.

## 4. Verdict
Give a short strategic recommendation with citations (title + year + venue or arXiv). Flag if it would require major refactor.

## 5. Constraints
- Prefer keeping GOT-JEPA + OccuSolver core unless user explicitly wants to pivot.
- Always note data leakage risks for any new pretraining data sources.

Apply skill: `mot-browser-research`, `mot-repo-orientation`.

Cross-reference `explore-sota` and `claim-verification` for deeper literature work.
