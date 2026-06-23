# Code Review

Systematic ML-focused code review for surgical video / MOT / pretraining changes.

## Preparation
1. `git diff main...HEAD` or review the PR diff.
2. Read relevant skill(s): `surgical-mot-eval`, `tdv-pretrain`, `debug-pytorch-gpu`, `lora-finetune`, `wandb-experiment`.
3. Note changed files and map to pipeline stages (detection, tracking, ReID, pretrain, data).

## ML correctness checklist
- Tensor shapes and dtypes match across model, dataloader, loss.
- EMA teacher updated under `torch.no_grad()` and `model.ema_update()` called.
- No data leakage: CT20 test videos (VID01,06,07,12,25,39,92,111) and val (VID30,110) never appear in SSL pretrain or training.
- Tracker config (birth_score, min_hits, max_age) appropriate; no hard-coded magic numbers without comment.
- Loss weights and schedules match the paper/config intent.
- DDP: `find_unused_parameters` only if justified; barriers before eval; rank-0 only logging.

## Performance & efficiency
- GPU util >70% on `seff <JOBID>` or `nvidia-smi`.
- No unnecessary `.item()` / `.cpu()` in hot loops.
- Use `torch.compile` or `torch.backends.cudnn.benchmark` where safe.
- Batch size / grad accumulation balanced for available VRAM (GB10: 24–32 for Stage 1 ViT-S; L40S DDP 3–4×).
- Parallelism: dataloaders use `num_workers`, prefetch; consider `PersistentDataLoader`.

## Safety & hygiene
- No secrets, tokens, or absolute local paths in code/configs committed.
- `requirements*.txt` or `pyproject.toml` pinned for reproducibility (major versions at minimum).
- Debug prints, pdb, and commented-out code removed.
- Type hints on public APIs; docstrings for classes and key functions.
- Configs have sensible defaults; no required fields that break smoke tests.

## Testing
- Run `pytest tests/test_mot_smoke.py -q` (or the narrowest impacted tests).
- If training change: run 2–5 step smoke with `--max_steps 5` or equivalent before claiming done.
- For eval changes: run stratified smoke eval and inspect per-tool AP and failure cases.

## Output format
Summarize findings strictly as:

**Critical bugs** (must fix before merge)
- ...

**Improvements** (should fix)
- ...

**Suggestions** (nice to have)
- ...

Reference the verification gate rule: targeted checks must pass before marking complete.

## Related
- Skill: `review-bugbot`, `review`
- Command: `/address-pr-comments` after fixes
- Full research/SWE cross reference: see `reproducibility`, `code-quality`, `testing-strategy` skills.
