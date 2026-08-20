# AI for Computer-Aided Design (CAD)

## Description

Deep generative models for parametric CAD sketches, B-rep synthesis, sketch-and-extrude sequences, and vision-language conditional CAD generation.

## When to use

You need to generate, complete, edit, or retrieve 3D parametric CAD models from sketches, images, text, or partial command sequences.

## Key concepts

- **Parametric CAD sequences**: sketch-and-extrude, boolean, fillet, chamfer operations.
- **B-rep and CSG representations**: boundary representation vs. constructive solid geometry.
- **CAD generative models**: Transformers, VQ-VAEs, and autoregressive models over CAD tokens.
- **Conditional CAD generation**: completion from partial inputs, image-to-CAD, text-to-CAD.
- **Design constraints**: symmetry, parallelism, perpendicularity, and manufacturability.

## Code pattern

```python
import torch
import torch.nn as nn

# Simplified autoregressive CAD command sequence model
class CADSequenceModel(nn.Module):
    def __init__(self, vocab_size, d_model=128, nhead=4, num_layers=4):
        super().__init__()
        self.embed = nn.Embedding(vocab_size, d_model)
        self.pos = nn.Parameter(torch.randn(1, 512, d_model))
        decoder_layer = nn.TransformerDecoderLayer(d_model=d_model, nhead=nhead, batch_first=True)
        self.decoder = nn.TransformerDecoder(decoder_layer, num_layers=num_layers)
        self.head = nn.Linear(d_model, vocab_size)

    def forward(self, seq, condition):
        x = self.embed(seq) + self.pos[:, :seq.size(1), :]
        x = self.decoder(x, condition.unsqueeze(1))
        return self.head(x)

vocab_size = 128  # operation + parameter tokens
model = CADSequenceModel(vocab_size)
commands = torch.randint(0, vocab_size, (4, 32))
logits = model(commands, condition=torch.randn(4, 128))
```

## Tuning notes

- Tokenize CAD operations and parameters separately or jointly depending on the model.
- Use a robust CAD kernel (e.g., Open CASCADE, FreeCAD) to validate generated sequences.
- Data augmentation by random command orderings and parameter perturbations can help.
- Evaluate with geometry-based and sequence-based metrics.

## Verification

1. Train a model to auto-complete partial CAD command sequences.
2. Generate 50 CAD models and check valid B-rep conversion rate.
3. Compare generated designs to ground-truth on Chamfer distance and command accuracy.

## References

- https://openaccess.thecvf.com/content/ICCV2021/papers/Wu_DeepCAD_A_Deep_Generative_Network_for_Computer-Aided_Design_Models_ICCV_2021_paper.pdf
- https://proceedings.mlr.press/v202/xu23f.html
- https://arxiv.org/abs/2409.17457
- https://proceedings.mlr.press/v162/xu22k.html
- https://ojs.aaai.org/index.php/AAAI/article/view/32531
