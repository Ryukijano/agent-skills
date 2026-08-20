# Full-Stack ML

## Description

End-to-end ML applications spanning data, model, API, frontend, deployment, and monitoring.

## When to use

You need to take an ML model from experiment to a deployed product with users, feedback, and continuous iteration.

## Key concepts

- **Full stack ML lifecycle**: data, training, serving, UI, deployment, monitoring.
- **Model serving**: REST/gRPC APIs, batch, edge, serverless.
- **Frontend integration**: interactive demos, dashboards, real-time inference.
- **MLOps**: experiment tracking, model registry, CI/CD, feature stores.
- **Deployment**: Docker, Kubernetes, serverless, CDK.
- **Feedback loops**: capture predictions, user actions, and retraining triggers.

## Code pattern

```python
# FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: PredictRequest):
    proba = model.predict_proba([req.text])[0]
    return {
        "label": model.classes_[proba.argmax()],
        "confidence": float(proba.max()),
    }
```

```jsx
// React frontend
import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    setResult(await res.json());
  };

  return (
    <div>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={predict}>Predict</button>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}
```

## Tuning notes

- Start simple and add complexity only when needed.
- Containerize the API and frontend; use a reverse proxy or API gateway.
- Track experiments and register models before deployment.
- Monitor latency, error rates, and prediction distributions in production.

## Verification

1. Train a model, serve it via FastAPI, and call it from a React frontend.
2. Containerize the app with Docker Compose and run end-to-end tests.
3. Add MLflow tracking and a simple Grafana dashboard for monitoring.

## References

- https://madewithml.com/
- https://github.com/GokuMohandas/Made-With-ML
- https://fullstackdeeplearning.com/
- https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/
- https://github.com/pipinho13/churnguard
