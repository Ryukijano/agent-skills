# Cosmos3 on DGX Spark Workflow

1. SSH to spark-1240 (or via configured host).
2. `cd /home/aimsgroupuol/AIMSgeneral`
3. Activate `venv/cosmos3` (source the activate or use full path).
4. Run verify: `scripts/verify_cosmos3_spark.sh`.
5. For ESD action forward: ensure NATTEN present; regenerate scope if needed; launch `scripts/run_cosmos3_actions_spark.sh forward_esd`.
6. Inspect outputs (vision.mp4 + sample_outputs.json).
7. For new experiments: read `DGX_SPARK_SETUP.md` and relevant devin playbooks first.
8. Report exact command + output path + status.

Apply `dgx-spark-cosmos3`, read `AGENTS.md`.
