---
name: endosight-3d-pipeline
description: Endosight 3D reconstruction pipeline (BFF + frontend) for clinical polyp video clips. Canonical root, mesh quality practices, sizing from fused point cloud, and verification.
---

## Endosight 3D

### Canonical location
`/home/aimsgroupuol/endosight-3d/`

- `backend/` : pipeline (reconstruction, BFF on :8000)
- `frontend/` : Leeds React UI (Vite :5173)
- `make dev` starts both.

### Key facts (from AGENTS)
- Clinical sizing from fused point cloud, not display mesh.
- Prefer Poisson surface (BPA only as fallback).
- Tail mode ~6 frames, ~2k–6k points typical.
- Viewer: `http://localhost:5173/elements/modelviewer?...`
- Login demo: admin@leeds.com / admin123

### Verification
`cd endosight-3d && ./scripts/verify.sh` (9 pytest tests).

### Do not
- Conflate mesh vertex count with clinical sizing metric.
- Use legacy 3d_reconstruction or leeds-3dgi-react-frontend as primary (they are symlinks or historical).

Related: `3d-reconstruction-best-practices`.
