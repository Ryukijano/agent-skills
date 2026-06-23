# Cosmos verify on Spark

Run the Cosmos3 Spark verification stack and report results.

1. Read `DGX_SPARK_SETUP.md` and `AGENTS.md` for paths.
2. Run `/home/aimsgroupuol/AIMSgeneral/scripts/verify_cosmos3_spark.sh`.
3. Check GPU: `python -c "import torch; print(torch.__version__, torch.cuda.get_device_name(0))"` in `venv/cosmos3`.
4. Report pass/fail, torch/CUDA/GPU, and whether `nvidia/Cosmos3-Nano` weights are cached.
5. If verify fails, suggest bootstrap: `scripts/bootstrap_cosmos3_spark.sh inference`.

Do not download large datasets or run kernel builds unless the user asks.
