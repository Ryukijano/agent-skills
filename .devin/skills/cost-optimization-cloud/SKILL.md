# Cloud Cost Optimization for MLOps

## Description

FinOps practices, spot/preemptible instances, right-sizing, reserved capacity, autoscaling, and cost-aware scheduling for ML workloads.

## When to use

You need to control cloud spend for data, training, or inference workloads without sacrificing reliability or performance.

## Key concepts

- **FinOps**: collaborative cloud financial management (inform, optimize, operate).
- **Spot/preemptible instances**: unused capacity at deep discounts with interruption risk.
- **Reserved capacity / savings plans**: commit to usage for lower rates.
- **Right-sizing and autoscaling**: match resources to actual demand.
- **Cost allocation and tagging**: attribute spend to teams, projects, and experiments.

## Code pattern

```python
import boto3
from datetime import datetime, timedelta

ec2 = boto3.client('ec2')
prices = ec2.describe_spot_price_history(
    InstanceTypes=['g5.xlarge'],
    ProductDescriptions=['Linux/UNIX'],
    StartTime=datetime.utcnow() - timedelta(hours=1)
)

if prices['SpotPriceHistory']:
    avg = sum(float(p['SpotPrice']) for p in prices['SpotPriceHistory']) / len(prices['SpotPriceHistory'])
    print(f"Average g5.xlarge spot price (1h): ${avg:.4f}")
else:
    print("No spot price history available")
```

## Tuning notes

- Use spot for interruptible training and batch jobs; use on-demand/reserved for serving.
- Set autoscaling min/max and scale-down delays to avoid idle nodes.
- Tier storage and archive old artifacts; storage costs compound quickly.
- Track cost per prediction and per experiment, not just total cloud bill.

## Verification

1. Implement a spot-instance training job with checkpointing and measure savings.
2. Compare cost and wall-clock time of spot vs. on-demand for the same workload.
3. Create a cost dashboard with tags and identify the top-3 spend drivers.

## References

- https://arxiv.org/abs/2307.12479
- https://aws.amazon.com/blogs/compute/introducing-price-capacity-optimized-allocation-strategy-for-ec2-spot-instances/
- https://www.finops.org/wg/scaling-kubernetes-for-ai-ml-workloads-with-finops/
- https://learn.microsoft.com/en-us/cloud-computing/finops/
- https://azure.microsoft.com/en-us/blog/cloud-cost-optimization-how-to-maximize-roi-from-ai-manage-costs-and-unlock-real-business-value/
