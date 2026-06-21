# MOT Train / Eval

Apply `mot-training-workflow` skill.

```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track
export XFORMERS_DISABLED=1
```

Ask which stage (1–4) or eval target, then run the matching script from `scripts/` and verify with `pytest tests/test_mot_smoke.py`.
