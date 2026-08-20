# Geospatial and Remote Sensing ML on GPU

## Description

Prithvi, SatMAE, TorchGeo, TerraTorch, segment-anything for Earth observation, and NVIDIA cuOpt.

## When to use

You are training or deploying geospatial foundation models on GPU for satellite/aerial imagery.

## Key concepts

- **Prithvi**: NASA/IBM geospatial foundation model on HLS data; supports temporal and location embeddings.
- **SatMAE**: masked autoencoder on temporal Sentinel-2.
- **TorchGeo**: PyTorch domain library with 100+ CRS-aware datasets, multispectral transforms, pretrained weights.
- **TerraTorch**: fine-tuning framework built on TorchGeo + Lightning for GFMs.
- **SamGeo**: Segment Anything for GeoTIFF/TMS data.
- **cuOpt**: GPU VRP/TSP/PDPTW solver with RAPIDS cuDF.

## Code pattern

```python
import torchgeo
from torchgeo.trainers import SemanticSegmentationTask
from torchgeo.datasets import EuroSAT

# Use a pretrained Prithvi or DOFA backbone
```

For TerraTorch:

```bash
pip install terratorch
```

## Tuning notes

- Chunk size and I/O are usually the bottleneck; use Zarr/COG/Tar streaming and many DataLoader workers.
- Multispectral input may require 6/13 channels, not 3.
- Use `bfloat16` for fine-tuning; keep normalization in FP32.

## Verification

1. Run a small EuroSAT or So2Sat classification benchmark.
2. Fine-tune Prithvi on a flood/wildfire segmentation task and compare IoU.
3. Profile data loading vs compute with Nsight Systems.

## References

- https://torchgeo.org/
- https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M
- https://samgeo.gishub.org/
- https://docs.nvidia.com/cuopt/
- https://arxiv.org/abs/2412.02732v3
