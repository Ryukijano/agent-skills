# AI for Sleep

## Description

Machine learning for sleep staging, sleep disorder detection, wearable PSG analysis, and sleep health monitoring.

## When to use

You are analyzing polysomnography (PSG), wearable sleep recordings, or building a tool to detect sleep disorders and stages.

## Key concepts

- **Sleep stages**: W, N1, N2, N3, REM; scored from EEG/EOG/EMG.
- **PSG**: gold-standard overnight multi-channel recording.
- **Wearable sleep monitoring**: actigraphy, PPG, single-channel EEG headbands.
- **Sleep disorders**: obstructive sleep apnea, insomnia, narcolepsy, restless legs.
- **Sleep foundation models**: large-scale pre-training on PSG/EEG data.
- **Event detection**: apneas, hypopneas, arousals, limb movements.

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
