# AI for Chip Design

## Description

Use machine learning to generate RTL, floorplan chips, optimize placement, and assist analog and mixed-signal design.

## When to use

You are automating digital or analog IC design tasks, including floorplanning, placement, standard-cell routing, or EDA-tool scripting.

## Usage

- Optimize macro and standard-cell placement for power, performance, and area with deep RL.
- Generate Verilog, Tcl, and Python EDA flows with domain-adapted code LLMs.
- Size transistors and layout analog cells with Bayesian optimization and surrogates.
- Explore design trade-offs across architecture, PPA, and manufacturability.

## Steps

1. Prepare netlist, constraints, and floorplan input for the target IC block.
2. Train an RL placement agent or a surrogate for analog sizing.
3. Legalize and sign off the placement with commercial EDA tools.
4. Use a code LLM to generate or review synthesis and STA scripts.
5. Verify timing, congestion, DRC, and power-grid constraints.
6. Compare the optimized design to a manual or baseline flow.

## Code pattern

```python
import tensorflow as tf
from circuit_training.learning import ppo_lib

# Policy network inputs a graph netlist and outputs placement coordinates
policy = ppo_lib.PolicyNet(num_actions=128)
```

## Tuning notes

- Use realistic constraints (timing, congestion, DRC, power grid) as reward or loss terms.
- Combine learned placement with commercial EDA legalizers and signoff tools.
- Fine-tune code LLMs on internal EDA scripts and design documentation for safe deployment.

## Verification

1. Generate a chip floorplan with an RL agent and compare wirelength/congestion to a human baseline.
2. Use a domain LLM to write a synthesis/STA Tcl script and run it in a commercial tool.
3. Optimize an analog cell with a learned surrogate and verify performance with SPICE.

## References

- https://doi.org/10.1038/s41586-021-03544-w
- https://github.com/google-research/circuit_training
- https://doi.org/10.48550/arxiv.2311.00176
- https://openroad.readthedocs.io/en/latest/
