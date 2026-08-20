# AI for Photovoltaics

## Description

Machine learning for solar-cell materials discovery, perovskite and organic PV optimization, device engineering, and stability prediction.

## When to use

You are exploring new absorbers, interfaces, or processing conditions for perovskite, organic, silicon, or tandem solar cells.

## Key concepts

- **Materials screening for absorbers**: bandgap, carrier mobility, defect tolerance, and toxicity prediction.
- **Perovskite composition and process design**: high-throughput experiments, robotic synthesis, and AI-guided optimization.
- **Organic photovoltaic (OPV) design**: molecular property prediction, non-fullerene acceptor discovery, and device-performance modeling.
- **Stability and degradation forecasting**: predict long-term performance under light, heat, and humidity.
- **Tandem and emerging architectures**: bandgap matching and current-matching for multi-junction cells.

## Code pattern

```python
from rdkit import Chem
from rdkit.Chem import Descriptors

mol = Chem.MolFromSmiles("c1cc2c(s1)c1ccccc1C2=O")
homo_lumo = Descriptors.MolMR(mol)  # example descriptor placeholder
print(homo_lumo)
```

## Tuning notes

- PV datasets are often small and high-dimensional; use transfer learning and physics-informed descriptors (bandgap, dielectric constant, ion migration).
- Distinguish between molecular and device-level predictions; device performance depends strongly on morphology and processing.
- Stability is as important as efficiency; include degradation and hysteresis features in models.

## Verification

1. Predict power-conversion efficiency or bandgap for a set of PV absorbers and compare to experimental cells.
2. Optimize a perovskite composition or annealing protocol using an autonomous or ML-guided lab loop.
3. Forecast degradation under accelerated aging and compare to ground-truth stability measurements.

## References

- https://pubs.rsc.org/en/content/articlehtml/2025/el/d5el00041f
- https://doi.org/10.1002/aenm.202506803
- https://www.sciencedirect.com/science/article/abs/pii/S0925838823021278
- https://www.sciencedirect.com/science/article/abs/pii/S209549562400161X
- https://pubs.rsc.org/en/content/articlehtml/2024/ta/d4ta01942c
