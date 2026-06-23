---
name: mot-repo-orientation
description: >-
  Orients agents to Gyanateet_tracking repo layout, MOT pipeline entry points,
  and key files. Use when the user asks to understand the repo, explore the
  codebase, or plan work with @Browser.
---

# MOT Repo Orientation

## Root

`/home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking`

## Architecture (four stages)

```
Stage 1: DETR teacher (supervised, detector_only)
    ↓ checkpoint
Stage 2: GOT-JEPA SSL (frozen teacher → student ω predictor)
    ↓ checkpoint
Stage 3: Joint MOT finetune (det + track + reid)
    ↓ checkpoint
Stage 4: OccuSolver + optional geometry (lean = CoTracker + depth)
```

## Key paths

| Path | Role |
|------|------|
| `core_app/mot/main.py` | Training CLI entry |
| `core_app/mot/trainer.py` | Stage dispatch, checkpoints |
| `core_app/mot/system.py` | `SurgicalMOTSystem` |
| `core_app/mot/jepa.py` | GOT-JEPA wrapper |
| `core_app/mot/occusolver.py` | CoTracker + visibility |
| `core_app/mot/geometry.py` | VGGT + null-space (Stage 4 full) |
| `core_app/mot/eval.py` | HOTA, smoke stratification |
| `core_app/data/splits.py` | CT20 train/val/test splits |
| `configs/train_mot/dinov2/` | Stage YAML configs |
| `scripts/` | Shell launchers + eval |
| `data/cholectrack20` | Local CT20 |
| `outputs/mot/` | Checkpoints |

## Diagram layers vs stages

- ② Gating (CoTracker + OccuSolver) → Stage 4
- ④ JEPA → Stage 2
- ⑤ Geometry (VGGT) → Stage 4 full only
- ⑥ DETR/localization → Stage 1 + 3

## Data rules

- SSL corpus: Cholec80 minus CT20 val/test overlap videos (`video01,06,07,12,25,30,39`)
- Cholec80 native labels = tool presence, not MOT boxes

## Exploration checklist

When `@Browser` + repo understanding is requested:

1. Read `AGENTS.md` and `agent_docs/cursor_explore_mot_training_pipeline.md`
2. Skim `core_app/mot/main.py` and `trainer.py` stage branches
3. List configs under `configs/train_mot/dinov2/`
4. Check `outputs/mot/` for latest checkpoints
5. Run `pytest tests/test_mot_smoke.py` if verifying infra

## Do not pivot without user approval

- VLA-JEPA robot policies
- Bulk Renji ESD downloads
- Replacing GOT-JEPA with unrelated world models
