# AI for Data Observability

## Description

ML-driven monitoring of data freshness, schema drift, volume anomalies, lineage breaks, and pipeline health to ensure reliable data operations.

## When to use

You need end-to-end visibility into data pipelines and want to detect, diagnose, and remediate data incidents automatically.

## Usage

- **Freshness and volume monitoring**: detect late or missing data.
- **Schema and distribution drift**: identify unexpected changes in data shape or distributions.
- **Lineage-aware anomaly detection**: localize pipeline failures using dependency graphs.
- **Automated root cause analysis**: rank likely causes and suggest fixes.
- **SLO dashboards**: track data reliability, completeness, and freshness KPIs.

## Steps

1. Instrument pipelines with run, dataset, and model metadata.
2. Define observability signals: freshness, row count, schema, distributions.
3. Train anomaly detectors on historical pipeline behavior.
4. Correlate anomalies with lineage and code or infrastructure changes.
5. Alert and auto-remediate common failure modes.

## Code pattern

```python
from scipy import stats

# Schema-free distribution check on a numeric column
latest = df["revenue"].dropna()
expected_mean = historical_mean
z_stat = (latest.mean() - expected_mean) / (latest.std() / len(latest) ** 0.5)
```

For production, integrate with tools such as Great Expectations, Soda, or Monte Carlo.

## Tuning notes

- Establish baseline windows that account for seasonality and known changes.
- Avoid alert fatigue by grouping correlated anomalies.
- Preserve lineage to reduce mean time to detection.

## Verification

1. Inject a schema change and show the observability alert fires.
2. Detect a row-count drop in a pipeline and localize the failed task.
3. Compare anomaly detection precision to threshold-only monitoring.

## References

- https://www.vldb.org/pvldb/vol15/p4015-shankar.pdf
- https://doi.org/10.60087/jaigs.v6i1.412
- https://doi.org/10.5281/zenodo.20801568
- https://doi.org/10.5281/zenodo.19487347
