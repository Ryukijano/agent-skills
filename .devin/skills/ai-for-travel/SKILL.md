# AI for Travel

## Description

Use AI to plan itineraries, recommend points of interest, personalize flights and hotels, and handle real-time disruptions within budget.

## When to use

You want to plan a trip, recommend points of interest, build an itinerary, or personalize travel options within time and budget constraints.

## Usage

- Recommend attractions and restaurants from user history and constraints.
- Build optimized day-by-day itineraries under time and budget.
- Adapt plans to weather, events, cancellations, and group preferences.
- Use LLM agents with live data for conversational travel planning.

## Steps

1. Collect traveler preferences, budget, dates, and accessibility needs.
2. Gather real-time POI, weather, pricing, and transit data from APIs.
3. Solve an orienteering or routing problem for itinerary optimization.
4. Validate opening hours, realistic travel times, and fallback options.
5. Generate a shareable itinerary and update it as conditions change.

## Code pattern

```python
import itertools

# Simplified orienteering: maximize POI score within a time budget
pois = [("museum", 90, 9), ("park", 60, 7), ("cafe", 45, 5)]  # (name, time, score)
budget = 180
best = max(
    (combo for r in range(1, len(pois) + 1)
     for combo in itertools.combinations(pois, r)
     if sum(p[1] for p in combo) <= budget),
    key=lambda combo: sum(p[2] for p in combo),
    default=(),
)
print([p[0] for p in best])
```

## Tuning notes

- Account for realistic travel times and attraction opening hours.
- Balance personalization with serendipity and group fairness.
- Verify bookings, prices, and availability through live APIs or links.
- Include fallback options for weather or cancellation.

## Verification

1. Build a one-day city itinerary that respects time and budget constraints.
2. Recommend POIs based on a small set of past trips and user ratings.
3. Compare an LLM-generated plan to a solver-based baseline on feasibility.

## References

- https://aclanthology.org/2025.acl-long.1339.pdf
- https://link.springer.com/article/10.1007/s40558-025-00318-2
- https://link.springer.com/article/10.1007/s44443-025-00178-0
- https://www.mdpi.com/2079-9292/14/10/2077
- https://arxiv.org/abs/2409.08069
