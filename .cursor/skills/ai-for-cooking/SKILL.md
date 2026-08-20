# AI for Cooking

## Description

Recipe generation, meal planning, ingredient substitution, food image recognition, and personalized nutrition-aware cooking assistance.

## When to use

You want to generate recipes from available ingredients, plan weekly meals, substitute items for dietary needs, or estimate nutrition from a photo.

## Key concepts

- **Food image recognition**: identify dishes and ingredients from photos.
- **Recipe generation and understanding**: text-to-recipe and ingredient-to-instruction mapping.
- **Ingredient decomposition and substitution**: break down compound ingredients and swap for allergies or preferences.
- **Nutritional optimization**: balance macronutrients and dietary guidelines across a meal plan.
- **Multimodal food computing**: combine vision, text, and structured nutrition data.

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
