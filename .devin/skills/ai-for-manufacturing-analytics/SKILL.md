# AI for Manufacturing Analytics

## Description

Turns MES and ERP data into OEE dashboards and predictive KPIs for prescriptive manufacturing decisions.

## When to use

You need to turn MES, ERP, quality, and maintenance data into actionable performance insights, from historical dashboards to predictive and prescriptive recommendations.

## Usage

- **Manufacturing KPIs**: track OEE, OLE, MTBF, MTTR, scrap rate, first-pass yield, and takt time.
- **Descriptive analytics**: build dashboards, Pareto charts, loss analysis, and trend reports.
- **Diagnostic analytics**: drill down into downtime, defect, and bottleneck causes.
- **Predictive and prescriptive**: forecast KPIs, simulate interventions, and recommend actions.
- **Association rule mining**: discover co-occurring conditions that drive losses.

## Steps

1. Integrate MES, ERP, quality, and maintenance data into a clean data model.
2. Define and compute consistent KPIs across shifts, lines, and plants.
3. Build dashboards and diagnostic views to find top losses and trends.
4. Train predictive models for KPIs and generate prescriptive recommendations.
5. Pilot recommendations, measure impact, and iterate.

## Code pattern

```python
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Find frequent patterns in downtime events
basket = pd.get_dummies(df[["machine", "shift", "downtime_category"]])
frequent = apriori(basket, min_support=0.05, use_colnames=True)
rules = association_rules(frequent, metric="lift", min_threshold=1.5)
```

## Tuning notes

- Define KPIs consistently across shifts, lines, and plants before modeling.
- Combine OEE with cost and sustainability metrics for a balanced view.
- Use controlled pilots to validate prescriptive recommendations before scaling.

## Verification

1. Build an OEE dashboard and reconcile it with manual production reports.
2. Predict next-week OEE and compare to a naive baseline.
3. Implement a prescriptive recommendation and measure actual KPI improvement.

## References

- https://doi.org/10.1108/ijqrm-01-2023-0012
- https://www.mdpi.com/2504-2289/7/3/138
- https://www.mdpi.com/2504-4494/6/3/59
- https://doi.org/10.2478/scjme-2024-0026
