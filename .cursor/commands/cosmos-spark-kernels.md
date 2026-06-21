# Cosmos Spark kernels (NATTEN)

Build and install NATTEN for Cosmos3 framework action inference on GB10.

1. Read `workflows/devin/cosmos-spark-kernels.devin.md` and `DGX_SPARK_SETUP.md`.
2. Confirm `uname -m` is aarch64 and `nvcc --version` works.
3. Run build with log:
   ```bash
   /home/aimsgroupuol/AIMSgeneral/scripts/build_cosmos_spark_kernels.sh \
     2>&1 | tee /home/aimsgroupuol/AIMSgeneral/outputs/build_spark_kernels.log
   ```
4. Run `/home/aimsgroupuol/AIMSgeneral/scripts/install_cosmos_spark_kernels.sh`.
5. Verify `import natten` in `venv/cosmos3-spark`.
6. Smoke test: `run_cosmos3_actions_spark.sh forward_camera`.

Warn user build takes 1–3+ hours. Do not kill an in-progress build without asking.
