# AI for Membranes

## Description

Design polymer membranes for gas and carbon-capture separations using graph ML to surpass selectivity-permeability upper bounds.

## When to use

You are designing polymeric, ceramic, or 2D membranes for gas separation, water treatment, fuel cells, or energy applications.

## Usage

- Predict membrane permeability, selectivity, fouling resistance, and stability from chemical structure.
- Screen polymeric and 2D materials for gas, ion, or water-selective membranes.
- Model fouling, flux decline, and cleaning cycles from process data.
- Generate polymer repeat units or pore structures for target separation performance.

## Steps

1. Collect membrane chemical structures and measured performance data under relevant conditions.
2. Represent polymers and 2D materials with repeat units, fragments, and topological descriptors.
3. Train regression models for permeability/selectivity, applying log-transforms for wide-ranging targets.
4. Use explainable AI to identify structural drivers of free volume, pore size, and solubility.
5. Run virtual screening or inverse design to propose candidates and validate top performers with synthesis.
6. Model fouling and flux decline from process data and optimize cleaning and operating schedules.

## Code pattern

```python
from rdkit import Chem
from sklearn.ensemble import GradientBoostingRegressor

mol = Chem.MolFromSmiles("C1CCOC1")  # example repeat unit
X = [[mol.GetNumHeavyAtoms(), Descriptors.MolWt(mol), Descriptors.TPSA(mol)]]
y = [ permeability_value ]
model = GradientBoostingRegressor().fit(X, y)
```

## Tuning notes

- Use appropriate representations for polymers (repeat units, fragments, topological descriptors) rather than monomer SMILES alone.
- Permeability and selectivity often span many orders of magnitude; log-transform targets before regression.
- Include operational conditions (temperature, pressure, feed composition) for deployment-relevant models.

## Verification

1. Predict gas permeability or water flux for a membrane polymer and compare to experimental data.
2. Identify top candidates from a virtual screen and validate one with synthesis and permeation testing.
3. Model fouling rate under realistic feed conditions and compare to pilot-plant observations.

## References

- https://pmc.ncbi.nlm.nih.gov/articles/PMC10941251/
- https://www.mdpi.com/2077-0375/15/12/353
- https://pureadmin.qub.ac.uk/ws/portalfiles/portal/556052977/Machine_learning_for_membrane.pdf
- https://doi.org/10.1063/5.0205433
- https://europepmc.org/article/med/39680111
