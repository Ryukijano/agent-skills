# AI for Urban Planning

## Description

Generates land-use scenarios and simulates urban growth to balance density, accessibility, and sustainability.

## When to use

You are developing land-use plans, simulating urban growth, designing neighborhoods, or engaging communities in planning.

## Usage

- **Land-use optimization**: allocate residential, commercial, and green spaces across scenarios.
- **Urban digital twins**: simulate mobility, energy, and environmental impacts at city scale.
- **Scenario simulation**: test zoning, density, and infrastructure options using agent-based and cellular models.
- **Participatory planning**: analyze public input and design trade-offs with stakeholder feedback.

## Steps

1. Define planning goals, constraints, and stakeholder objectives.
2. Collect geospatial, demographic, environmental, and mobility data.
3. Build or use spatial optimization and simulation models.
4. Co-design scenarios with planners and the public.
5. Evaluate alternatives on equity, sustainability, and feasibility.

## Code pattern

```python
import geopandas as gpd

# Compute zoning compliance area for a parcel
gdf = gpd.read_file("parcels.geojson")
gdf["allowed_units"] = (gdf["area_m2"] * gdf["floor_area_ratio"]) / gdf["unit_size"]
print(gdf[["parcel_id", "allowed_units"]].head())
```

## Tuning notes

- Combine AI suggestions with professional planner judgment.
- Validate model outputs with community priorities and legal constraints.
- Use high-quality, interoperable geospatial data.

## Verification

1. Generate a set of spatial plans and compare to expert designs.
2. Simulate a policy scenario and compare predicted outcomes.
3. Conduct a participatory review of AI-assisted alternatives.

## References

- https://www.nature.com/articles/s43588-025-00846-1
- https://www.nature.com/articles/s43588-023-00503-5
- https://www.mdpi.com/2073-445X/12/7/1315
- https://www.sciencedirect.com/science/article/abs/pii/S0169204625000441
