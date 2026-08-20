SKILLS = [
    {
        "name": "ai-for-economics",
        "title": "AI for Economics",
        "description": "Causal inference, policy evaluation, nowcasting, heterogeneous treatment effects, and demand estimation for economic and policy analysis.",
        "devin_body": r'''
## When to use

You are evaluating economic policies, estimating treatment effects, nowcasting macro indicators, or modeling consumer/worker behavior from observational or panel data.

## Key concepts

- **Causal ML**: use machine learning to estimate average and heterogeneous treatment effects (e.g., causal forests, double/debiased machine learning).
- **Policy evaluation without controls**: forecast counterfactual outcomes for treated units using pre-treatment data and ML forecasters.
- **Nowcasting**: predict current-quarter GDP, inflation, or employment before official releases by combining high-frequency data.
- **Demand and elasticity estimation**: recover price/causal effects on demand with endogeneity controls.

## Code pattern

```python
import pandas as pd
from econml.dml import LinearDML
from sklearn.ensemble import GradientBoostingRegressor

# Causal effect of a policy/treatment on an outcome
Y = df["outcome"]
T = df["treatment"]
X = df[["region", "pre_trend", "demographic"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(),
    model_t=GradientBoostingRegressor(),
)
est.fit(Y, T, X=X)
print("ATE:", est.ate_)
print("CATE intervals:", est.ate__interval())
```

## Tuning notes

- Use out-of-fold nuisance predictions and cross-fitting to avoid overfitting in causal ML.
- For nowcasting, prefer models that handle ragged edges and mixed frequencies (factor models, MIDAS, LSTM).
- Validate counterfactual forecasts with placebo tests and pre-trend checks.

## Verification

1. Replicate a difference-in-differences or synthetic-control result with a causal ML estimator.
2. Build a nowcast of a macro variable and compare to a benchmark AR model.
3. Estimate a price elasticity and test robustness to confounders.
''',
        "references": [
            "https://doi.org/10.1146/annurev-economics-080217-053433",
            "https://arxiv.org/html/2312.05858v2",
            "https://arxiv.org/html/2208.03489",
            "https://www.annualreviews.org/content/journals/10.1146/annurev-economics-080217-053214",
        ],
    },
    {
        "name": "ai-for-marketing",
        "title": "AI for Marketing",
        "description": "Customer segmentation, personalization, propensity modeling, marketing-mix attribution, and generative AI for content and campaigns.",
        "devin_body": r'''
## When to use

You need to target customers more precisely, personalize messages, allocate marketing budget, or measure campaign effectiveness.

## Key concepts

- **Customer segmentation**: RFM, clustering, and behavioral segmentation to identify actionable personas.
- **Propensity and uplift modeling**: predict likelihood to buy or respond to a treatment; target those most persuadable.
- **Marketing attribution**: assign credit across touchpoints using rule-based, data-driven, or causal methods.
- **Generative AI for creative**: LLMs and diffusion models for copy, images, and dynamic creative assembly.

## Code pattern

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# RFM-style customer segmentation
X = df[["recency_days", "frequency", "monetary_value"]]
X_scaled = StandardScaler().fit_transform(X)
clusters = KMeans(n_clusters=4, random_state=42, n_init="auto").fit_predict(X_scaled)
df["segment"] = clusters
```

## Tuning notes

- Segmentations are only useful if they are stable and lead to differentiated actions.
- Uplift models need randomized holdouts to validate true incremental impact.
- Use causal or doubly robust estimators for attribution, especially with sequential data.

## Verification

1. Compare a clustering-based segment to a rule-based baseline in an A/B test.
2. Build an uplift model and estimate incremental lift on a holdout set.
3. Evaluate a generative copy pipeline for relevance and brand safety.
''',
        "references": [
            "https://www.bcg.com/publications/2024/blueprint-for-ai-powered-marketing",
            "https://doi.org/10.1016/j.jbusres.2023.114254",
            "https://faculty.washington.edu/hemay/Personalization_Review.pdf",
            "https://doi.org/10.63125/x3e0dx27",
        ],
    },
    {
        "name": "ai-for-sales",
        "title": "AI for Sales",
        "description": "Predictive lead scoring, sales forecasting, opportunity win probability, next-best action, and pipeline analytics.",
        "devin_body": r'''
## When to use

You want to prioritize leads, forecast revenue, reduce churn, or guide sales reps toward the next best action.

## Key concepts

- **Predictive lead scoring**: estimate conversion probability from firmographic and engagement signals.
- **Pipeline forecasting**: time-series or classification models to predict bookings and close dates.
- **Opportunity win probability**: models updated with CRM stage, activity, and sentiment features.
- **Next-best action**: recommend the next call, email, content, or offer to advance a deal.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

X = df[["email_opens", "demo_attended", "company_size", "page_views"]]
y = df["converted"]

model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["lead_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use chronological splits to avoid leakage from future activities into lead scores.
- Calibrate probabilities so sales teams can trust score thresholds.
- Refresh models frequently because buyer behavior and market conditions shift.

## Verification

1. Train a lead-scoring model and compare conversion lift over a rule-based baseline.
2. Build a weekly sales forecast and measure MAPE against actuals.
3. Test a next-best-action recommendation in a field pilot.
''',
        "references": [
            "https://doi.org/10.3390/forecast6030028",
            "https://learn.microsoft.com/en-us/dynamics365/sales/work-predictive-lead-scoring",
            "https://docs.oracle.com/en/cloud/saas/sales/fasqa/how-does-the-ai-lead-score-get-calculated.html",
            "https://www.malque.pub/ojs/index.php/mr/article/view/10728",
        ],
    },
    {
        "name": "ai-for-hr",
        "title": "AI for Human Resources",
        "description": "Talent analytics, recruitment matching, attrition prediction, workforce planning, and compensation and equity analysis.",
        "devin_body": r'''
## When to use

You are optimizing hiring, predicting turnover, matching candidates to roles, or analyzing workforce composition and pay equity.

## Key concepts

- **Talent analytics**: data-driven insights for recruitment, retention, and development.
- **Attrition prediction**: classification models to identify flight-risk employees.
- **Resume-job matching**: semantic similarity using embeddings and dense retrieval.
- **Pay and promotion equity**: statistical tests and models to detect disparities across groups.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["age", "job_satisfaction", "overtime", "tenure", "salary_level"]]
y = df["attrition"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- HR models are high-stakes; ensure fairness, explainability, and legal compliance.
- Attrition labels are often imbalanced; use resampling or cost-sensitive learning.
- Audit hiring models for adverse impact on protected groups.

## Verification

1. Train an attrition model and evaluate recall for at-risk employees.
2. Build a resume-to-job matching pipeline and measure top-k accuracy.
3. Run an equity analysis on compensation or promotion outcomes.
''',
        "references": [
            "https://arxiv.org/html/2307.03195",
            "https://link.springer.com/article/10.1186/s43093-025-00704-6",
            "https://doi.org/10.1016/j.fraope.2026.100673",
            "https://oracle.com/human-capital-management/analytics/",
        ],
    },
    {
        "name": "ai-for-operations-research",
        "title": "AI for Operations Research",
        "description": "Optimization, MILP/CP, vehicle routing and scheduling, decision-focused learning, and learning-augmented heuristics.",
        "devin_body": r'''
## When to use

You need to make optimal or near-optimal decisions under constraints for routing, scheduling, resource allocation, or network design.

## Key concepts

- **Mathematical programming**: LP, MILP, and constraint programming for feasibility and optimality.
- **Combinatorial optimization augmented ML**: embed optimization oracles inside learning pipelines.
- **Learning for routing and scheduling**: GNNs and reinforcement learning to learn heuristics for TSP/VRP/job shop.
- **Decision-focused learning**: train models with losses that account for downstream optimization costs.

## Code pattern

```python
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver.CreateSolver("GLOP")
x = solver.NumVar(0, 10, "x")
y = solver.NumVar(0, 10, "y")

solver.Add(2 * x + y <= 10)
solver.Maximize(3 * x + 4 * y)
status = solver.Solve()

print(solver.Objective().Value())
print(x.solution_value(), y.solution_value())
```

## Tuning notes

- Choose exact solvers when problem size permits; otherwise use metaheuristics or learned heuristics.
- In decision-focused learning, backpropagate through the optimization layer with care.
- Validate learned policies against strong OR baselines (e.g., LKH, CP-SAT).

## Verification

1. Solve a small MILP and compare the objective to a greedy baseline.
2. Train a learned heuristic for a routing problem and benchmark against a classical solver.
3. Implement decision-focused learning and show improvement over two-stage predict-then-optimize.
''',
        "references": [
            "https://arxiv.org/html/2601.10583",
            "https://arxiv.org/pdf/2507.00218",
            "https://ojmo.centre-mersenne.org/item/10.5802/ojmo.43.pdf",
            "https://link.springer.com/article/10.1007/s10994-026-07116-9",
        ],
    },
    {
        "name": "ai-for-supply-chain-optimization",
        "title": "AI for Supply Chain Optimization",
        "description": "Multi-echelon inventory, distribution network design, demand-supply synchronization, and resilient supply chain planning.",
        "devin_body": r'''
## When to use

You are designing distribution networks, setting inventory policies, synchronizing supply with demand, or mitigating disruption risk.

## Key concepts

- **Multi-echelon inventory optimization**: coordinate stock levels across warehouses, plants, and retailers.
- **Distribution network design**: facility location, allocation, and transportation trade-offs under demand uncertainty.
- **Demand-supply synchronization**: RL and digital twins to adapt to stochastic, non-stationary environments.
- **Resilience and risk**: scenario optimization and robustness to disruptions.

## Code pattern

```python
import pulp

# Simple warehouse-allocation MILP
prob = pulp.LpProblem("NetworkDesign", pulp.LpMinimize)
open_wh = pulp.LpVariable.dicts("open", warehouses, cat="Binary")
ship = pulp.LpVariable.dicts("ship", (warehouses, customers), lowBound=0)

# Objective: fixed opening + transportation costs
prob += pulp.lpSum([fixed_cost[w] * open_wh[w] for w in warehouses]) + \
        pulp.lpSum([cost[w][c] * ship[w][c] for w in warehouses for c in customers])

# Demand satisfaction
for c in customers:
    prob += pulp.lpSum([ship[w][c] for w in warehouses]) == demand[c]

prob.solve()
```

## Tuning notes

- Combine forecasting and optimization; small forecast errors can have large downstream cost effects.
- Use safety stock and robustness to protect against demand and lead-time uncertainty.
- RL policies need careful simulation environments before production deployment.

## Verification

1. Formulate and solve a multi-warehouse allocation problem with real cost data.
2. Compare an RL inventory policy to a base-stock policy in simulation.
3. Stress-test the supply chain against disruption scenarios.
''',
        "references": [
            "https://www.mdpi.com/1424-8220/25/8/2428",
            "https://www.mdpi.com/1999-4893/14/8/240",
            "https://link.springer.com/article/10.1007/s10100-023-00872-2",
            "https://iieta.org/journals/mmep/paper/10.18280/mmep.130403",
        ],
    },
    {
        "name": "ai-for-demand-forecasting",
        "title": "AI for Demand Forecasting",
        "description": "Time-series forecasting, hierarchical and intermittent demand, probabilistic forecasts, and promotion/event effects.",
        "devin_body": r'''
## When to use

You need to predict future demand for products, services, or resources to drive inventory, staffing, production, or pricing decisions.

## Key concepts

- **Statistical baselines**: ARIMA, ETS, Prophet, and Theta for structured seasonality.
- **ML/DL forecasting**: gradient boosting, LSTM, CNN, transformers, and N-BEATS for complex patterns.
- **Hierarchical and intermittent demand**: reconcile forecasts across levels and handle sparse/zero-inflated series.
- **Probabilistic forecasting**: prediction intervals and quantile forecasts for decision-making under uncertainty.

## Code pattern

```python
from statsforecast import StatsForecast
from statsforecast.models import AutoARIMA, Naive

sf = StatsForecast(
    df=df,
    models=[AutoARIMA(season_length=12), Naive()],
    freq="M",
    n_jobs=-1,
)
forecasts = sf.forecast(h=12)
```

## Tuning notes

- Match model choice to data frequency, seasonality, and horizon; benchmark against strong baselines.
- For promotions and events, include causal features and avoid future leakage.
- Evaluate with scale-independent metrics (MAPE, RMSSE, M5-style metrics).

## Verification

1. Build a demand forecast and backtest with rolling cross-validation.
2. Compare a tree-based, deep-learning, and statistical model on the same series.
3. Generate prediction intervals and check coverage on a holdout period.
''',
        "references": [
            "https://www.mdpi.com/2571-5577/7/5/93",
            "https://nixtlaverse.nixtla.io/statsforecast/docs/getting-started/getting_started_complete.html",
            "https://doi.org/10.1016/j.aei.2026.104625",
            "https://www.sciencedirect.com/science/article/pii/S2212827122004036",
        ],
    },
    {
        "name": "ai-for-pricing",
        "title": "AI for Pricing",
        "description": "Price elasticity, dynamic and personalized pricing, revenue management, promotion optimization, and causal demand forecasting for pricing.",
        "devin_body": r'''
## When to use

You need to set or adjust prices to maximize revenue, margin, or market share while accounting for demand response and competitive effects.

## Key concepts

- **Price elasticity**: estimate how quantity demanded changes with price, often via log-log regression or causal ML.
- **Dynamic pricing**: adjust prices in real time based on demand, inventory, and competitor signals.
- **Revenue management**: capacity control, overbooking, and fare-class optimization.
- **Causal pricing**: off-policy learning and DML to forecast demand under new price regimes.

## Code pattern

```python
import numpy as np
import pandas as pd
import statsmodels.api as sm

# Log-log model for price elasticity
df["log_q"] = np.log(df["quantity"])
df["log_p"] = np.log(df["price"])
X = sm.add_constant(df[["log_p", "log_income", "promo"]])

model = sm.OLS(df["log_q"], X).fit()
print("Elasticity:", model.params["log_p"])
```

## Tuning notes

- Address price endogeneity with instrumental variables, randomized experiments, or DML.
- Consider business rules: price fences, fairness, and customer perception.
- Test new pricing policies with controlled experiments or counterfactual evaluation before rollout.

## Verification

1. Estimate a price elasticity and validate on an experimental price change.
2. Build a dynamic pricing simulator and optimize for revenue under demand uncertainty.
3. Compare a causal pricing model to a pure forecast model in an off-policy test.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2312.15282",
            "https://doi.org/10.1057/s41272-024-00478-6",
            "https://proceedings.mlr.press/v202/simchi-levi23a/simchi-levi23a.pdf",
            "https://www.sciencedirect.com/science/article/abs/pii/S0278431921000578",
        ],
    },
    {
        "name": "ai-for-fraud-detection",
        "title": "AI for Fraud Detection",
        "description": "Transaction fraud, anti-money laundering, anomaly detection, graph-based fraud networks, and concept-drift monitoring.",
        "devin_body": r'''
## When to use

You need to detect fraudulent payments, accounts, claims, or transactions in real time while minimizing false positives.

## Key concepts

- **Supervised fraud classification**: tree ensembles and neural nets on labeled fraud cases.
- **Anomaly detection**: isolation forests, autoencoders, and one-class methods for unknown fraud patterns.
- **Graph-based detection**: GNNs to exploit account, device, and merchant networks.
- **Concept drift and adversaries**: fraud patterns evolve; monitor model performance and adversarial behavior.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

X = df.drop("is_fraud", axis=1)
clf = IsolationForest(contamination=0.01, random_state=42)
clf.fit(X)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Fraud data is extremely imbalanced; use stratified sampling, class weights, or cost-sensitive loss.
- Use time-based splits and chronological validation to avoid leakage.
- Combine graph structure with behavioral features for network-based fraud.

## Verification

1. Train a fraud classifier and report precision-recall at the top-decile.
2. Build a graph feature extractor and measure lift over tabular features.
3. Deploy a drift monitor and simulate an adversarial shift.
''',
        "references": [
            "https://arxiv.org/html/2307.05633",
            "https://doi.org/10.3390/app16041931",
            "https://www.mdpi.com/1911-8074/19/1/14",
            "https://ar5iv.labs.arxiv.org/html/2411.05815",
        ],
    },
    {
        "name": "ai-for-recommendation-systems",
        "title": "AI for Recommendation Systems",
        "description": "Collaborative filtering, content-based and hybrid recommendation, sequence models, and multi-objective ranking for commerce and content.",
        "devin_body": r'''
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
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2412.01378",
            "https://www.mdpi.com/2076-3417/13/20/11378",
            "https://link.springer.com/article/10.1007/s00521-024-10866-z",
            "https://www.sciencedirect.com/science/article/abs/pii/S0925231224014899",
        ],
    },
    {
        "name": "ai-for-customer-service",
        "title": "AI for Customer Service",
        "description": "Conversational AI, intent classification, sentiment and satisfaction analysis, ticket routing, and agent-assist systems.",
        "devin_body": r'''
## When to use

You want to automate customer support, triage tickets, route inquiries, or augment human agents with real-time suggestions.

## Key concepts

- **Intent classification and slot filling**: map user utterances to intents and extract entities.
- **Conversational AI and LLMs**: chatbots, retrieval-augmented generation, and human escalation.
- **Sentiment and user satisfaction**: detect frustration, satisfaction, and conversation quality.
- **Ticket routing and agent assist**: classify and route to the right team or suggest responses.

## Code pattern

```python
from transformers import pipeline

# Sentiment analysis for customer messages
classifier = pipeline("sentiment-analysis")
result = classifier("The chatbot resolved my issue in seconds.")
print(result)
```

## Tuning notes

- Design for graceful handoff to human agents when automation fails.
- Use retrieval-augmented generation to ground answers in approved knowledge bases.
- Track resolution rate, CSAT, and cost per contact to measure real value.

## Verification

1. Build an intent classifier and measure F1 on a labeled test set.
2. Deploy a chatbot and compare resolution rate to the previous channel.
3. Run a sentiment/satisfaction model and validate against post-interaction surveys.
''',
        "references": [
            "https://www.mdpi.com/2076-3417/15/17/9439",
            "https://arxiv.org/html/2403.12388",
            "https://www.copc.com/ai-customer-experience-research-2025/",
            "https://aclanthology.org/2026.acl-industry.121/",
        ],
    },
    {
        "name": "ai-for-retail",
        "title": "AI for Retail",
        "description": "Demand forecasting, inventory placement, personalized recommendations, dynamic pricing, and omnichannel fulfillment for retail.",
        "devin_body": r'''
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
''',
        "references": [
            "https://blogs.nvidia.com/blog/ai-in-retail-cpg-survey-2026/",
            "https://www.scmr.com/article/ai-is-moving-omnichannel-closer-to-the-customer",
            "https://kpmg.com/kpmg-us/content/dam/kpmg/pdf/2023/kpmg-generative-ai-consumer-retail-survey-report.pdf",
            "https://s48401.pcdn.co/wp-content/uploads/2025/11/eTailInsights2025TheRetailAIRevolutionRPT7_final.pdf",
        ],
    },
]
