# 3D Recon Best-Practice Pass

1. Confirm input clip meets tail-frame policy (6 frames typical).
2. Run the upload/recon flow; inspect fused cloud metrics.
3. Choose Poisson (default) or note why BPA.
4. Apply post-process (crop, smooth, paint).
5. Open in viewer; confirm sizing comes from cloud, not vertex count of mesh.
6. Run verify suite.
7. Document any deviation in the batch metadata.

Apply `3d-reconstruction-best-practices`, `endosight-3d-pipeline`.
