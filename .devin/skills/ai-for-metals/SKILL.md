# AI for Metals and Alloys

## Description

Machine learning for alloy design, phase stability, mechanical properties, process optimization, and microstructure-property mapping.

## When to use

You are designing new alloys or optimizing metal processing and need to predict phase stability, mechanical behavior, corrosion resistance, or manufacturability from composition and processing history.

## Key concepts

- **Alloy design and property prediction**: composition-process-microstructure-property models for steels, aluminum, magnesium, titanium, and high-entropy alloys.
- **Phase diagrams and CALPHAD-ML hybrids**: integrate thermodynamic databases with ML for phase stability and transformation kinetics.
- **Microstructure quantification**: grain size, texture, precipitate distributions, and phase fractions from EBSD/SEM images.
- **High-entropy alloys (HEAs) and metallic glasses**: ML-driven search for solid solutions, single-phase regions, and glass-forming ability.
- **Additive manufacturing and processing**: porosity, crack susceptibility, and heat-treatment optimization.

## Code pattern

```python
import matminer
from sklearn.ensemble import RandomForestRegressor

featurizer = matminer.featurizers.composition.ElementProperty.from_preset("magpie")
X = df["composition"].apply(featurizer.featurize)
y = df["yield_strength_MPa"]
model = RandomForestRegressor().fit(list(X), y)
```

## Tuning notes

- Use physically meaningful descriptors (elemental, thermodynamic, structural) rather than raw composition alone.
- Train separate models for distinct alloy classes or microstructural regimes.
- Validate with tensile/creep/fatigue experiments, not just property databases.

## Verification

1. Predict a mechanical or phase-stability property for a multi-component alloy and compare to DFT or experiment.
2. Build a classifier for single-phase HEA formation and validate against known systems.
3. Segment metal micrographs and extract grain-size or precipitate statistics.

## References

- https://doi.org/10.3390/alloys5010007
- https://www.sciencedirect.com/science/article/abs/pii/S0927796X23000323
- https://bsg.byu.edu/docs/papers/nrm_ml_for_alloys.pdf
- https://doi.org/10.1007/s10853-025-11154-4
