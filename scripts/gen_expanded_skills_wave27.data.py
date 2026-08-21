SKILLS = [
    {
        "name": "ai-for-personal-finance",
        "title": "AI for Personal Finance",
        "description": 'Use machine learning to categorize transactions, forecast cash flow, build robo-advisory portfolios, and guide debt and savings decisions for households.',
        "devin_body": r'''## When to use

You want to manage household budgets, forecast cash flow, choose an investment allocation, or get personalized savings and debt-payoff guidance.

## Usage

- Categorize bank and credit-card transactions into budgets automatically.
- Forecast income, bills, and discretionary cash flow over weeks to months.
- Construct and rebalance risk-profiled investment portfolios.
- Score credit risk and optimize savings toward personal goals.

## Steps

1. Connect and label transaction data with strict encryption and on-device processing where possible.
2. Train a categorization or forecasting model with chronological train/test splits.
3. Backtest cash-flow and portfolio recommendations against historical behavior.
4. Calibrate risk and explain fees, taxes, and liquidity trade-offs.
5. Deliver personalized nudges and rebalancing alerts with opt-out controls.

## Code pattern

```python
import pandas as pd
import cvxpy as cp

# Simple goal-based savings allocation
income = 5000
bills = 2000
discretionary = income - bills
goals = {"emergency_fund": 300, "vacation": 200, "retirement": 400}

# Verify allocation fits within budget
assert sum(goals.values()) <= discretionary
```

## Tuning notes

- Use chronological train/test splits to avoid look-ahead in cash-flow forecasts.
- Keep sensitive financial data encrypted and on-device when possible.
- Calibrate robo-advisor risk questionnaires against actual drawdown behavior.
- Explain trade-offs in fees, taxes, and liquidity before recommending products.

## Verification

1. Categorize a month of transactions and compare to manual labels.
2. Build a 30-day cash-flow forecaster and backtest on a holdout month.
3. Propose a portfolio allocation for a given risk profile and rebalance rule.
''',
        "references": [
            "https://www.mdpi.com/2673-2688/5/1/6",
            "https://doi.org/10.3386/w35574",
            "https://doi.org/10.1109/icmla52953.2021.00063",
            "https://www.sciencedirect.com/science/article/abs/pii/S0957417421005017",
        ],
    },
    {
        "name": "ai-for-legal-assistance",
        "title": "AI for Legal Assistance",
        "description": 'Use NLP to triage legal questions, summarize contracts, flag risky clauses, and help non-experts fill forms and find the right jurisdiction.',
        "devin_body": r'''## When to use

You need to understand a contract, fill out a legal form, triage a civil legal issue, or summarize a legal document without immediate access to a lawyer.

## Usage

- Extract clauses, entities, and obligations from contracts and leases.
- Summarize legal documents into plain language and redline suggestions.
- Triage intake queries to relevant legal topics and services.
- Ground answers in statutes, forms, and verified FAQs with RAG.

## Steps

1. Collect the document or user query and identify the relevant jurisdiction.
2. Run a clause-extraction or summarization model with a disclaimer that it is not legal advice.
3. Retrieve statutes or form templates from verified sources.
4. Flag high-risk terms and generate redline or plain-language explanations.
5. Escalate complex or high-stakes matters to a licensed attorney.

## Code pattern

```python
from transformers import pipeline

# Summarize a contract clause and extract key terms
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
clause = "..."
summary = summarizer(clause, max_length=60, min_length=10, do_sample=False)
```

## Tuning notes

- Always add a disclaimer that the tool is not a substitute for legal advice.
- Use retrieval from verified sources; do not generate citations from memory.
- Protect client confidentiality and avoid training on sensitive uploads.
- Validate hallucination rates on a held-out set of real legal Q&A pairs.

## Verification

1. Classify 100 legal intake queries into topic categories and compare to expert labels.
2. Summarize a lease agreement and flag any high-risk clauses.
3. Build a jurisdiction-aware FAQ agent that cites local statutes.
''',
        "references": [
            "https://arxiv.org/abs/2410.03762v1",
            "https://doi.org/10.1016/j.fmre.2026.03.026",
            "https://arxiv.org/abs/2512.04105",
            "https://arxiv.org/abs/2509.07170",
        ],
    },
    {
        "name": "ai-for-wellness",
        "title": "AI for Wellness",
        "description": 'Use machine learning to track sleep, stress, and activity, then deliver personalized wellness nudges grounded in behavior-change science.',
        "devin_body": r'''## When to use

You want to monitor sleep, stress, activity, and mood, then deliver personalized wellness nudges grounded in behavior-change science.

## Usage

- Fuse wearable, EMA, and sleep-diary signals into wellness scores.
- Model stress from HRV, activity, and sleep patterns.
- Classify sleep stages and recommend hygiene habits.
- Personalize mindfulness and habit-nudge interventions.

## Steps

1. Ingest wearable, sleep, and self-report data with user consent.
2. Align time-series signals and compute validated features.
3. Train a stress, sleep, or wellness model and validate against scales like PSS, PSQI, WHO-5.
4. Generate personalized recommendations and explain the reasoning.
5. Let users opt out, adjust goals, and avoid alarm fatigue.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Simple stress classifier from HRV and sleep features
X = np.column_stack([hrv_rmssd, sleep_hours, steps])
y = stress_label
clf = RandomForestClassifier(n_estimators=100).fit(X, y)
```

## Tuning notes

- Align wearables and self-reports; neither alone captures wellness fully.
- Avoid over-monitoring and alarm fatigue; respect user autonomy.
- Validate recommendations with validated scales (PSS, PSQI, WHO-5).
- Keep health data encrypted and allow users to delete their history.

## Verification

1. Predict next-day self-reported stress from HRV and sleep features.
2. Recommend a mindfulness session and measure change in PSS or session rating.
3. Build a personalized sleep-hygiene plan and track sleep duration over two weeks.
''',
        "references": [
            "https://pubmed.ncbi.nlm.nih.gov/40748022/",
            "https://doi.org/10.1145/3706598.3713852",
            "https://doi.org/10.1145/3772318.3791817",
            "https://www.nature.com/articles/s41598-026-37028-6",
        ],
    },
    {
        "name": "ai-for-fitness",
        "title": "AI for Fitness",
        "description": 'Use machine learning to build adaptive workout plans, count reps, check exercise form, and prevent injury from wearable and video feedback.',
        "devin_body": r'''## When to use

You want to build personalized workouts, count reps, check exercise form, or adapt a training plan from wearable and video feedback.

## Usage

- Estimate exercise pose and count reps from camera or IMU data.
- Classify human activities and exercises from wearables.
- Adapt training volume and recovery based on progress and fatigue.
- Flag excessive range of motion, asymmetry, or load spikes.

## Steps

1. Collect video, IMU, or wearable data during a set of exercises.
2. Calibrate pose estimation or activity recognition for the user's body and camera.
3. Train a rep-counting or form-deviation model on diverse participants.
4. Validate against manual counts and expert form assessments.
5. Adjust the workout plan based on completion, fatigue, and injury signals.

## Code pattern

```python
import mediapipe as mp
import cv2

# Capture a frame and estimate pose landmarks
cap = cv2.VideoCapture("squat.mp4")
ret, frame = cap.read()
pose = mp.solutions.pose.Pose()
results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
landmarks = results.pose_landmarks
```

## Tuning notes

- Calibrate pose estimation for camera angle, lighting, and body proportions.
- Combine IMU and video signals for robustness to occlusion.
- Respect fatigue and injury signals; never override user-reported pain.
- Test algorithms on diverse ages, abilities, and exercise environments.

## Verification

1. Count repetitions of a bodyweight exercise and compare to manual counts.
2. Detect a form deviation (e.g., knee valgus in a squat) on a short video.
3. Build a weekly workout plan that adapts based on completion and heart-rate data.
''',
        "references": [
            "https://www.sciencedirect.com/science/article/pii/S1110016825006970",
            "https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2026.1785114/full",
            "https://dl.acm.org/doi/fullHtml/10.1145/3654777.3676461",
            "https://www.mdpi.com/2227-9032/14/4/482",
        ],
    },
    {
        "name": "ai-for-mental-health",
        "title": "AI for Mental Health",
        "description": 'Use AI to deliver low-intensity CBT support, track mood, triage crisis risk, and keep human clinicians in the loop for escalation.',
        "devin_body": r'''## When to use

You are building or using a consumer mental-health tool that offers CBT techniques, mood tracking, crisis triage, or low-intensity support.

## Usage

- Deliver CBT and DBT techniques through structured conversational prompts.
- Track mood and EMA scores with validated instruments such as PHQ-9 and GAD-7.
- Detect crisis language and route to human help and emergency resources.
- Build rapport and personalize engagement over time.

## Steps

1. Onboard the user with clear disclaimers and 24/7 crisis hotlines.
2. Collect mood, sleep, and activity data with privacy controls.
3. Deploy CBT worksheets or chatbot interactions tied to evidence-based techniques.
4. Monitor for deterioration or crisis indicators and trigger human escalation.
5. Validate outcomes with clinical measures and continuously audit safety.

## Code pattern

```python
import pandas as pd

# Simple mood trend and crisis alert
mood = pd.Series([4, 3, 2, 2, 1, 1, 0])
if mood.tail(3).mean() < 1.5:
    print("Escalate to crisis resources")
```

## Tuning notes

- A chatbot is not a replacement for a licensed therapist or emergency services.
- Include clear safety disclaimers and 24/7 crisis hotlines.
- Protect mental-health data with strong privacy and access controls.
- Validate against clinical measures and monitor for signs of deterioration.

## Verification

1. Parse a daily mood diary and visualize a 14-day trend.
2. Implement a CBT thought-record helper and check it follows the worksheet steps.
3. Build a keyword-based crisis triage and test it on safe sample messages.
''',
        "references": [
            "https://www.nature.com/articles/s41746-026-02886-x",
            "https://ai.nejm.org/doi/full/10.1056/AIoa2400802",
            "https://pmc.ncbi.nlm.nih.gov/articles/PMC11904749/",
            "https://doi.org/10.2196/mental.7785",
        ],
    },
    {
        "name": "ai-for-personal-productivity",
        "title": "AI for Personal Productivity",
        "description": 'Use AI to prioritize tasks, resolve calendar conflicts, block focus time, and automate repetitive personal workflows.',
        "devin_body": r'''## When to use

You want to prioritize tasks, resolve calendar conflicts, block focus time, or automate repetitive personal workflows.

## Usage

- Prioritize tasks with urgency/importance scoring or learned preferences.
- Resolve calendar conflicts and propose reschedules or declines.
- Block deep-work windows and protect focus time.
- Automate email triage, travel booking, and recurring task workflows.

## Steps

1. Sync calendar, task, and email data with minimal, scoped permissions.
2. Build a preference model from user edits and past decisions.
3. Generate a daily or weekly plan and compare it to the user's manual plan.
4. Propose conflict resolutions and schedule focus blocks.
5. Test on synthetic data first, then let the user approve every change.

## Code pattern

```python
# Simplified task ordering by priority (lower number = higher priority)
tasks = [("email", 3), ("planning", 2), ("deep_work", 1)]
ordered = sorted(tasks, key=lambda x: x[1])
print([t[0] for t in ordered])
```

## Tuning notes

- Learn from user edits rather than overriding their preferences.
- Respect focus time and avoid over-scheduling back-to-back meetings.
- Integrate with calendar APIs using minimal, scoped permissions.
- Test on synthetic calendars before applying to a user's real schedule.

## Verification

1. Build a daily task scheduler and compare its plan to a user's manual plan.
2. Resolve a synthetic calendar conflict using stated priorities.
3. Auto-categorize low-priority emails and measure time saved.
''',
        "references": [
            "https://aclanthology.org/2026.acl-long.1648.pdf",
            "https://arxiv.org/abs/2601.11957",
            "https://arxiv.org/abs/2509.25693",
            "https://aclanthology.org/2026.acl-long.1614.pdf",
        ],
    },
    {
        "name": "ai-for-cooking",
        "title": "AI for Cooking",
        "description": 'Generate personalized recipes and meal plans that account for dietary restrictions, available ingredients, and nutrition goals.',
        "devin_body": r'''## When to use

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
''',
        "references": [
            "https://www.mdpi.com/2072-6643/17/9/1492",
            "https://ojs.aaai.org/index.php/AAAI/article/view/35359",
            "https://arxiv.org/abs/2406.13714",
            "https://arxiv.org/abs/2408.16889",
            "https://doi.org/10.1145/3627673.3679885",
        ],
    },
    {
        "name": "ai-for-home-automation",
        "title": "AI for Home Automation",
        "description": 'Use machine learning to automate lighting and HVAC, reduce energy costs, predict occupancy, and improve comfort while preserving privacy.',
        "devin_body": r'''## When to use

You want to automate lighting, HVAC, or appliances, reduce home energy costs, or improve comfort based on occupancy and weather.

## Usage

- Schedule HVAC and appliances to minimize cost and carbon under time-of-use pricing.
- Predict occupancy from sensors, phones, and cameras.
- Shift flexible loads in response to price or grid signals.
- Learn thermostat and device policies from occupant feedback.

## Steps

1. Install and calibrate sensors for occupancy, temperature, and weather.
2. Collect historical usage, pricing, and occupant comfort data.
3. Train a scheduling or control policy with user comfort constraints.
4. Validate in simulation and allow manual override at all times.
5. Deploy locally and measure energy savings and comfort complaints.

## Code pattern

```python
import pandas as pd

# Rule-based thermostat setback when away
if occupancy == 0:
    target_temp = 18 if season == "winter" else 26
else:
    target_temp = comfort_setpoint
```

## Tuning notes

- Respect user comfort bounds and allow manual overrides at all times.
- Account for occupancy, weather, and time-of-use electricity prices.
- Run safety-critical logic on-device and never lock out physical controls.
- Evaluate both energy savings and comfort complaints.

## Verification

1. Predict occupancy from sensor patterns and compare to ground truth.
2. Schedule appliances to minimize electricity cost under time-of-use pricing.
3. Compare an RL-based thermostat policy to a rule-based baseline in simulation.
''',
        "references": [
            "https://www.mdpi.com/1996-1073/17/24/6420",
            "https://doi.org/10.1109/jiot.2022.3152586",
            "https://arxiv.org/pdf/1909.10165",
            "https://doi.org/10.1016/j.enbuild.2025.115391",
        ],
    },
    {
        "name": "ai-for-shopping",
        "title": "AI for Shopping",
        "description": 'Answer natural-language product questions and surface personalized recommendations from real-time catalog and behavior data.',
        "devin_body": r'''## When to use

You want to discover products, compare prices, summarize reviews, or build a personalized buyer guide for a consumer purchase.

## Usage

- Rank products by relevance, value, and user constraints.
- Summarize pros, cons, and recurring issues from customer reviews.
- Extract specs, dimensions, and compatibility from listings.
- Track price history and alert users to deals.

## Steps

1. Fetch real-time listings and reviews from trusted sources.
2. Parse specs, prices, and availability with grounding in source pages.
3. Train or prompt a summarizer for review pros and cons.
4. Rank options against user constraints and explain trade-offs.
5. Keep price alerts fresh and disclose affiliate or sponsored relationships.

## Code pattern

```python
from transformers import pipeline

# Summarize customer reviews for a product
reviews = "Great battery. Screen is dim. Fast shipping. ..."
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(reviews, max_length=60, min_length=10, do_sample=False)
```

## Tuning notes

- Avoid hallucinated specs; always link back to source listings.
- Disclose commercial relationships or affiliate links.
- Update prices and availability frequently; stale data misleads buyers.
- Balance personalization with transparency and user control.

## Verification

1. Summarize 50 reviews for a product category and compare to a manual summary.
2. Build a price-alert pipeline and verify it detects a price drop.
3. Compare an LLM buyer guide to a review-and-spec-based ranking.
''',
        "references": [
            "https://product.ai/research/trust-in-ai-commerce-report/",
            "https://openai.com/index/chatgpt-shopping-research/",
            "https://www.ipsos.com/sites/default/files/ct/publication/documents/2026-07/ipsos-views-shopping-with-AI.pdf",
            "https://www.pymnts.com/study_posts/the-50-million-consumer-migration-the-data-behind-retails-shift-toward-ai-discovery/",
        ],
    },
    {
        "name": "ai-for-travel",
        "title": "AI for Travel",
        "description": 'Use AI to plan itineraries, recommend points of interest, personalize flights and hotels, and handle real-time disruptions within budget.',
        "devin_body": r'''## When to use

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
''',
        "references": [
            "https://aclanthology.org/2025.acl-long.1339.pdf",
            "https://link.springer.com/article/10.1007/s40558-025-00318-2",
            "https://link.springer.com/article/10.1007/s44443-025-00178-0",
            "https://www.mdpi.com/2079-9292/14/10/2077",
            "https://arxiv.org/abs/2409.08069",
        ],
    },
    {
        "name": "ai-for-event-planning",
        "title": "AI for Event Planning",
        "description": 'Use AI to match venues and vendors, aggregate guest preferences, schedule activities, and stay within budget for events.',
        "devin_body": r'''## When to use

You want to plan a party, wedding, meeting, or community event by finding vendors, scheduling activities, managing guests, and staying within budget.

## Usage

- Aggregate attendee dietary, accessibility, and location preferences.
- Score and match vendors to event briefs and budgets.
- Schedule sessions or ceremonies under room and time constraints.
- Forecast RSVPs and no-shows from past event data.

## Steps

1. Collect event goals, budget, guest list, and constraints.
2. Gather vendor or venue options and review ratings and availability.
3. Match candidates to the brief using text similarity and budget filters.
4. Build a schedule and menu that respects dietary and accessibility needs.
5. Track RSVPs and generate a day-of run sheet with human approval for contracts.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Match vendor descriptions to event requirements
vectorizer = TfidfVectorizer().fit(vendor_descriptions + [event_requirements])
X = vectorizer.transform(vendor_descriptions + [event_requirements])
scores = cosine_similarity(X[-1:], X[:-1])
```

## Tuning notes

- Collect group preferences early and provide ranked alternatives.
- Check vendor availability, insurance, and cancellation policies.
- Handle dietary restrictions and accessibility needs explicitly.
- Keep human final approval for contracts and payments.

## Verification

1. Match a list of vendors to a sample event brief and budget.
2. Build an RSVP forecaster and evaluate on past events.
3. Schedule a multi-session event with room and time constraints.
''',
        "references": [
            "https://dl.acm.org/doi/10.1145/3314421",
            "https://doi.org/10.5281/zenodo.20046609",
            "https://doi.org/10.56741/jnest.v5i01.1050",
            "https://doi.org/10.1609/aaai.v40i19.38684",
        ],
    },
    {
        "name": "ai-for-lifestyle",
        "title": "AI for Lifestyle",
        "description": "Use AI to build habits, recommend hobbies, coach personal goals, and deliver holistic lifestyle nudges that fit a user's values.",
        "devin_body": r'''## When to use

You want to build habits, discover hobbies, coach personal goals, or deliver holistic lifestyle nudges that fit a user's context and values.

## Usage

- Model habit loops and predict dropout from adherence data.
- Recommend hobbies and activities from a short user profile.
- Test and personalize nudges with multi-armed bandits.
- Explain recommendations in terms of user values and goals.

## Steps

1. Elicit user values, goals, and constraints through a short onboarding.
2. Track habit completion and objective adherence, not just engagement.
3. Train a personalization or bandit model to select nudges.
4. Validate with self-report and adherence metrics.
5. Let users contest, adjust, or stop nudges at any time.

## Code pattern

```python
import numpy as np

# Epsilon-greedy bandit for choosing daily nudges
nudges = ["walk", "read", "meditate"]
rewards = np.random.rand(len(nudges))  # online updates
choice = np.argmax(rewards) if np.random.rand() > 0.1 else np.random.randint(len(nudges))
print(nudges[choice])
```

## Tuning notes

- Avoid nagging; respect user autonomy and allow opt-outs.
- Use small data and frequent user feedback to personalize.
- Ground suggestions in self-reported values, not engagement alone.
- Validate with self-report and objective adherence, not just clicks.

## Verification

1. Recommend a 7-day habit and track completion streaks.
2. Build a hobby recommender from a short user profile and compare to manual choices.
3. Simulate the effect of a nudge on a personal goal metric.
''',
        "references": [
            "https://doi.org/10.48550/arxiv.2509.06269",
            "https://www.mdpi.com/2076-3417/14/22/10220",
            "https://doi.org/10.1609/aaai.v40i21.38818",
            "https://doi.org/10.3389/frai.2026.1834771",
            "https://ojs.aaai.org/index.php/AAAI/article/view/35159",
        ],
    },
]
