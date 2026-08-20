# AI for Chip Design

## Description

ML for RTL generation, EDA scripting, floorplanning, placement, routing, timing optimization, and analog/mixed-signal design.

## When to use

You are automating digital or analog IC design tasks, including floorplanning, placement, standard-cell routing, or EDA-tool scripting.

## Key concepts

- **Floorplanning and placement**: deep RL (e.g., AlphaChip) optimizes macro and standard-cell placement for PPA.
- **RTL and EDA scripting**: domain-adapted LLMs (e.g., ChipNeMo) generate Verilog, Tcl, and Python EDA flows.
- **Analog design**: ML surrogate models and Bayesian optimization size transistors and layout cells.
- **Design-space exploration**: multi-objective optimization over architecture, PPA, and manufacturability.

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
