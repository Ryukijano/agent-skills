---
name: webapp-testing
description: >-
  Toolkit for interacting with and testing local web applications using
  Playwright. Supports verifying frontend functionality, debugging UI behavior,
  capturing browser screenshots, and viewing browser logs.
---

# Web Application Testing

To test local web applications, write native Python Playwright scripts.

## Decision Tree
```
User task → Is it static HTML?
    ├─ Yes → Read HTML file directly to identify selectors
    └─ No (dynamic webapp) → Is the server already running?
        ├─ No → Start server, wait for it to be ready
        └─ Yes → Navigate, wait for networkidle, take screenshot, identify selectors
```

## Example
```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto('http://localhost:5173')
    page.wait_for_load_state('networkidle')  # CRITICAL
    page.screenshot(path='/tmp/inspect.png', full_page=True)
    # ... your automation logic
    browser.close()
```

## Reconnaissance-Then-Action Pattern
1. Inspect rendered DOM: `page.screenshot()`, `page.content()`, `page.locator('button').all()`
2. Identify selectors from inspection results
3. Execute actions using discovered selectors

## Common Pitfall
- DON'T inspect DOM before waiting for `networkidle` on dynamic apps
- DO wait for `page.wait_for_load_state('networkidle')` before inspection

## Best Practices
- Use `sync_playwright()` for synchronous scripts
- Always close the browser when done
- Use descriptive selectors: `text=`, `role=`, CSS selectors, or IDs
- Add appropriate waits: `page.wait_for_selector()` or `page.wait_for_timeout()`
