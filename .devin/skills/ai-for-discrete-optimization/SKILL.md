# AI for Discrete Optimization

## Description

Learning-augmented branch-and-bound, primal heuristics, GNNs for combinatorial optimization, and data-driven algorithm configuration.

## When to use

You need to solve combinatorial optimization problems such as scheduling, routing, packing, or integer programming and want to use ML to speed up exact or heuristic solvers.

## Key concepts

- **Branch-and-bound learning**: branching, node selection, cutting planes, and primal heuristics.
- **Graph neural networks for CO**: encode combinatorial structure as graphs and learn policies.
- **Imitation and reinforcement learning**: learn construction or improvement heuristics.
- **Algorithm configuration**: use historical data to tune solver parameters.

## Code pattern

```python
import torch
import torch.nn.functional as F
from torch_geometric.nn import GCNConv

# GNN that scores nodes/edges for a combinatorial decision
class COGNN(torch.nn.Module):
    def __init__(self, in_channels, hidden_channels):
        super().__init__()
        self.conv1 = GCNConv(in_channels, hidden_channels)
        self.conv2 = GCNConv(hidden_channels, hidden_channels)
        self.score = torch.nn.Linear(hidden_channels, 1)

    def forward(self, x, edge_index):
        x = F.relu(self.conv1(x, edge_index))
        x = F.relu(self.conv2(x, edge_index))
        return self.score(x).squeeze(-1)

# Score candidate nodes for branching
scores = model(node_features, edge_index)
next_node = int(torch.argmax(scores))
```

## Tuning notes

- Use strong OR baselines (SCIP, Gurobi, CP-SAT) to evaluate ML additions.
- Distinguish between pure learned solvers and learned heuristics inside exact solvers.
- Reward functions in RL must account for solver time, not just solution quality.

## Verification

1. Train a GNN branching policy and compare branch-and-bound nodes to SCIP defaults.
2. Learn a primal heuristic for a routing problem and benchmark against LKH or OR-Tools.
3. Run algorithm configuration (e.g., SMAC) and compare cross-validated solver runtimes.

## References

- https://doi.org/10.1016/j.ejor.2020.07.063
- https://doi.org/10.48550/arxiv.2601.10583
- https://ojs.aaai.org/index.php/AAAI/article/view/26810
- https://jmlr.org/papers/volume24/21-0449/21-0449.pdf
- https://link.springer.com/article/10.1007/s10107-024-02130-y
