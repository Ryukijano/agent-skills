# AI for Oncology

## Description

AI for cancer detection, subtyping, treatment response, prognosis, radiomics, pathology, and clinical trial matching.

## When to use

You are building AI for cancer detection, tumor subtyping, treatment response prediction, prognosis, or matching patients to clinical trials.

## Key concepts

- **Radiomics and deep learning for tumor imaging**: high-throughput feature extraction and CNN-based biomarkers.
- **Digital and computational pathology**: molecular biomarker prediction from H&E slides.
- **Treatment response and survival prediction**: from imaging, genomics, and EHR data.
- **Multimodal data fusion**: imaging, genomics, pathology, and clinical variables.
- **Clinical trial matching and real-world evidence**: NLP and eligibility criteria.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Predict treatment response from radiomic features
X = df[['texture_contrast', 'shape_volume', 'wavelet_HLL_glcm_entropy']]
y = df['response']

model = RandomForestClassifier(n_estimators=200, class_weight='balanced')
model.fit(X, y)
```

## Tuning notes

- Use standardized radiomic feature extraction (e.g., pyradiomics with IBSI filters).
- Validate with external and prospective cohorts, not just public leaderboards.
- Integrate pathology, genomics, and clinical data when available.
- Report uncertainty and ensure models support clinical decisions.

## Verification

1. Train a tumor classification or response model and compare with standard care.
2. Extract radiomic features and assess repeatability across scanners.
3. Validate a multimodal survival prediction on an external cohort.

## References

- https://link.springer.com/article/10.1186/s12943-025-02450-3
- https://www.cancerbiomed.org/content/22/1/6
- https://bmjoncology.bmj.com/content/3/1/e000134
- https://link.springer.com/article/10.1186/s12967-025-07308-2
- https://www.nature.com/articles/s41416-023-02317-8
