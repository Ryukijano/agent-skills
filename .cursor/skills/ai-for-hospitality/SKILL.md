# AI for Hospitality

## Description

AI for guest personalization, revenue management, dynamic pricing, operations, and conversational service.

## When to use

You are running hotels, restaurants, events, or travel services and need to forecast demand, set prices, staff operations, or personalize guest interactions.

## Key concepts

- **RevPAR and demand forecasting**: time-series models with seasonality, events, and competitor data.
- **Dynamic pricing and availability optimization**: adjust rates in real time based on demand signals.
- **NLP for reviews and chatbots**: sentiment, topic extraction, and conversational concierge.
- **Customer segmentation and personalization**: target offers, room upgrades, and loyalty rewards.
- **Workforce scheduling and maintenance**: optimize staffing and housekeeping routes.

## Code pattern

```python
from prophet import Prophet

df = df.rename(columns={"date": "ds", "bookings": "y"})
m = Prophet(
    yearly_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode="multiplicative",
)
m.fit(df)
future = m.make_future_dataframe(periods=30)
forecast = m.predict(future)
```

## Tuning notes

- Add holidays, events, competitor rates, and weather as regressors.
- Use chronological splits; do not leak future booking data into training.
- Calibrate price sensitivity with controlled A/B tests.
- Protect guest privacy and comply with GDPR and hospitality data policies.

## Verification

1. Forecast daily RevPAR and measure MAPE against actuals.
2. Run a dynamic-pricing A/B test and compare revenue lift to a baseline.
3. Build a review-sentiment model and align it with guest NPS.

## References

- https://doi.org/10.11591/ijai.v15.i3.pp2024-2040
- https://www.bcg.com/publications/2026/ai-first-hotels-leaner-faster-smarter
- https://doi.org/10.1177/10963480231188663
- https://doi.org/10.47941/jmh.1957
