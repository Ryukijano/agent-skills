# AI for Cooking

## Description

Generate personalized recipes and meal plans that account for dietary restrictions, available ingredients, and nutrition goals.

## When to use

You want to generate recipes from available ingredients, plan weekly meals, substitute items for dietary needs, or estimate nutrition from a photo.

## Usage

- Generate recipes from pantry lists and dietary goals.
- Identify dishes and ingredients from photos and estimate portions.
- Substitute ingredients for allergies, intolerances, and cultural preferences.
- Optimize weekly meal plans for macros and dietary guidelines.

## Steps

1. Catalog pantry, appliances, dietary restrictions, and user goals.
2. Look up nutritional values in a trusted database rather than generating them.
3. Generate or adapt recipes, checking cook times and allergen safety.
4. Validate output against reviewed recipes and food-safety rules.
5. Build a weekly meal plan and shopping list with macro targets.

## Code pattern

```python
import requests

# Look up a food item in USDA FoodData Central
api_key = "YOUR_API_KEY"
response = requests.get(
    f"https://api.nal.usda.gov/fdc/v1/foods/search?query=chicken&api_key={api_key}"
)
data = response.json()
```

## Tuning notes

- Verify nutritional values against a reliable database; do not trust generated numbers.
- Respect allergies, intolerances, and cultural or religious dietary rules.
- Handle missing ingredients gracefully with safe, tested substitutions.
- Test generated recipes for step coherence and safety (e.g., cook times).

## Verification

1. Generate a recipe from a pantry list and a dietary goal.
2. Classify a food image and estimate calories, then compare to a database entry.
3. Swap one ingredient and show the change in macros and allergens.

## References

- https://www.mdpi.com/2072-6643/17/9/1492
- https://ojs.aaai.org/index.php/AAAI/article/view/35359
- https://arxiv.org/abs/2406.13714
- https://arxiv.org/abs/2408.16889
- https://doi.org/10.1145/3627673.3679885
