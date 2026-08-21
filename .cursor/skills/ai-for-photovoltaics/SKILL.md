# AI for Photovoltaics

## Description

Use ML and high-throughput experimentation to discover solar-cell absorbers, optimize perovskite and organic PV, and predict device performance and stability.

## When to use

You are exploring new absorbers, interfaces, or processing conditions for perovskite, organic, silicon, or tandem solar cells.

## Usage

- Screen absorbers for bandgap, carrier mobility, defect tolerance, and toxicity.
- Optimize perovskite composition and processing with high-throughput experiments and robotic synthesis.
- Predict molecular and device properties for organic photovoltaics and non-fullerene acceptors.
- Forecast stability and degradation under light, heat, and humidity for candidate cells.

## Steps

1. Define target application (single-junction, tandem, flexible) and collect material and device datasets.
2. Train models to predict bandgap, carrier mobility, absorption, and defect tolerance for absorber candidates.
3. Run high-throughput or robotic experiments to synthesize and characterize perovskite/organic films.
4. Build a device-performance model that couples material descriptors to measured PCE, FF, and VOC.
5. Forecast stability under accelerated aging and identify degradation mechanisms.
6. Validate top candidates with real devices and iterate the model with new experimental results.

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
