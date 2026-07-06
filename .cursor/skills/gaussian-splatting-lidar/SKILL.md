# gaussian-splatting-lidar

## Description
LiDAR-augmented Gaussian Splatting for geometrically consistent photorealistic rendering and high-quality 3D reconstruction. Combines dense LiDAR depth priors with 3D Gaussian Splatting to overcome the geometric limitations of pure vision-based splat methods.

## Key Papers & Repos (July 2026)
- **GS-SDF**: LiDAR-Augmented Gaussian Splatting and Neural SDF - https://github.com/hku-mars/GS-SDF
- **LiDAR + Gaussian Splatting Field Guide**: https://lidarnews.com/gaussian-splatting-and-lidar-a-practitioners-field-guide/
- **SuperFlex** (SuperQuadrics @ ECCV 2026): https://superflex3d.github.io
- **SLAM Handbook** (factor graphs for world models): https://github.com/SLAM-Handbook-contributors
- **RayRoPE** (multi-view transformers, positional encoding): https://rayrope.github.io
- **IronSight** (4D reconstruction from Meta Ray-Bans)
- **FoundObj** (ICML 2026, self-supervised 3D scene segmentation): arXiv:2605.27178

## Architecture: GS-SDF
```
LiDAR Point Cloud ----> Depth Priors
                           |
                           v
RGB Images ---------> 3D Gaussian Splats (initialized with LiDAR)
                           |
                    Gaussian Pruning &
                    Densification
                           |
                    Neural SDF (signed distance field)
                           |
              Photorealistic Render + Mesh Extraction
```

## When to Use LiDAR-Augmented vs Pure 3DGS
| Scenario | Recommendation |
|---|---|
| Indoor scenes, good cameras | Pure 3DGS sufficient |
| Outdoor, large-scale, autonomous driving | LiDAR-augmented essential |
| Medical endoscopy / surgical scenes | Depth from SfM + monocular depth |
| SLAM loop closure required | LiDAR-augmented + factor graph |
| Photorealism only, no mesh needed | Pure 3DGS |
| Geometric accuracy critical | GS-SDF with neural SDF |

## Setup
```bash
# Clone GS-SDF
git clone https://github.com/hku-mars/GS-SDF
cd GS-SDF

# Install dependencies
pip install -r requirements.txt

# Build LiDAR preprocessing
cmake -B build && cmake --build build

# Run with your data
python train.py --source_path /data/scene --lidar_path /data/scene/lidar
```

## Key Techniques
1. **LiDAR-Initialized Splats**: Use LiDAR point cloud as initialization for Gaussians instead of SfM sparse points
2. **Depth Supervision**: LiDAR depth supervises Gaussian opacity and position during training
3. **Neural SDF Regularization**: Gaussians constrained to lie near the zero-level set of an implicit SDF
4. **Adaptive Densification**: Prune floaters using LiDAR coverage masks
5. **Multi-Return Handling**: Handle LiDAR multi-return for semi-transparent surfaces

## Integration with Endosight Pipeline
```python
# For surgical video / endoscopy scenes (no LiDAR)
# Use monocular depth estimation as proxy for LiDAR
from depth_anything_v2 import DepthAnythingV2

depth_model = DepthAnythingV2()
depth_map = depth_model.predict(frame)  # pseudo-LiDAR

# Then initialize Gaussians from depth map
splat_positions = unproject_depth(depth_map, camera_intrinsics)
gaussians.initialize_from_pointcloud(splat_positions)
```

## Related Skills
- `3d-reconstruction-best-practices` - General 3D reconstruction
- `endosight-3d-pipeline` - Surgical 3D reconstruction
- `vjepa-physics-world-model` - World model for 3D scene prediction

## Tags
gaussian-splatting, lidar, 3dgs, sdf, slam, nerf, 3d-reconstruction, outdoor, autonomous-driving
