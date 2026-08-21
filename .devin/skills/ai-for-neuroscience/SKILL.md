# AI for Neuroscience

## Description

Decode speech and motor intent from electrocorticography to restore communication and movement via brain-computer interfaces.

## When to use

You are analyzing EEG, MEG, fMRI, calcium imaging, or spike data and want to decode neural states, detect biomarkers, or build NeuroAI models.

## Usage

- **Neural decoding**: predict cognitive states, movements, or stimuli from EEG, MEG, fMRI, or spike data.
- **Foundation models**: apply self-supervised models (DIVER-1, NeuroSTORM, AdaBrain) for cross-subject/cross-device representations.
- **Signal preprocessing**: use MNE, FSL, or AFNI to standardize, filter, and artifact-reject recordings.
- **Biomarker discovery**: identify neural signatures that correlate with disease, behavior, or treatment response.
- **Brain-computer interfaces**: build real-time decoders and map them to output devices or feedback.
- **Connectomics**: model structural and functional brain connectivity from imaging or electrophysiology.

## Steps

1. Choose the neural modality and task (e.g., sleep staging, motor BCI, naturalistic decoding) and curate datasets.
2. Preprocess signals: re-reference, filter, artifact-reject, and segment into epochs or trials.
3. Extract features (band power, spectrograms, connectivity) or load pretrained foundation-model embeddings.
4. Train a task-specific decoder with cross-subject or leave-one-subject validation.
5. Evaluate on held-out data and compare to expert or clinical annotations (accuracy, kappa, AUROC).
6. Deploy on the target hardware or device and validate in a real-time, closed-loop setting.

## Code pattern

```python
import mne
import numpy as np
import torch
import torch.nn as nn

# Load and epoch an EEG recording
raw = mne.io.read_raw_edf('subject_01.edf', preload=True)
events = mne.make_fixed_length_events(raw, duration=2.0)
epochs = mne.Epochs(raw, events, tmin=0, tmax=2.0, baseline=None, preload=True)

X = epochs.get_data()  # (n_epochs, n_channels, n_times)
y = epochs.metadata['condition']

# Simple 1D CNN over time per channel
class SimpleCNN(nn.Module):
    def __init__(self, n_channels, n_classes):
        super().__init__()
        self.conv1 = nn.Conv1d(n_channels, 32, kernel_size=25, stride=2)
        self.pool = nn.AdaptiveAvgPool1d(1)
        self.fc = nn.Linear(32, n_classes)

    def forward(self, x):
        x = torch.relu(self.conv1(x))
        x = self.pool(x).squeeze(-1)
        return self.fc(x)

model = SimpleCNN(X.shape[1], len(np.unique(y)))
print(model)
```

## Tuning notes

- Standardize channel layouts and sampling rates across subjects.
- Reject epochs with excessive movement or EMG artifact before training.
- Use cross-subject validation to estimate real-world generalization.
- Temporal alignment matters for ERP/ERF analyses.
- Interpret models with SHAP or channel-wise saliency maps.

## Verification

1. Train a CNN to classify two cognitive conditions from EEG and report accuracy.
2. Visualize topographic activation for important time windows.
3. Compare a subject-specific model to a leave-one-subject-out model.

## References

- https://mne.tools/
- https://github.com/facebookresearch/neuroai
- https://github.com/catalystneuro/neuroconv
- https://doi.org/10.1016/j.neures.2024.06.003
- https://doi.org/10.1088/1741-2552/ae4455
