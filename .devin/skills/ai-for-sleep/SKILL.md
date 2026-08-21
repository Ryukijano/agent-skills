# AI for Sleep

## Description

Automate sleep staging and sleep-disordered-breathing detection from PSG, wearables, and home sleep tests with deep learning.

## When to use

You are analyzing polysomnography (PSG), wearable sleep recordings, or building a tool to detect sleep disorders and stages.

## Usage

- **Sleep staging**: score 30-second epochs into W, N1, N2, N3, and REM from PSG, wearables, or EEG headbands.
- **Sleep-disordered-breathing detection**: detect and classify apneas, hypopneas, and arousals.
- **AHI estimation**: estimate apnea-hypopnea index and severity from oximetry, PPG, or other sensors.
- **Foundation models**: pre-train on large PSG/EEG corpora for cross-cohort and cross-device transfer.
- **Event-level analysis**: identify arousals, limb movements, and respiratory events with precise timing.
- **Clinical validation**: compare wearable or automated scoring to AASM expert-annotated PSG.

## Steps

1. Collect and annotate PSG or wearable recordings following AASM scoring rules.
2. Preprocess signals (filter, resample, align modalities) and create 30-second epochs with context windows.
3. Train a temporal/sequence model (CNN, ResNet+TCN+LSTM, Mamba, or transformer) for staging or event detection.
4. Evaluate against expert annotators using epoch/stage agreement (Cohen's kappa, AUROC, AUPRC).
5. Validate on external cohorts and compare wearable-only models to gold-standard PSG.
6. Deploy for home sleep testing or clinical decision support with nightly risk reports.

## Code pattern

```python
import mne
import numpy as np
from scipy.signal import welch
from sklearn.ensemble import RandomForestClassifier

# Load an EDF and extract fixed-length epochs
raw = mne.io.read_raw_edf('sleep.edf', preload=True)
events = mne.make_fixed_length_events(raw, duration=30.0)
epochs = mne.Epochs(raw, events, tmin=0, tmax=30.0, baseline=None, preload=True)

# Extract band power features from one EEG channel
sfreq = raw.info['sfreq']
data = epochs.get_data()[:, 0, :]  # first EEG channel
f, psd = welch(data, fs=sfreq, nperseg=sfreq*2)

delta = psd[:, (f >= 0.5) & (f < 4)].mean(axis=1)
theta = psd[:, (f >= 4) & (f < 8)].mean(axis=1)
alpha = psd[:, (f >= 8) & (f < 13)].mean(axis=1)
features = np.column_stack([delta, theta, alpha])

# Train a simple sleep-stage model (labels needed)
clf = RandomForestClassifier(n_estimators=100)
# clf.fit(features, labels)
```

## Tuning notes

- Apply the AASM scoring rules as the reference standard.
- Handle class imbalance across sleep stages (N2 usually dominates).
- Use time context (adjacent epochs) to improve staging.
- Validate wearable models against concurrent PSG.
- Watch for channel mismatches across recording devices.

## Verification

1. Train a sleep-stage classifier on 30-s PSG epochs and compare to human scoring.
2. Extract delta/theta/alpha features and visualize their distribution by stage.
3. Evaluate a model on data from a different device/sensor.

## References

- https://www.physionet.org/content/dreamt/2.2.0/
- https://yang-ai-lab.github.io/osf/
- https://doi.org/10.3390/bioengineering11030206
- https://link.springer.com/article/10.1186/s12911-025-03129-x
- https://www.nature.com/articles/s41746-025-02237-2
