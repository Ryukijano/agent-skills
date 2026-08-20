# AI for Space Exploration

## Description

Onboard autonomy, science target selection, anomaly detection, mission planning, and analysis of space and Earth-observation data.

## When to use

You are designing, simulating, or operating spacecraft, rovers, or satellites that must make decisions with limited communication, power, or compute.

## Key concepts

- **Onboard autonomy and science agents**: detect events, prioritize observations, and retarget instruments without ground-in-the-loop.
- **Dynamic targeting and opportunistic science**: AI-driven selection of targets during orbital overflights.
- **Anomaly detection and health monitoring**: detect faults in telemetry, instruments, and subsystems.
- **Mission planning and scheduling**: optimize observation campaigns under constraints.
- **Earth-observation and planetary data**: analyze multispectral, hyperspectral, and mass-spectrometer data.

## Code pattern

```python
from astropy.io import fits
import numpy as np

with fits.open("observation.fits") as hdul:
    image = hdul[0].data
    header = hdul[0].header

# Simple onboard anomaly score
score = np.abs(image - np.median(image)) / np.std(image)
anomaly_mask = score > 5
```

## Tuning notes

- Resource constraints (power, compute, radiation-hardened hardware) dominate design choices.
- Communication delays and blackouts require robust onboard decision-making.
- Validate autonomy with high-fidelity simulators and representative analog datasets.

## Verification

1. Implement a simple anomaly detector on spacecraft telemetry and flag synthetic faults.
2. Build a target-prioritization model and test it in a mission simulator.
3. Process a FITS image cube and validate derived science products against ground truth.

## References

- https://science.jpl.nasa.gov/projects/autonomous-sciencecraft-experiment-ase/
- https://www.nasa.gov/science-research/earth-science/how-nasa-is-testing-ai-to-make-earth-observing-satellites-smarter/
- https://ntrs.nasa.gov/citations/20240005003
- https://science.nasa.gov/science-research/science-enabling-technology/technology-highlights/towards-autonomous-surface-missions-on-ocean-worlds/
