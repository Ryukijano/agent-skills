# AI for Proteomics

## Description

Mass spectrometry protein identification and quantification, DDA/DIA workflows, post-translational modifications, and AI-driven peptide property prediction.

## When to use

You are analyzing mass spectrometry proteomics data to quantify proteins, identify post-translational modifications, build spectral libraries, or predict peptide properties.

## Key concepts

- **LC-MS/MS workflows**: DDA, DIA, SRM/PRM, and data-independent acquisition.
- **Peptide-spectrum matching**: search engines, spectral libraries, and rescoring.
- **Protein inference and FDR**: PSM, peptide, and protein-level false discovery rates.
- **PTMs**: phosphorylation, ubiquitination, glycosylation, and other modifications.
- **AI for proteomics**: retention time, fragmentation, and MHC-peptide binding prediction.

## Code pattern

```python
from pyteomics import mzml

# Iterate DDA spectra and parse precursor charge states
with mzml.read("run.mzML") as reader:
    for spectrum in reader:
        if spectrum["ms level"] == 2:
            prec = spectrum["precursorList"]["precursor"][0]
            ion = prec["selectedIonList"]["selectedIon"][0]
            print(ion["charge state"], ion["selected ion m/z"])
```

## Tuning notes

- Control FDR at PSM, peptide, and protein levels (1% typical).
- Normalize for total ion current or a reference channel.
- Impute missing values only after confirming MCAR/MAR mechanism.
- Choose DIA software (DIA-NN, Spectronaut, OpenSWATH) matched to library design.

## Verification

1. Benchmark identification and quantification on a public standard (e.g., iPRG, PXD).
2. Compare peptide-level fold changes to orthogonal western blot or PRM data.
3. Check retention time and ion intensity predictions against observed values.

## References

- https://doi.org/10.1002/pmic.201900335
- https://doi.org/10.1038/s41587-022-01424-w
- https://doi.org/10.1016/j.crmeth.2021.100003
- https://doi.org/10.1002/pmic.202400398
