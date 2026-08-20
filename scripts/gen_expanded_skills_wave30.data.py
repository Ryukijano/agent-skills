SKILLS = [
    {
        "name": "ai-for-learning-analytics",
        "title": "AI for Learning Analytics",
        "description": "Learning management system analysis, learner trajectory modeling, early warning systems, engagement dashboards, and educational data mining.",
        "devin_body": r'''## When to use

You want to turn LMS logs, assessment records, and behavioral traces into actionable insight about student progress, risk, and course effectiveness.

## Key concepts

- **Learning analytics cycle**: data capture, analysis, intervention, and reflection.
- **Clickstream and engagement features**: time-on-task, resource access, forum activity, and submission patterns.
- **Knowledge tracing**: Deep Knowledge Tracing (DKT) and Bayesian Knowledge Tracing (BKT) to model mastery over time.
- **Early warning systems**: predictive models that flag at-risk students for timely support.
- **Fairness and privacy**: protect sensitive student data and audit for subgroup bias.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Build simple at-risk predictor from LMS engagement features
X = df[["logins_per_week", "assignments_completed", "forum_posts", "quiz_avg"]]
y = df["at_risk"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["risk_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use time-based train/test splits to avoid look-ahead leakage.
- Prefer interpretable features so instructors can trust and act on alerts.
- Integrate predictions with advising workflows rather than using them in isolation.

## Verification

1. Build an engagement dashboard from an LMS export.
2. Train a dropout predictor and evaluate AUC on a held-out term.
3. Compare a DKT model to a baseline logistic model on a public knowledge-tracing dataset.
''',
        "references": [
            "https://doi.org/10.1145/3636555.3636856",
            "https://doi.org/10.18608/jla.2024.8367",
            "https://arxiv.org/abs/2504.11481",
            "https://doi.org/10.1007/s40593-024-00429-7",
        ],
    },
    {
        "name": "ai-for-educational-assessment",
        "title": "AI for Educational Assessment",
        "description": "Automated essay scoring, conversational assessment, LLM rubric grading, feedback generation, and validity and fairness of AI-driven evaluation.",
        "devin_body": r'''## When to use

You need to score open-ended work, generate formative feedback, or design assessments at scale while preserving validity, reliability, and fairness.

## Key concepts

- **Automated Essay Scoring (AES)**: models that predict holistic or trait-level writing scores.
- **Conversational assessment**: LLM-driven dialogs that probe understanding aligned with learning outcomes.
- **Rubric generation and calibration**: derive scoring criteria and align AI scores with human raters.
- **Fairness and validity**: check for subgroup score differences and construct validity across populations.

## Code pattern

```python
from transformers import pipeline

# Zero-shot LLM scoring with a rubric
rubric = "Score the essay on argumentation, evidence, and clarity from 1 to 5."
prompt = f"{rubric}\n\nEssay: {essay}\n\nScore:"

# Use a local or API-based text-generation model
scorer = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf")
result = scorer(prompt, max_new_tokens=10)
```

## Tuning notes

- Evaluate against human raters using quadratic weighted kappa (QWK) or intraclass correlation (ICC).
- Validate on demographically diverse samples to detect score bias.
- Combine LLM scores with structured rubrics rather than relying on raw outputs.

## Verification

1. Score a benchmark essay set and compare AI-human agreement.
2. Generate rubrics for an assignment and validate them with instructors.
3. Audit subgroup score parity and correlation with final course grades.
''',
        "references": [
            "https://doi.org/10.1145/3702163.3702169",
            "https://arxiv.org/abs/2403.06149",
            "https://arxiv.org/abs/2405.18632",
            "https://arxiv.org/abs/2404.04941",
        ],
    },
    {
        "name": "ai-for-tutoring",
        "title": "AI for Tutoring",
        "description": "Intelligent tutoring systems, dialogue-based tutoring, error diagnosis, Socratic scaffolding, and personalized next-step hints.",
        "devin_body": r'''## When to use

You want to build or augment a one-on-one digital tutor that diagnoses misconceptions and gives step-by-step guidance without giving away the answer.

## Key concepts

- **Intelligent Tutoring System (ITS) architecture**: student model, expert model, tutoring model, and interface.
- **Dialogue tutoring**: natural-language interaction that scaffolds problem solving.
- **Error diagnosis and remediation**: identify the specific misconception behind a wrong step.
- **Pedagogical guardrails**: keep hints productive, avoid answer leakage, and maintain learning outcomes.

## Code pattern

```python
import openai

# Socratic tutor prompt that avoids giving the answer
system_prompt = (
    "You are a patient math tutor. Ask one clarifying question at a time, "
    "guide the student to discover their own mistake, and never reveal the final answer."
)
response = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"I got {student_answer} for {problem}. What should I do?"},
    ],
)
```

## Tuning notes

- Evaluate tutor responses on pedagogical dimensions, not just fluency.
- Use the target curriculum and problem set to constrain model outputs.
- Keep a human escalation path for high-stakes or persistent errors.

## Verification

1. Build a small math tutoring dialog and rate hint quality against a rubric.
2. Compare learning gains between an AI tutor and a worksheet-only control.
3. Test error diagnosis accuracy on a labeled set of student misconceptions.
''',
        "references": [
            "https://doi.org/10.1007/s40593-025-00505-6",
            "https://aclanthology.org/2025.naacl-long.57/",
            "https://arxiv.org/abs/2402.09216",
            "https://doi.org/10.1145/3701716.3715244",
        ],
    },
    {
        "name": "ai-for-curriculum-design",
        "title": "AI for Curriculum Design",
        "description": "Goal-aligned course sequencing, personalized learning paths, content alignment, adaptive curricula, and standards mapping.",
        "devin_body": r'''## When to use

You are designing or adapting courses, modules, or learning pathways to align with learner goals, prior knowledge, and competency standards.

## Key concepts

- **Competency and prerequisite graphs**: model skills and their dependencies.
- **Learning path planning**: sequence content to optimize mastery and engagement.
- **Standards alignment**: map learning objectives to curriculum or accreditation frameworks.
- **Adaptive curricula**: adjust pacing, depth, and examples based on learner data.

## Code pattern

```python
import networkx as nx

# Build a simple prerequisite graph and topologically sort a learning path
G = nx.DiGraph()
G.add_edges_from([
    ("basic_algebra", "linear_equations"),
    ("linear_equations", "quadratic_equations"),
    ("quadratic_equations", "polynomials"),
])
path = list(nx.topological_sort(G))
```

## Tuning notes

- Validate generated paths against learning outcomes and instructor expertise.
- Avoid over-filtering that limits exposure to challenging or novel topics.
- Use learner feedback to refine sequencing and difficulty.

## Verification

1. Map a course to a competency framework and check coverage.
2. Generate a personalized learning path for a mock learner profile.
3. Measure completion and mastery rates for a sequenced versus random curriculum.
''',
        "references": [
            "https://arxiv.org/abs/2407.11773",
            "https://doi.org/10.32657/10356/181505",
            "https://www.nature.com/articles/s41598-024-56497-1",
            "https://www.frontiersin.org/articles/10.3389/feduc.2024.1288723",
        ],
    },
    {
        "name": "ai-for-language-learning",
        "title": "AI for Language Learning",
        "description": "AI chatbots for conversation practice, automated writing and pronunciation feedback, CEFR-level adaptation, and second-language acquisition support.",
        "devin_body": r'''## When to use

You are supporting second or foreign language learners with interactive practice, corrective feedback, and level-appropriate content.

## Key concepts

- **Computer-assisted language learning (CALL/MALL)**: AI tools for speaking, listening, reading, and writing.
- **Conversational agents and chatbots**: simulate dialogue partners for practice.
- **Corrective recasts and scaffolding**: provide graduated feedback on learner errors.
- **Proficiency-level adaptation**: align content and feedback with frameworks such as CEFR.

## Code pattern

```python
from transformers import pipeline

# Generate a CEFR-appropriate conversation prompt for a learner
level = "B1"
topic = "travel"
prompt = (
    f"Create a {level}-level English conversation about {topic}. "
    "Ask an open question and provide a gentle recast if the answer contains errors."
)

chatbot = pipeline("text-generation", model="HuggingFaceH4/zephyr-7b-beta")
response = chatbot(prompt, max_new_tokens=120)
```

## Tuning notes

- Respect target-language varieties and sociolinguistic contexts.
- Validate corrective feedback against language instructor judgments.
- Combine chatbot practice with structured input and production tasks.

## Verification

1. Run a chatbot conversation and score its CEFR appropriateness.
2. Collect learner uptake after automated corrective recasts.
3. Compare writing improvement between an AI-feedback group and a control group.
''',
        "references": [
            "https://doi.org/10.64152/10125/73575",
            "https://doi.org/10.1017/s0958344024000168",
            "https://aclanthology.org/2024.nlp4call-1.18/",
            "https://doi.org/10.64152/10125/73574",
        ],
    },
    {
        "name": "ai-for-special-education",
        "title": "AI for Special Education",
        "description": "Assistive technologies, personalized interventions, augmentative and alternative communication, accessibility, and inclusive learning for learners with disabilities.",
        "devin_body": r'''## When to use

You are supporting learners with disabilities, neurodiversity, or special educational needs through accessible and personalized AI tools.

## Key concepts

- **Assistive communication (AAC)**: AI-powered speech, symbol, and text supports.
- **Personalized adaptive learning**: tailor pacing, content, and interaction modality.
- **Multimodal interaction**: speech, vision, touch, and haptics for diverse abilities.
- **Co-design and inclusion**: involve learners, families, and educators in design.
- **Ethics and equity**: protect privacy, avoid stigma, and audit for ableist bias.

## Code pattern

```python
from transformers import pipeline

# Speech-to-text with a local Whisper model for accessibility
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base")
text = transcriber("student_response.wav")["text"]
```

## Tuning notes

- Co-design with target users and special-education professionals.
- Test for accessibility standards (WCAG, Section 508) and device compatibility.
- Monitor for algorithmic bias and unintended deskilling of human support.

## Verification

1. Prototype an assistive reading or communication tool.
2. Test the tool with representative users and collect usability feedback.
3. Evaluate whether the intervention improves target skills or independence.
''',
        "references": [
            "https://doi.org/10.3390/socsci14050288",
            "https://doi.org/10.3102/00346543241293424",
            "https://link.springer.com/article/10.1007/s10639-024-13134-8",
            "https://doi.org/10.1177/01626434241257237",
        ],
    },
    {
        "name": "ai-for-student-engagement",
        "title": "AI for Student Engagement",
        "description": "Engagement prediction, behavioral analytics, early warning systems, intervention targeting, and motivational feedback.",
        "devin_body": r'''## When to use

You want to identify disengaged or at-risk learners and trigger timely, evidence-based supports before performance declines.

## Key concepts

- **Behavioral, cognitive, and affective engagement**: combine log, academic, and self-report signals.
- **Early warning systems**: predict dropout or failure with time-aware models.
- **Intervention targeting**: match at-risk students to the most effective supports.
- **Nudges and feedback**: send timely, actionable messages to learners and advisors.

## Code pattern

```python
import pandas as pd
from xgboost import XGBClassifier

X = df[["login_count", "time_on_platform", "assignments_late", "discussion_posts", "prior_gpa"]]
y = df["disengaged"]

model = XGBClassifier(eval_metric="logloss", random_state=42)
model.fit(X, y)
df["engagement_risk"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Use chronological splits and avoid leakage from future events.
- Combine LMS data with academic and demographic context carefully.
- Address surveillance and equity concerns by involving students and advisors.

## Verification

1. Build an engagement dashboard from a course LMS export.
2. Predict at-risk status weekly and evaluate precision-recall over time.
3. Run a small intervention pilot and measure re-engagement rates.
''',
        "references": [
            "https://www.sciencedirect.com/science/article/pii/S0160791X24000228",
            "https://doi.org/10.1145/3636555.3636906",
            "https://www.frontiersin.org/articles/10.3389/feduc.2024.1421479",
            "https://learning-analytics.info/index.php/JLA/article/view/7985",
        ],
    },
    {
        "name": "ai-for-higher-education",
        "title": "AI for Higher Education",
        "description": "Admissions analytics, retention and completion modeling, student success advising, enrollment planning, and institutional research.",
        "devin_body": r'''## When to use

You are improving access, success, retention, or operational decisions in colleges and universities.

## Key concepts

- **Predictive retention and completion models**: identify students likely to drop out or stop out.
- **Admissions analytics**: forecast yield, optimize enrollment, and support holistic review.
- **Student success advising**: match students with courses, supports, and career pathways.
- **Equity and transparency**: ensure AI advice does not reinforce historical disadvantage.

## Code pattern

```python
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = df[["hs_gpa", "first_gen", "credit_load", "campus_engagement"]]
y = df["retained_year_2"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
model = RandomForestClassifier(random_state=42).fit(X_train, y_train)
```

## Tuning notes

- Avoid high-stakes decisions based solely on predicted risk scores.
- Ensure compliance with FERPA, GDPR, and institutional IRB requirements.
- Audit predictions for subgroup disparities and validate longitudinally.

## Verification

1. Predict first-year retention and report AUC by demographic subgroup.
2. Build an equity-aware course or admissions recommender.
3. Evaluate whether advisor use of an early-alert system changes outcomes.
''',
        "references": [
            "https://www.nature.com/articles/s41598-025-23116-6",
            "https://link.springer.com/article/10.1007/s10734-025-01509-w",
            "https://www.science.org/doi/10.1126/sciadv.adg9405",
            "https://arxiv.org/abs/2411.15348",
        ],
    },
    {
        "name": "ai-for-lifelong-learning",
        "title": "AI for Lifelong Learning",
        "description": "Continuous skill development, career-aligned learning pathways, micro-credentials, and AI support for adult and professional learners.",
        "devin_body": r'''## When to use

You are helping adult learners, working professionals, or career-switchers acquire new skills and credentials throughout their lives.

## Key concepts

- **Lifelong and self-directed learning**: support learners in setting and pursuing their own goals.
- **Competency and career alignment**: map skills to job postings, career ladders, and credentials.
- **Micro-credentials and portfolios**: recognize mastery in small, demonstrable units.
- **Continuous adaptation**: update recommendations as labor markets and learner goals evolve.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Match learner profile to relevant learning resources
learner_skills = "data visualization, statistics, Python"
resources = ["SQL fundamentals", "data viz with Tableau", "advanced Python"]

vec = TfidfVectorizer()
vectors = vec.fit_transform([learner_skills] + resources)
sim = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
recommendations = sorted(zip(resources, sim), key=lambda x: x[1], reverse=True)
```

## Tuning notes

- Align recommendations with credible labor-market signals and employer needs.
- Support self-regulated learning with goal-setting and progress dashboards.
- Ensure mobile and low-bandwidth access for working adults.

## Verification

1. Map a target job role to required skills and learning resources.
2. Recommend a personalized learning path and track completion.
3. Survey learners on career relevance and satisfaction after the path.
''',
        "references": [
            "https://www.mdpi.com/2076-3417/15/17/9352",
            "https://doi.org/10.59075/shmsar14",
            "https://doi.org/10.33545/26649845.2026.v8.i2a.514",
            "https://arxiv.org/abs/2501.07278",
        ],
    },
    {
        "name": "ai-for-pedagogy",
        "title": "AI for Pedagogy",
        "description": "Teacher-AI collaboration, lesson planning, instructional design, feedback generation, and evidence-based teaching practice augmentation.",
        "devin_body": r'''## When to use

You want to support teachers in planning, delivering, and improving instruction while keeping educators at the center of the learning process.

## Key concepts

- **Teacher-AI co-design**: generative AI as a collaborator, not a replacement, for educators.
- **Lesson and activity generation**: create standards-aligned plans, materials, and assessments.
- **Formative feedback**: provide teachers with insights on student understanding.
- **TPACK and professional development**: build the knowledge needed to integrate AI responsibly.

## Code pattern

```python
import openai

# Co-create a differentiated lesson plan with a local or API LLM
prompt = (
    "Design a 45-minute middle-school science lesson on photosynthesis. "
    "Include learning objectives, a hands-on activity, and two differentiation options."
)
lesson = openai.ChatCompletion.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "You are an experienced instructional coach."},
        {"role": "user", "content": prompt},
    ],
)
```

## Tuning notes

- Preserve teacher agency and local curriculum context.
- Verify accuracy of AI-generated content, especially in specialized subjects.
- Use AI to reduce administrative load, not to deskill teaching.

## Verification

1. Generate a lesson plan and have a teacher review it for quality and fit.
2. Adapt a plan for two different learner profiles and collect feedback.
3. Measure time saved and teacher satisfaction with an AI-assisted planning tool.
''',
        "references": [
            "https://link.springer.com/article/10.1007/s10956-024-10174-0",
            "https://dl.acm.org/doi/10.1145/3788074",
            "https://link.springer.com/article/10.1007/s40751-024-00168-3",
            "https://link.springer.com/article/10.1007/s10639-025-13699-y",
        ],
    },
    {
        "name": "ai-for-educational-games",
        "title": "AI for Educational Games",
        "description": "Game-based learning, adaptive difficulty, intelligent NPCs, scaffolding, and learning analytics embedded in playful environments.",
        "devin_body": r'''## When to use

You are building or adapting games that teach concepts through interactive, adaptive, and engaging play.

## Key concepts

- **Digital game-based learning (DGBL)**: use games to motivate and support learning.
- **Adaptive difficulty and player modeling**: adjust challenge to maintain flow.
- **Intelligent NPCs**: AI characters that scaffold, coach, or converse with players.
- **Procedural content generation**: create varied levels, puzzles, and scenarios.

## Code pattern

```python
# Simple adaptive difficulty based on recent player performance
recent = [1, 1, 0, 1, 1]  # 1 = success, 0 = failure
success_rate = sum(recent) / len(recent)

if success_rate > 0.8:
    next_level = current_level + 1
elif success_rate < 0.4:
    next_level = max(1, current_level - 1)
else:
    next_level = current_level
```

## Tuning notes

- Balance learning objectives with player enjoyment and autonomy.
- Avoid excessive scaffolding that removes productive struggle.
- Collect learning evidence and validate against a non-game baseline.

## Verification

1. Design a short learning game around a specific concept.
2. Implement adaptive difficulty and test retention on repeated play.
3. Measure learning gains and motivation compared to a traditional lesson.
''',
        "references": [
            "https://journals.sagepub.com/doi/10.1177/07356331251396354",
            "https://eric.ed.gov/?id=EJ1445818",
            "https://link.springer.com/article/10.1007/s10639-025-13624-3",
            "https://ojs.aaai.org/index.php/AAAI/article/view/30354",
        ],
    },
    {
        "name": "ai-for-competency-development",
        "title": "AI for Competency Development",
        "description": "Competency-based education, skill gap analysis, adaptive credentialing, and AI-driven mastery and portfolio assessment.",
        "devin_body": r'''## When to use

You are designing competency-based learning where demonstrated mastery, not seat time, drives progression and credentials.

## Key concepts

- **Competency frameworks and skills taxonomies**: ESCO, O*NET, or institutional competency maps.
- **Skill gap analysis**: compare current abilities to role or course requirements.
- **Mastery assessment**: evaluate observable performances and artifacts.
- **Portfolio and credentialing**: recognize competence through badges, micro-credentials, or transcripts.

## Code pattern

```python
import pandas as pd

# Simple skill gap matrix for a learner against a role profile
required = {"python": 4, "sql": 3, "communication": 3}
learner = {"python": 3, "sql": 2, "communication": 4}

gaps = {skill: max(0, required[skill] - learner.get(skill, 0)) for skill in required}
```

## Tuning notes

- Define competencies as observable and assessable behaviors.
- Combine formative evidence, summative assessments, and authentic tasks.
- Ensure credentials are portable and aligned with employer or academic standards.

## Verification

1. Map a course or program to a competency framework.
2. Assess learner mastery with a rubric and compare to a traditional grade.
3. Recommend targeted resources based on identified skill gaps.
''',
        "references": [
            "https://doi.org/10.1016/j.caeai.2025.100485",
            "https://doi.org/10.66053/aillce.v1i1.29",
            "https://doi.org/10.1111/bjet.13556",
            "https://link.springer.com/article/10.1007/s44366-025-0039-x",
        ],
    },
]
