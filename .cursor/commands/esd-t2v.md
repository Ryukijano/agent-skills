# ESD T2V (Cosmos3 synthetic)

Generate synthetic endoscopic submucosal dissection (or related) video with Cosmos3-Nano T2V.

1. Read `workflows/devin/cosmos-esd-t2v.devin.md` and `inputs/prompts/esd_public_datasets.json`.
2. Ask user which phase if unclear: **dissection v2** | **injection v2** | **laparoscopy v2**.
3. Activate `source /home/aimsgroupuol/AIMSgeneral/venv/cosmos3/bin/activate`.
4. Set `export PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True`.
5. Run generation (default dissection v2, seed 42):
   ```bash
   python /home/aimsgroupuol/AIMSgeneral/scripts/run_cosmos3_t2v_spark.py \
     --prompt-file /home/aimsgroupuol/AIMSgeneral/inputs/prompts/endoscopy_esd_submucosal_dissection_t2v_v2.json \
     --output /home/aimsgroupuol/AIMSgeneral/outputs/esd/submucosal_dissection_v2.mp4 \
     --negative-prompt "laparoscopic, pneumoperitoneum, overexposed, blown highlights, blood spray, arterial jet, gore, cartoon, CGI" \
     --height 480 --width 480 --num-frames 81 --num-inference-steps 35 --fps 16 --seed 42 --guidance-scale 5.5
   ```
6. `ffprobe` the output and report path + duration.

Use Diffusers only — no NATTEN required. Do not download Renji datasets unless user asks.
