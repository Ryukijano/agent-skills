---
name: 3d-reconstruction-best-practices
description: Best practices for clinical 3D reconstruction from endoscopic video (Endosight / polyp pipeline). Focus on point cloud fusion, surface reconstruction choice (Poisson vs BPA), sizing from fused cloud, and viewer considerations.
---

## 3D Reconstruction Best Practices

### Pipeline preference
- One main-process upload + recon flow (POST /api/v1/reconstruct/upload) for offline clinical work.
- Tail clips: 6 frames recommended.
- Fused point cloud is the source of truth for clinical polyp sizing.

### Surface
- Prefer Poisson reconstruction first.
- Use BPA only if too sparse or explicitly requested (`prefer_ball_pivot`).
- Post-process: distance crop + bounds crop (margin ~0.06), largest component, Taubin smooth (6 iters), k-NN weighted vertex paint.

### Viewer
- MeshLambertMaterial with vertexColors, DoubleSide.
- Proper lighting (Hemisphere + Directional).
- computeVertexNormals if missing.
- Toggle between mesh and point cloud in UI.

### Verification
Run the project's verify script (9 tests historically in endosight-3d).

Related: `endosight-3d-pipeline`.
