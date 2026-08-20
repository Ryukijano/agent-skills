# Microservices

## Description

Small, independently deployable services, inter-service communication, containers, and service discovery.

## When to use

Your application is large enough that independent scaling, deployment, and team ownership of capabilities outweigh the cost of distributed-system complexity.

## Key concepts

- **Bounded contexts and DDD**: split services by business capability, not technical layer.
- **Inter-service communication**: REST, gRPC, message brokers (async).
- **Container orchestration**: Docker, Kubernetes, Helm.
- **Service discovery and load balancing**: DNS, ingress, sidecars, service mesh.
- **Resilience**: retries, timeouts, circuit breakers, bulkheads, graceful degradation.
- **Observability**: distributed tracing, centralized logs, metrics.

## Code pattern

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: inference
  template:
    metadata:
      labels:
        app: inference
    spec:
      containers:
        - name: inference
          image: myregistry/inference:v1.2
          ports:
            - containerPort: 8000
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
          readinessProbe:
            httpGet:
              path: /ready
              port: 8000
```

## Tuning notes

- Avoid nanoservices; start with a well-factored monolith if the domain is unclear.
- Prefer async messaging for loose coupling; use synchronous calls only when required.
- Keep services stateless; externalize session and state to caches/databases.
- Implement CI/CD, canary deployments, and automated rollback for each service.

## Verification

1. Split a monolith API into two services and deploy with Docker Compose or Kubernetes.
2. Add a gRPC or message-broker integration and measure latency and resilience.
3. Implement health probes, metrics, and a failing-service fallback.

## References

- https://martinfowler.com/microservices/
- https://microservices.io/
- https://kubernetes.io/docs/home/
- https://grpc.io/docs/
- https://martinfowler.com/articles/microservice-trade-offs.html
