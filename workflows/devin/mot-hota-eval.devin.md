# MOT HOTA eval (smoke-stratified)

**Macro:** `!mot-hota-eval`

## Procedure

### Setup
- `BASE=/home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking`
- `conda activate surgi_track`
- Read `AGENTS.md` for latest checkpoint paths.

### Default checkpoints (Jun 2026)
- Stage 3: `outputs/mot/cholec20-stage3-joint-finetune-vits/best.pth.tar`
- Stage 4 lean: `outputs/mot/cholec20-stage4-lean-vits/best.pth.tar`

### Run eval
```bash
cd $BASE
python scripts/eval_checkpoint.py --mot-eval --stratify-smoke \
  --checkpoint outputs/mot/cholec20-stage3-joint-finetune-vits/best.pth.tar

python scripts/eval_mot_hota.py --checkpoint <path>
```

### Tracker tuning
If zero predictions on short clips: lower `birth_score`, reduce `min_hits`.

### Delivery
- Report HOTA, MOTA, smoke-stratified breakdown if available.
- Compare Stage 3 vs Stage 4 lean when both checkpoints exist.

## Verification
- `pytest tests/test_mot_smoke.py -q` if eval code was changed.
