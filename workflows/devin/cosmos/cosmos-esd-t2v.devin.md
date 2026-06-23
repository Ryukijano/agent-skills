# ESD / surgical synthetic video (Cosmos3 T2V)

**Macro:** `!cosmos-esd-t2v`

## Procedure

### Setup
- `BASE=/home/aimsgroupuol/AIMSgeneral`
- `source $BASE/venv/cosmos3/bin/activate`
- `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`
- Read prompt catalog: `inputs/prompts/esd_public_datasets.json`, `datasets/esd/README.md`.

### Choose prompt
- **ESD dissection (dark + blood):** `inputs/prompts/endoscopy_esd_submucosal_dissection_t2v_v2.json`
- **ESD injection lift:** `inputs/prompts/endoscopy_esd_injection_lift_t2v_v2.json`
- **Laparoscopy:** `inputs/prompts/surgical_laparoscopy_t2v_v2.json`

### Generate
- Run T2V (adjust `--seed` / output as needed):
  ```bash
  python $BASE/scripts/run_cosmos3_t2v_spark.py \
    --prompt-file $BASE/inputs/prompts/endoscopy_esd_submucosal_dissection_t2v_v2.json \
    --output $BASE/outputs/esd/submucosal_dissection_v2_seed${SEED}.mp4 \
    --negative-prompt "laparoscopic, pneumoperitoneum, overexposed, blown highlights, blood spray, arterial jet, gore, cartoon, CGI" \
    --height 480 --width 480 --num-frames 81 \
    --num-inference-steps 35 --fps 16 --seed 42 --guidance-scale 5.5
  ```
- Or batch: `ESD_PROMPT_VERSION=v2 $BASE/scripts/run_esd_dataset_spark.sh`

### QA
- `ffprobe` duration and resolution on output mp4.
- Extract one mid-frame with ffmpeg for visual check.

### Delivery
- Output path(s), seed, prompt file used, ffprobe summary.
- Note if clip is too bright (lower guidance to 5.0) or blood too weak (iterate prompt v3).

## Specifications

- Video is 480×480, ~5s at 16 fps (81 frames), saved under `outputs/esd/` or user path.
- Negative prompt excludes laparoscopy vignette and gore spray.
- Uses Diffusers `Cosmos3OmniPipeline` — no NATTEN required.

## Advice

- Rectangular endoscopy framing — negative prompt must block **circular laparoscope vignette**.
- v2 prompts target **dim lighting** and **controlled ooze** (not arterial spray).
- Do not auto-download Renji Figshare datasets (100–500 GB); user must approve.

## Forbidden actions

- Do not use `~/workspace` paths.
- Do not start Figshare downloads without explicit user request.

## Required from user

- Target phase: dissection | injection | laparoscopy.
- Optional: seed list for a small dataset batch.
