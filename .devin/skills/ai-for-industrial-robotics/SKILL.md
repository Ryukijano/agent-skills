# AI for Industrial Robotics

## Description

Machine learning for factory manipulation, assembly, pick-and-place, force control, sim-to-real, and vision-language-action models in industrial settings.

## When to use

You are automating precision assembly, cable routing, bin picking, or contact-rich tasks in a manufacturing cell.

## Key concepts

- **Industrial dexterity and manipulation**: end-to-end imitation and diffusion policies, force/torque and tactile feedback.
- **Sim-to-real transfer**: domain randomization, teacher-student distillation, and synthetic datasets.
- **Vision-language-action (VLA) models**: grounding natural-language instructions in robot policies.
- **Multimodal datasets and benchmarks**: PRISM, Industrial Dexterity Benchmark, and factory-relevant skills.

## Code pattern

```python
import torch
import torch.nn as nn

# Simple end-effector force-guided policy network
class ForcePolicy(nn.Module):
    def __init__(self, in_dim=7, out_dim=6):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, 64), nn.ReLU(),
            nn.Linear(64, out_dim)
        )

    def forward(self, x):
        return self.net(x)
```

## Tuning notes

- Contact-rich tasks need force/torque or tactile sensing, not just vision.
- Collect small but high-quality teleoperated demonstrations per skill.
- Test on real hardware early; simulation gap is large for insertion and deformation.

## Verification

1. Train a peg/insertion policy on force-torque data and measure success rate.
2. Fine-tune a VLA model on a small set of natural-language assembly instructions.
3. Compare a learned policy to a classical force controller on a contact-rich task.

## References

- https://arxiv.org/html/2607.14021v2
- https://www.nature.com/articles/s42256-026-01292-y
- https://arxiv.org/html/2604.20246
- https://arxiv.org/html/2608.17962
