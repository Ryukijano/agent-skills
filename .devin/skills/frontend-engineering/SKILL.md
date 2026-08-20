# Frontend Engineering

## Description

Building user interfaces for ML-powered applications with modern frameworks, state management, and data visualization.

## When to use

You need a web or mobile UI to collect input, display predictions, visualize model outputs, or monitor ML systems.

## Key concepts

- **Component frameworks**: React, Svelte, Vue, Angular.
- **State management**: hooks, Redux, Zustand, Pinia, Svelte stores.
- **Data fetching**: REST/GraphQL clients, TanStack Query, SWR.
- **Visualization**: D3, Chart.js, Plotly, Recharts, Vega-Lite.
- **Performance**: code splitting, virtualization, memoization, lazy loading.
- **ML-specific UI**: confidence scores, explanations, feedback loops, A/B tests.

## Code pattern

```jsx
import { useState } from "react";

function PredictionForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button type="submit">Predict</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </form>
  );
}
```

## Tuning notes

- Keep UI state close to where it is used; lift only when needed.
- Debounce input for real-time features and throttle expensive renders.
- Use Suspense and error boundaries for async boundaries.
- Design for accessibility and responsive layouts.

## Verification

1. Build a React/Svelte/Vue form that calls a prediction API.
2. Add a chart that visualizes model confidence distributions.
3. Run Lighthouse or web-vitals checks and optimize metrics.

## References

- https://react.dev/learn
- https://svelte.dev/docs
- https://vuejs.org/
- https://developer.mozilla.org/en-US/docs/Learn
- https://d3js.org/
