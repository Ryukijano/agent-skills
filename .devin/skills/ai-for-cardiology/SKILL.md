# AI for Cardiology

## Description

ECG interpretation, arrhythmia detection, heart failure screening, echocardiography analysis, and cardiovascular risk stratification with deep learning.

## When to use

You are interpreting ECGs, detecting arrhythmias, predicting heart failure or ejection fraction, or integrating wearables into cardiovascular care.

## Key concepts

- **ECG signal processing**: filtering, baseline wander removal, R-peak detection, and resampling to a standard rate.
- **Arrhythmia detection**: atrial fibrillation, flutter, premature ventricular contractions, and blocks.
- **Convolutional and 1D networks for 12-lead ECG classification**.
- **AI-enabled ECG**: detect low ejection fraction or prior AF even during sinus rhythm.
- **Holter and wearable monitoring**: long-term, low-fidelity single-lead data.

## Code pattern

```python
import wfdb
import torch
from torch import nn

# Load a 12-lead ECG record
record = wfdb.rdrecord("ptbxl/00001", pn_dir="ptbxl")
# shape: (time, 12)

ecg = torch.tensor(record.p_signal.T, dtype=torch.float32).unsqueeze(0)
model = nn.Sequential(
    nn.Conv1d(12, 32, kernel_size=7),
    nn.ReLU(),
    nn.AdaptiveAvgPool1d(1),
    nn.Flatten(),
    nn.Linear(32, 2)
)
```

## Tuning notes

- Standardize sampling rate (e.g., 500 Hz) and lead order across datasets.
- Use patient-level or time-based splits to avoid leakage.
- Align with AAMI/ESC annotation standards.
- Calibrate scores and integrate with clinical workflows (EMR, ECG carts).

## Verification

1. Train an atrial fibrillation classifier and report F1 on an external test set.
2. Compare AI-ECG ejection fraction screening to echocardiography.
3. Validate real-time inference on Holter data.

## References

- https://www.nature.com/articles/s41591-018-0240-2
- https://doi.org/10.1016/s0140-6736(19)31721-0
- https://openheart.bmj.com/content/12/1/e003185
- https://www.mdpi.com/1424-8220/25/13/4109
