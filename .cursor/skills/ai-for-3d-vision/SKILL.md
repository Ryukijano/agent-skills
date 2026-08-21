# AI for 3D Vision

## Description

Use AI for 3D Vision to reconstruct scenes, process point clouds and estimate depth.

## When to use

You need to reconstruct, represent, or interpret 3D geometry from images, point clouds, or depth sensors.


## Usage


- **Point cloud deep learning**: PointNet, PointNet++, DGCNN, and Point Transformer.
- **Neural radiance fields and 3D Gaussian splatting**: Implicit and explicit scene representations.
- **Depth estimation**: Monocular and stereo depth and completion.
- **3D object detection and segmentation**: VoteNet, PointRCNN, and 3D instance segmentation.
- **Surface reconstruction and registration**: Traditional and learning-based methods.

## Steps

1. Collect and prepare multi-view images, point clouds and depth maps.
2. Reconstruct.
3. Represent.
4. Interpret 3D geometry from images.
5. Validate by reconstructing a small object from multi-view images with NeRF or Gaussian splatting and render novel views.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import open3d as o3d

pcd = o3d.io.read_point_cloud("scene.ply")
pcd.estimate_normals(
    search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30)
)
o3d.io.write_point_cloud("scene_normals.ply", pcd)
```


## Tuning notes

- Normalize point clouds and handle varying density.
- Use multi-view consistency for depth and reconstruction.
- Combine geometric and photometric cues.
- Validate with Chamfer distance, F-score, or mAP on 3D benchmarks.


## Verification

1. Reconstruct a small object from multi-view images with NeRF or Gaussian splatting and render novel views.
2. Segment or classify a point cloud and report mIoU or accuracy.
3. Estimate depth from a monocular image and compare to ground truth.

## References

- https://arxiv.org/abs/2210.00379
- https://doi.org/10.1007/s00371-023-03237-7
- https://arxiv.org/abs/2306.03000
- https://arxiv.org/abs/2301.13656
- https://arxiv.org/abs/2404.00714
