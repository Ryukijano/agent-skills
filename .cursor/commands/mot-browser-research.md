# MOT Browser Research

# MOT browser research (GOT-JEPA surgical tracking)

**Macro:** `!mot-browser-research`

## Procedure

### Setup
- `BASE=/home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking`
- Read `AGENTS.md` for training status, blockers, and checkpoint paths.
- Read `.cursor/skills/mot-browser-research/SKILL.md` and `agent_docs/cursor_repo_understanding.md`.

### Research loop
1. Frame the question: detection, association, smoke/occlusion, SSL, or infra (Spark vs Leeds Aire)?
2. Search online (arXiv, GitHub, dataset pages). Cite every claim.
3. Map findings to stages in `core_app/mot/` and configs in `configs/train_mot/dinov2/`.
4. Strategic verdict: adopt / optional / reject with next concrete step.

### Direction guardrails
- **Stay** GOT-JEPA + OccuSolver unless user explicitly pivots.
- **VLA-JEPA** = robot policies, not MOT — reject as primary path.
- **Desmoking** (Seeing Through Smoke) = optional ablation only.
- **V-JEPA / Cholec_Vjepa-2** = complementary SSL, not replacement for per-track ω prediction.

### Delivery
- Short answer first, comparison table, recommendation, Sources list with markdown links.

## Forbidden actions
- Do not bulk-download Renji ESD datasets.
- Do not pivot architecture without explicit user approval.
