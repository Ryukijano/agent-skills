# Build Cosmos Spark kernels (NATTEN) on GB10

**Macro:** `!cosmos-spark-kernels`

## Procedure

### Setup
- Confirm host is DGX Spark aarch64: `uname -m` → `aarch64`, GPU → GB10.
- Set `BASE=/home/aimsgroupuol/AIMSgeneral`.
- Ensure `cosmos-dependencies/` is cloned under `$BASE`.
- Read `DGX_SPARK_SETUP.md` § Spark kernel build.

### Build
- Run build with logging (1–3+ hours):
  ```bash
  $BASE/scripts/build_cosmos_spark_kernels.sh \
    2>&1 | tee $BASE/outputs/build_spark_kernels.log
  ```
- Confirm wheels appear in `$BASE/cosmos-dependencies/wheels/*.whl`.

### Install
- Run `$BASE/scripts/install_cosmos_spark_kernels.sh`.
- Activate `source $BASE/venv/cosmos3-spark/bin/activate`.
- Verify: `python -c "import natten, torch; print(natten.__version__, torch.cuda.get_device_name(0))"`.

### Smoke test (actions)
- Run `$BASE/scripts/run_cosmos3_actions_spark.sh forward_camera`.
- Confirm `outputs/omni_actions/action_forward_dynamics_camera_spark/vision.mp4` and `status: success` in `sample_outputs.json`.

### Delivery
- List built wheels with sizes.
- Report forward_camera success/failure and any attention-backend errors.

## Specifications

- `natten` imports successfully in `venv/cosmos3-spark`.
- `build_cosmos_spark_kernels.sh` sets `TORCH_CUDA_ARCH_LIST=12.0` for sm_121 forward-compat.
- Framework inference completes sampling without "Could not find a compatible Attention backend".

## Advice

- Build uses **Python 3.11** to match `venv/cosmos3` unless user overrides `PYTHON_VERSION`.
- `CUDA_VERSION` must be set before build (handled in script); if build fails at line 46, check `nvcc --version`.
- SDPA alone is **not** enough for full video action inference — NATTEN is required for multi-dim attention.
- Skip flash-attn on GB10 unless user explicitly needs it; community guidance favors SDPA for generic attention.

## Forbidden actions

- Do not kill long builds without user consent.
- Do not install wrong-architecture wheels from PyPI.

## Required from user

- Disk space (~10GB+ for build tree).
- Acceptance of 1–3 hour build time.
