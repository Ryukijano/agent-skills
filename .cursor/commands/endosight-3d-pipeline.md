# Endosight 3D Development Flow

1. `cd /home/aimsgroupuol/endosight-3d`
2. `make dev` (or manually start BFF + Vite).
3. For a clinical clip: use `backend/scripts/sweep_clinical_clips.sh Patient_X Polyp_Y`.
4. Inspect mesh in viewer; toggle point-cloud vs mesh.
5. Run verify: `./scripts/verify.sh`.
6. For pipeline changes: read `backend/pipeline/reconstruction/polyp_size.py` and `run_reconstruction_pipeline.py`.
7. Note: sizing comes from fused cloud; mesh is for visualization.

Apply `endosight-3d-pipeline`.
