# ESD forward dynamics (Cosmos3 action modes)

**Macro:** `!cosmos-esd-actions`

## Procedure

### Setup
- `BASE=/home/aimsgroupuol/AIMSgeneral`
- Confirm NATTEN installed: `venv/cosmos3-spark` (or `cosmos3` if wheels installed there).
- Read `datasets/esd/ACTION_DOMAIN.md`.

### Prerequisites check
- `source $BASE/venv/cosmos3-spark/bin/activate` (fallback: `venv/cosmos3`)
- `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- `export I4_ATTN_BACKENDS=sdpa`
- `python -c "import natten; print('ok')"` — if fail, run `!cosmos-spark-kernels` playbook first.

### Regenerate scope actions
- `python $BASE/scripts/generate_esd_scope_actions.py` → `inputs/action/esd_scope_action_16.json`

### Run forward dynamics (zero-shot, recommended)
- `$BASE/scripts/run_cosmos3_actions_spark.sh forward_esd`
- Uses `domain_name: camera_pose` + ESD seed frame `inputs/action/esd_frame0_v2.png`.

### Optional: reserved ESD domain (untrained)
- `$BASE/scripts/run_cosmos3_actions_spark.sh forward_esd_domain`
- Uses `esd_endoscope` (domain id 9) — expect poor quality until fine-tuned.

### Delivery
- Output: `outputs/omni_actions/action_forward_dynamics_esd_spark/vision.mp4`
- Paste `status` from `sample_outputs.json`.
- Compare briefly to pure T2V: `outputs/esd/submucosal_dissection_v2.mp4`.

## Specifications

- Inference exits 0; `sample_outputs.json` has `"status": "success"`.
- `vision.mp4` exists under `outputs/omni_actions/action_forward_dynamics_esd_spark/`.
- Config uses fps **16** (within recommended 10–30), 256×256, 25 frames.

## Advice

- **camera_pose** is the only viable zero-shot domain for ESD scope motion today.
- `esd_endoscope` slot is registered in `cosmos-framework/.../domain_utils.py` for future SFT.
- 9D actions = translation(3) + rot6d(6); damped from `camera_action_44.json`.
- Checkpoint name for framework CLI: `Cosmos3-Nano` (not `nvidia/Cosmos3-Nano`).

## Forbidden actions

- Do not assume `esd_endoscope` works without fine-tuning.
- Do not commit secrets or HF tokens.

## Required from user

- Confirm `venv/cosmos3-spark` exists with natten, or permission to build kernels.
- Optional: custom ESD seed image path to replace `esd_frame0_v2.png`.
