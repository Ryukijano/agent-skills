# MOT HOTA Eval

Run HOTA (and smoke-stratified MOT metrics) for surgical tool tracking on CholecTrack20.

## 1. Env
```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track
export XFORMERS_DISABLED=1
```

## 2. Choose checkpoint
Prefer Stage 3 or Stage 4 lean final `best.pth.tar`.

## 3. Run stratified MOT eval (primary)
```bash
python scripts/eval_checkpoint.py --mot-eval --stratify-smoke \
  --checkpoint outputs/mot/<run>/best.pth.tar
```
This produces per-smoke-level and overall mAP/MOTA/MOTAP + per-tool AP.

## 4. Full HOTA (TrackEval style)
```bash
python scripts/eval_mot_hota.py --checkpoint outputs/mot/<run>/best.pth.tar
```
If zero tracks:
- Lower `birth_score` (e.g. 0.4 → 0.2)
- Reduce `min_hits` (2 or 1)
- Increase `max_age` temporarily

Re-run and record tuned params.

## 5. Leak check
Confirm eval videos do not intersect pretrain corpus (see `surgical-mot-eval`).

## 6. Record & compare
- Log to WandB under the run.
- Table: baseline vs this run (mAP@50, MOTA, IDF1, HOTA).
- Note any tool with AP < 0.15 — investigate data or capacity.

Apply `surgical-mot-eval`, `mot-training-workflow`.

Verification: `pytest tests/test_mot_smoke.py -q` after changes to eval code.
