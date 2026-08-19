# Spatial Transcriptomics on GPU

## Description

Cell segmentation, transcript assignment, BIDCell, segger, PanoSpace, and foundation models for spatial omics.

## When to use

You are processing imaging-based spatial transcriptomics (Xenium, CosMx, MERFISH, Stereo-seq) on GPU.

## Key concepts

- **Cell segmentation**: BIDCell (self-supervised), segger (GNN), CellSAM (foundation).
- **Transcript assignment**: assign mRNA spots to cells.
- **GNNs**: heterogeneous graph of transcripts and cells.
- **Integration**: combine with scRNA-seq for cell typing.

## Code pattern

```python
import torch
# segger example
from segger import SeggerData, Segger

dataset = SeggerData(...)
model = Segger(...)
model.fit(dataset)
```

## Tuning notes

- Requires 12-32GB GPU memory depending on tissue complexity.
- Use cell morphology and cell-type priors in loss functions.
- Downstream: cell-type deconvolution, neighborhood analysis.

## Verification

1. Segment a Xenium or CosMx sample and compare to manual annotations.
2. Count transcripts per cell and check distribution.
3. Integrate with scVI/scRNA-seq and confirm cell-type consistency.

## References

- https://github.com/sydneybiox/bidcell/
- https://github.com/dpeerlab/segger
- https://github.com/hehuifeng/PanoSpace-core
- https://cellsam.deepcell.org/
