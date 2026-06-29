---
name: docker-containerization
description: >-
  Containerize applications with Docker. Use when the user wants to create
  Dockerfiles, build images, manage containers, or set up docker-compose for
  multi-service apps.
---

# Docker Containerization

## Dockerfile Best Practices
```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
CMD ["python", "main.py"]
```

## Multi-stage Build (Smaller Images)
```dockerfile
FROM python:3.11 AS builder
WORKDIR /app
COPY . .
RUN pip install --user -r requirements.txt

FROM python:3.11-slim
COPY --from=builder /root/.local /root/.local
COPY --from=builder /app /app
WORKDIR /app
ENV PATH=/root/.local/bin:$PATH
CMD ["python", "main.py"]
```

## docker-compose for Multi-Service
```yaml
version: '3.8'
services:
  web:
    build: .
    ports: ["8000:8000"]
    volumes: ["./data:/app/data"]
    environment:
      - DEBUG=1
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: secret
    volumes: ["dbdata:/var/lib/postgresql/data"]
volumes:
  dbdata:
```

## Common Commands
- Build: `docker build -t myapp .`
- Run: `docker run -p 8000:8000 myapp`
- Compose up: `docker-compose up -d`
- Clean: `docker system prune -a`
- Debug: `docker exec -it <container> bash`

## Best Practices
- Use `.dockerignore` to exclude unnecessary files
- Pin versions for reproducibility
- Run as non-root user
- Keep images small (use slim/alpine bases)
- Use multi-stage builds for production
