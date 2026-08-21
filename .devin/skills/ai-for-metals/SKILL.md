# AI for Metals and Alloys

## Description

Use ML to design alloys, predict phase stability and properties, quantify microstructure, and optimize metal processing and additive manufacturing.

## When to use

You are designing new alloys or optimizing metal processing and need to predict phase stability, mechanical behavior, corrosion resistance, or manufacturability from composition and processing history.

## Usage

- Predict composition-process-microstructure-property relationships for steels, aluminum, titanium, magnesium, and HEAs.
- Combine CALPHAD thermodynamics with ML for phase stability and transformation kinetics.
- Quantify microstructure (grain size, texture, precipitates, phase fractions) from EBSD/SEM images.
- Optimize additive manufacturing, heat treatment, and processing parameters for target properties.

## Steps

1. Collect composition, processing, microstructure, and property data for the alloy class of interest.
2. Encode composition with physically meaningful descriptors and train models for target properties or phase stability.
3. Segment and quantify microstructure images to extract grain, precipitate, and texture features.
4. Run CALPHAD-ML hybrids or phase-stability classifiers and validate against DFT or experiments.
5. Optimize processing (heat treatment, AM parameters, rolling) with Bayesian or active-learning methods.
6. Validate the best candidates with mechanical, corrosion, or creep tests and compare to known alloy baselines.

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
- https://bsg.byu.edu/docs/papers/NRM_ML_for_Alloys.pdf
- https://doi.org/10.1007/s10853-025-11154-4
