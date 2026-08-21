# AI for Data Observability

## Description

Monitor data freshness, volume, and lineage to detect pipeline failures.

## When to use

You need end-to-end visibility into data pipelines and want to detect, diagnose, and remediate data incidents automatically.

## Usage

- Auto-generate freshness, volume, and schema monitors (Monte Carlo, dataobservability.ai).
- Detect anomalies in row counts and distribution (Soda, Prizm).
- Map column-level lineage and downstream impact.
- Correlate data incidents with cost and performance metrics.
- Build runbooks and root-cause analysis with AIOps.

## Steps

1. Connect warehouses, lakes, and pipeline orchestrators.
2. Baseline historical metrics for freshness, volume, and schema.
3. Deploy ML-based or rule-based anomaly detection.
4. Alert teams and route incidents by lineage.
5. Track MTTR and refine thresholds.

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
