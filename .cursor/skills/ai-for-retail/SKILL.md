# AI for Retail

## Description

Demand forecasting, inventory placement, personalized recommendations, dynamic pricing, and omnichannel fulfillment for retail.

## When to use

You are optimizing retail operations across merchandising, supply chain, pricing, and customer experience.

## Key concepts

- **Omnichannel demand forecasting**: integrate store, online, and marketplace data.
- **Inventory and fulfillment**: allocate stock across stores, DCs, and dark stores for fast fulfillment.
- **Personalization and search**: recommendations, visual search, and conversational commerce.
- **Dynamic pricing and promotions**: react to competition, stock levels, and customer segments.

## Code pattern

```python
from prophet import Prophet

# Store-level demand forecast
df = df.rename(columns={"date": "ds", "sales": "y"})
m = Prophet(seasonality_mode="multiplicative")
m.fit(df)

future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
```

## Tuning notes

- Retail time series are noisy and event-driven; include promotions, holidays, and competitor pricing.
- Use hierarchical reconciliation to keep store, category, and chain forecasts consistent.
- Balance personalization with inventory availability and margin constraints.

## Verification

1. Build a product-level demand forecast and evaluate on a heldout period with promotions.
2. Test an inventory rebalancing policy against a baseline allocation rule.
3. Run a personalized recommendation or pricing experiment and measure revenue impact.

## References

- https://blogs.nvidia.com/blog/ai-in-retail-cpg-survey-2026/
- https://www.scmr.com/article/ai-is-moving-omnichannel-closer-to-the-customer
- https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2023/kpmg-generative-ai-consumer-retail-survey-report.pdf
- https://s48401.pcdn.co/wp-content/uploads/2025/11/eTailInsights2025TheRetailAIRevolutionRPT7_final.pdf
