# AI for Cultural Heritage

## Description

Transcribe and restore damaged manuscripts and inscriptions with OCR and lacuna filling to make fragile heritage accessible.

## When to use

You are digitizing, analyzing, or preserving cultural heritage assets such as monuments, artifacts, manuscripts, oral traditions, or historic sites.

## Usage

- Digitize, annotate, and segment heritage assets.
- Extract and link entities, provenance, and temporal metadata.
- Reconstruct damaged or missing regions with inpainting.
- Build knowledge graphs and digital twins.

## Steps

1. Digitize, annotate, and segment heritage assets.
2. Extract and link entities, provenance, and temporal metadata.
3. Reconstruct damaged or missing regions with inpainting.
4. Build knowledge graphs and digital twins.
5. Validate with domain experts and authority files.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
import open3d as o3d
from sklearn.ensemble import IsolationForest

# Load a heritage 3D point cloud and detect anomalous structural regions
pcd = o3d.io.read_point_cloud("heritage_site.ply")
points = np.asarray(pcd.points)
outliers = IsolationForest(contamination=0.05, random_state=42).fit_predict(points)
pcd.colors = o3d.utility.Vector3dVector([
    [1, 0, 0] if x == -1 else [0.7, 0.7, 0.7] for x in outliers
])
```

## Tuning notes

- Heritage data is often scarce and imbalanced; combine domain priors with data augmentation.
- Validate 3D reconstructions against measured ground truth and expert connoisseurship.
- Address bias and provenance in training data, especially for indigenous or contested heritage.

## Verification

1. Digitize a small artifact and compare the 3D model to manual measurements.
2. Train an object classifier on a heritage image corpus and report per-class precision/recall.
3. Forecast microclimate risk for a heritage building and compare to observed degradation.

## References

- https://www.mdpi.com/2072-4292/18/4/628
- https://www.mdpi.com/2071-1050/17/20/9192
- https://www.nature.com/articles/s40494-026-02403-z
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335943
- https://link.springer.com/article/10.1007/s10791-026-10049-5
