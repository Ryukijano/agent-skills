# Cosmos3 on DGX Spark — bootstrap & verify

**Macro:** `!cosmos-spark-setup`

## Procedure

### Setup
- SSH to `spark-1240` (`aimsgroupuol@10.41.187.94`) or work locally on the Spark box.
- Set `BASE=/home/aimsgroupuol/AIMSgeneral` — never use `~/workspace` (does not exist).
- Read `DGX_SPARK_SETUP.md` for current layout and checklist.

### Bootstrap
- Run `chmod +x $BASE/scripts/*.sh`.
- Run `$BASE/scripts/bootstrap_cosmos3_spark.sh inference` if `venv/cosmos3` is missing.
- Run `$BASE/scripts/verify_cosmos3_spark.sh` and capture output.
- If weights missing, run `$BASE/scripts/download_cosmos3_weights.sh` (requires `HF_TOKEN` if gated).

### Smoke test (T2V)
- `source $BASE/venv/cosmos3/bin/activate`
- `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- Run `$BASE/scripts/run_cosmos3_t2v_spark.py` with defaults → `outputs/cosmos3_spark_test.mp4`.

### Delivery
- Report: Python/torch/CUDA version, GPU name (expect **NVIDIA GB10**), verify script pass/fail, smoke test output path.
- If failures: paste last 50 lines of log; do not retry bootstrap more than once without diagnosing.

## Specifications

- `torch` is `2.11.0+cu130`, `cuda.is_available()` is True, device is GB10.
- `nvidia/Cosmos3-Nano` loads via Diffusers without error.
- `outputs/cosmos3_spark_test.mp4` exists after smoke test.

## Advice

- GB10 is **aarch64 + sm_121**; do not `pip install` x86 flash-attn/natten wheels.
- Diffusers T2V works **without** kernel compile; framework **action modes** need NATTEN (separate playbook).
- Use `bf16`; 480×480 and 49–81 frames are good defaults for surgical clips.

## Forbidden actions

- Do not clone Cosmos or install venvs under `~/workspace`.
- Do not `git push --force` or change git config.
- Do not download multi-hundred-GB Renji ESD datasets without explicit user approval.

## Required from user

- SSH access to Spark (if remote).
- `HF_TOKEN` if Hugging Face weights are gated.
