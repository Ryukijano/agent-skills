# Proteomics and Metabolomics ML

## Description

Mass spectrometry, peptide identification, DelPi, DIA-BERT, GiCOPS, ANN-SoLo, and metabolite annotation on GPU.

## When to use

You are analyzing mass spectrometry data for protein/metabolite identification and annotation.

## Key concepts

- **Peptide identification**: DelPi (DIA), DIA-BERT (transformer), GiCOPS (database search).
- **Spectral library search**: ANN-SoLo with approximate nearest neighbors.
- **Metabolite annotation**: CSI:FingerID, Sirius, GNPS.
- **GPU**: PyTorch/CUDA for transformers and ANN search.

## Code pattern

```python
# DelPi inference
from delpi import DelPi
model = DelPi.from_pretrained("...")
model = model.to('cuda')
```

## Tuning notes

- DIA-BERT needs 40GB+ GPU (V100/A100) for training; smaller for inference.
- Use FDR control at 1% for peptide-spectrum matches.
- Metabolite annotation often combines MS/MS with molecular DBs.

## Verification

1. Run DelPi/DIA-BERT on a DIA dataset and compare IDs to DDA.
2. Run ANN-SoLo and measure sensitivity vs runtime.
3. Validate protein identifications with a known standard mixture.

## References

- https://github.com/bertis-informatics/delpi
- https://github.com/guomics-lab/DIA-BERT
- https://github.com/pcdslab/gicops
- https://doi.org/10.5281/zenodo.3831054
