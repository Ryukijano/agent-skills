# Laparoscopy T2V (rich v2)

Generate laparoscopic synthetic video with Cosmos3 T2V.

1. Read `inputs/prompts/surgical_laparoscopy_t2v_v2.json`.
2. `source /home/aimsgroupuol/AIMSgeneral/venv/cosmos3/bin/activate`
3. Run:
   ```bash
   python /home/aimsgroupuol/AIMSgeneral/scripts/run_cosmos3_t2v_spark.py \
     --prompt-file /home/aimsgroupuol/AIMSgeneral/inputs/prompts/surgical_laparoscopy_t2v_v2.json \
     --output /home/aimsgroupuol/AIMSgeneral/outputs/laparoscopy_rich_v2.mp4 \
     --height 480 --width 480 --num-frames 81 --num-inference-steps 35 --fps 16 --seed 42 --guidance-scale 6.5
   ```
4. Report output path and ffprobe summary.
