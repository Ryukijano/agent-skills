# API Development

## Description

REST, gRPC, and GraphQL API design, implementation, documentation, and versioning for ML services.

## When to use

You are exposing functionality (predictions, data, features) to clients, frontends, or other services via a network API.

## Key concepts

- **REST**: resource-oriented, HTTP verbs, stateless, hypermedia-driven design.
- **API contract and documentation**: OpenAPI/Swagger, automatic docs.
- **Validation**: Pydantic, JSON Schema, proto3.
- **Authentication and authorization**: OAuth2, JWT, API keys.
- **Versioning and deprecation**: URI, header, or media-type versioning.
- **gRPC/GraphQL**: high-performance RPC and flexible query languages.

## Code pattern

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str
    top_k: int = 3

class PredictResponse(BaseModel):
    labels: list[str]
    scores: list[float]

@app.post("/predict", response_model=PredictResponse, tags=["inference"])
def predict(req: PredictRequest):
    # model inference placeholder
    return PredictResponse(labels=["class_a", "class_b"], scores=[0.9, 0.1])
```

## Tuning notes

- Design for idempotency and clear error responses.
- Return consistent status codes; use 204 for empty deletes.
- Use pagination and rate limiting for large collections.
- Generate client SDKs from OpenAPI and keep contracts in version control.

## Verification

1. Build a FastAPI service with OpenAPI docs and Pydantic validation.
2. Implement JWT or API-key auth and test protected endpoints.
3. Add versioning and verify backward-compatible client behavior.

## References

- https://fastapi.tiangolo.com/
- https://spec.openapis.org/oas/latest
- https://grpc.io/docs/what-is-grpc/introduction/
- https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design
- https://blog.postman.com/rest-api-best-practices/
