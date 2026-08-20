# AI for Recommendation Systems

## Description

Collaborative filtering, content-based and hybrid recommendation, sequence models, and multi-objective ranking for commerce and content.

## When to use

You need to recommend products, content, jobs, or services to users in e-commerce, media, marketplaces, or social platforms.

## Key concepts

- **Collaborative filtering**: matrix factorization, item-to-item, and neural collaborative filtering.
- **Content-based and hybrid**: combine item/user features with interaction signals.
- **Sequential recommendation**: capture session dynamics with RNNs, transformers, or session-based models.
- **Multi-objective ranking**: balance relevance, diversity, freshness, fairness, and business constraints.

## Code pattern

```python
from surprise import SVD, Dataset, Reader

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[["user_id", "item_id", "rating"]], reader)
trainset = data.build_full_trainset()

model = SVD().fit(trainset)
pred = model.predict(uid="user_123", iid="item_456")
```

## Tuning notes

- Handle cold-start users and items with content features or popularity fallbacks.
- Evaluate ranking with metrics like nDCG, MAP, and hit rate rather than just rating RMSE.
- Monitor for filter bubbles, popularity bias, and fairness in recommendations.

## Verification

1. Train a collaborative filtering model and evaluate ranking quality on a heldout set.
2. Add side information and measure cold-start improvement.
3. Test a sequential model against a static baseline in an A/B test.

## References

- https://doi.org/10.48550/arxiv.2412.01378
- https://www.mdpi.com/2076-3417/13/20/11378
- https://link.springer.com/article/10.1007/s00521-024-10866-z
- https://www.sciencedirect.com/science/article/abs/pii/S0925231224014899
