# AI for Industrial Robotics

## Description

Use machine learning to automate precision assembly, bin picking, cable routing, and force-guided manipulation in manufacturing cells.

## When to use

You are automating precision assembly, cable routing, bin picking, or contact-rich tasks in a manufacturing cell.

## Usage

- Learn end-to-end manipulation and diffusion policies with force/torque feedback.
- Transfer skills from simulation to real with domain randomization.
- Ground natural-language assembly instructions in vision-language-action models.
- Curate multimodal teleoperation datasets for factory-relevant skills.

## Steps

1. Set up a robot cell with cameras, force sensors, and teleoperation recording.
2. Collect small, high-quality demonstrations for the target assembly skill.
3. Train an imitation, diffusion, or VLA policy with appropriate augmentations.
4. Validate success rate on real hardware, not just simulation.
5. Iterate with force feedback and failure analysis for contact-rich tasks.

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

- https://arxiv.org/abs/2607.14021v2
- https://www.nature.com/articles/s42256-026-01292-y
- https://arxiv.org/abs/2604.20246
- https://arxiv.org/abs/2608.17962
