# ESD forward dynamics

Run Cosmos3 forward dynamics for ESD using pretrained camera_pose + ESD seed frame.

1. Read `datasets/esd/ACTION_DOMAIN.md` and `workflows/devin/cosmos-esd-actions.devin.md`.
2. Confirm NATTEN: `source /home/aimsgroupuol/AIMSgeneral/venv/cosmos3-spark/bin/activate && python -c "import natten"`.
   - If missing, tell user to run `/cosmos-spark-kernels` first.
3. Regenerate actions: `python /home/aimsgroupuol/AIMSgeneral/scripts/generate_esd_scope_actions.py`.
4. Run:
   ```bash
   /home/aimsgroupuol/AIMSgeneral/scripts/run_cosmos3_actions_spark.sh forward_esd
   ```
5. Report `outputs/omni_actions/action_forward_dynamics_esd_spark/vision.mp4` and `status` in `sample_outputs.json`.

Use `forward_esd` (camera_pose) unless user explicitly wants untrained `forward_esd_domain`.
