# Pretrain and Evaluate

Full TDV (or JEPA-style) pretrain → downstream MOT detection/track → smoke-stratified eval on CholecTrack20.

## 0. Setup
```bash
cd /home/aimsgroupuol/AIMSgeneral/Gyanateet_tracking
conda activate surgi_track
export XFORMERS_DISABLED=1
```

## 1. Stage 0 / TDV pretrain (or GOT-JEPA)
- Configure `configs/train_mot/dinov2/tdv-pretrain.yaml` (or stage2 JEPA config).
- Smoke: edit `max_steps: 2`, run locally or 1-GPU srun.
- Full: use `jobs/tdv-pretrain.slurm` or `sbatch` variant.
- Monitor with WandB + `seff`.
- Output: `outputs/tdv_pretrain/tdv_frame_encoder.pth` (and full checkpoints).

Apply skills: `tdv-pretrain`, `wandb-experiment`, `aire-slurm-submit`.

## 2. Stage 1 supervised teacher (detector_only)
Point detection config at the pretrained encoder:
```yaml
encoder_checkpoint: outputs/tdv_pretrain/tdv_frame_encoder.pth
detector_only: true
```
Run Stage 1 (see `mot-training-workflow` or `scripts/train_stage1_ddp_3gpu.sh`).

Target: decent pseudo-label quality (mAP@50 on val > ~0.25–0.30).

## 3. Stage 2–4 MOT training
Follow the 4-stage pipeline in `mot-training-workflow` skill.
Typical chain:
- Stage 2 (SSL/JEPA) loads Stage 1 checkpoint.
- Stage 3 joint loads Stage 2.
- Stage 4 lean loads Stage 3 (recommended for final).

## 4. Evaluation (leak-free + stratified)
```bash
python scripts/eval_checkpoint.py --mot-eval --stratify-smoke \
  --checkpoint outputs/mot/<run>/best.pth.tar

python scripts/eval_mot_hota.py --checkpoint outputs/mot/<run>/best.pth.tar
```
Never eval on pretrain-overlap videos.

Key targets (lean pipeline):
- mAP@50 improvement ≥ 3–5 points vs vanilla DINOv2 baseline.
- MOTA ≥ 5 point lift.
- Per-tool AP stable (no tool collapses).
- HOTA reasonable after birth/min_hits tuning if needed.

## 5. Ablation discipline
- Record exact commit, config hash, data split version.
- Use WandB groups for matched runs.
- Document in `experiments/<slug>/README.md`.

## 6. Verification gate
- Smoke train + eval must pass.
- `pytest tests/test_mot_smoke.py -q`.
- Targeted metrics table in PR or notes.

Apply skills: `surgical-mot-eval`, `tdv-pretrain`, `ablation-study`, `reproducibility`, `data-management`.

See also: `paper-code-release` when preparing artifacts for publication.
