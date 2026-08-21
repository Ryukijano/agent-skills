# AI for Computer-Aided Design (CAD)

## Description

Generate editable parametric CAD command sequences from text or sketches to accelerate mechanical design iteration.

## When to use

You need to generate, complete, edit, or retrieve 3D parametric CAD models from sketches, images, text, or partial command sequences.

## Usage

- Generate parametric CAD command sequences and B-rep geometry from design specifications.
- Complete partial CAD sketches or models using transformer or VQ-VAE models over CAD tokens.
- Condition generation on images, text, or partial inputs for image-to-CAD and text-to-CAD workflows.
- Enforce geometric and manufacturing constraints such as symmetry, parallelism, and manufacturability.

## Steps

1. Parse or collect CAD data (sketch-and-extrude sequences, B-rep, CSG, or command history) and tokenize operations.
2. Train or fine-tune a transformer, VQ-VAE, or autoregressive model on parametric CAD sequences.
3. Implement conditional generation for sketch completion, image-to-CAD, or text-to-CAD tasks.
4. Validate generated sequences with a CAD kernel (Open CASCADE, FreeCAD) and convert to valid B-rep solids.
5. Check geometric constraints (symmetry, perpendicularity, fillets) and manufacturability rules.
6. Iterate with domain feedback and integrate the model into a CAD design-assistant or retrieval pipeline.

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
