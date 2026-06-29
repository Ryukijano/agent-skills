---
name: api-design
description: >-
  Design and implement REST and GraphQL APIs. Use when the user wants to create
  API endpoints, design API schemas, or implement API best practices.
---

# API Design

## REST API Best Practices
- Use nouns for resources: `/users`, `/users/{id}`, `/users/{id}/posts`
- HTTP methods: GET (read), POST (create), PUT (replace), PATCH (update), DELETE
- Status codes: 200 (OK), 201 (Created), 204 (No Content), 400 (Bad Request), 401 (Unauthorized), 403 (Forbidden), 404 (Not Found), 429 (Rate Limited), 500 (Server Error)
- Versioning: `/api/v1/users` or via Accept header
- Pagination: `?page=1&limit=20` or cursor-based
- Filtering: `?status=active&role=admin`

## FastAPI Quick Start
```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str

class UserResponse(BaseModel):
    id: int
    name: str
    email: str

@app.post("/users", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    # Business logic here
    return UserResponse(id=1, **user.dict())

@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]
```

## Key Principles
- Stateless (REST): Each request contains all needed info
- Consistent response format: `{"data": ..., "meta": ...}` or `{"data": ..., "error": null}`
- Error format: `{"error": {"code": "NOT_FOUND", "message": "User not found"}}`
- Idempotency: GET, PUT, DELETE should be safe to retry
- Rate limiting: Return `X-RateLimit-*` headers

## Documentation
- OpenAPI/Swagger: FastAPI generates automatically
- Include examples for each endpoint
- Document error responses
