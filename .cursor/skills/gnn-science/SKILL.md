# Graph Neural Networks for Science

## Description

GNNs for molecules, materials, weather, neural operators, and large-scale graph training on GPU.

## When to use

You are working with graph-structured scientific data: molecules, crystals, meshes, point clouds, or spatiotemporal grids.

## Key concepts

- **Message passing**: MPNN, GCN, GAT, SchNet, DimeNet, GemNet.
- **GraphCast**: mesh-based GNN for global weather forecasting.
- **GNNs for MD**: MACE, NequIP, Allegro, GemNet-OC.
- **Large-scale training**: PyTorch Geometric, DGL, GraphStorm, whole-graph training.
- **Heterogeneous graphs**: different node/edge types (e.g., spatial transcriptomics, knowledge graphs).

## Code pattern

```python
import torch_geometric
from torch_geometric.nn import GCNConv

class GCN(torch.nn.Module):
    def __init__(self, in_channels, out_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, 64)
        self.conv2 = GCNConv(64, out_channels)

    def forward(self, x, edge_index):
        x = self.conv1(x, edge_index).relu()
        return self.conv2(x, edge_index)
```

## Tuning notes

- Use `edge_index` (COO) for small graphs; `SparseTensor` or DGL for large graphs.
- Add self-loops and normalize adjacency.
- For equivariant molecular graphs, prefer equivariant GNNs over plain GCN.

## Verification

1. Train GCN on QM9 for a property and check MAE.
2. Run a GraphCast inference on a single time step and compare to IFS.
3. Benchmark PyG vs DGL on a large graph.

## References

- https://pytorch-geometric.readthedocs.io/
- https://www.dgl.ai/
- https://github.com/google-deepmind/graphcast
- https://www.nature.com/articles/s41467-022-29939-5
