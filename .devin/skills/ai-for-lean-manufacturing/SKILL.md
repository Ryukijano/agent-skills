# AI for Lean Manufacturing

## Description

Quantifies waste, maps value streams, and prioritizes kaizen actions using real-time production event data.

## When to use

You are running a lean transformation and need to identify muda, quantify value-added time, prioritize improvement actions, and sustain pull-based flow.

## Usage

- **Waste identification**: classify overproduction, waiting, transport, over-processing, inventory, motion, and defects.
- **Value stream mapping (VSM)**: visualize material and information flow and compute value-added ratio.
- **Process mining for lean**: discover actual flows from event logs and quantify non-value-added time.
- **Bottleneck and line balancing**: detect constraints limiting takt time and throughput.
- **Kaizen prioritization**: use Pareto, GUT matrix, and 5-Why analysis guided by data.

## Steps

1. Extract event logs, process maps, and time-study data from MES or SCADA.
2. Compute value-added, necessary non-value-added, and non-value-added time.
3. Identify the biggest wastes and bottlenecks with Pareto and flow analysis.
4. Prioritize kaizen actions and simulate their impact on lead time and WIP.
5. Track before/after metrics and update the digital value stream map.

## Code pattern

```python
import pandas as pd

# Compute value-added ratio from event log
log = pd.read_csv("production_events.csv", parse_dates=["start", "end"])
log["duration"] = (log["end"] - log["start"]).dt.total_seconds()
va_time = log.loc[log["activity_type"] == "value_added", "duration"].sum()
total_time = log["duration"].sum()
print("Value-added ratio:", va_time / total_time)
```

## Tuning notes

- Distinguish value-added from necessary non-value-added using domain definitions.
- Update VSMs with real-time data rather than static time studies.
- Tie analytics to actionable kaizen actions and track before/after metrics.

## Verification

1. Build a digital value stream map and compare lead time to the manual version.
2. Identify the top three wastes with a Pareto chart and validate with shop-floor observation.
3. Run a kaizen experiment and measure lead-time or WIP reduction.

## References

- https://doi.org/10.1108/ijlss-03-2024-0059
- https://doi.org/10.1080/00207543.2021.1906460
- https://doi.org/10.3390/su16041694
- https://doi.org/10.1016/j.eswa.2019.01.026
- https://doi.org/10.3390/jmmp10030098
