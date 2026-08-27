# Docker Operations Runbook

## Purpose

This runbook describes operational procedures for managing Docker containers, images, networks, and volumes used by the Real-Time Lakehouse Platform.

---

# Architecture

Docker hosts:

- Kafka
- Zookeeper (if applicable)
- Spark
- Supporting services

---

# Starting Services

```bash
docker compose up -d
```

---

# Stopping Services

```bash
docker compose down
```

---

# Restart Services

```bash
docker compose restart
```

Restart single service

```bash
docker compose restart kafka
```

---

# View Running Containers

```bash
docker ps
```

All containers

```bash
docker ps -a
```

---

# View Logs

Entire stack

```bash
docker compose logs
```

Kafka

```bash
docker compose logs kafka
```

Spark

```bash
docker compose logs spark
```

Follow logs

```bash
docker compose logs -f kafka
```

---

# Execute Commands Inside Container

```bash
docker exec -it kafka bash
```

Spark

```bash
docker exec -it spark bash
```

---

# Build Images

```bash
docker compose build
```

Rebuild without cache

```bash
docker compose build --no-cache
```

---

# Remove Containers

```bash
docker compose down
```

Remove with volumes

```bash
docker compose down -v
```

---

# Remove Images

```bash
docker image prune
```

Remove unused

```bash
docker system prune
```

---

# Volumes

List

```bash
docker volume ls
```

Inspect

```bash
docker volume inspect <volume>
```

Remove

```bash
docker volume rm <volume>
```

---

# Networks

List

```bash
docker network ls
```

Inspect

```bash
docker network inspect <network>
```

---

# Health Validation

Verify:

- Containers running
- Kafka healthy
- Spark healthy
- Network connected
- Required ports exposed
- Volumes mounted

---

# Recovery Procedure

If services fail:

1. Stop stack
2. Review logs
3. Remove failed containers
4. Restart stack
5. Validate services
6. Execute integration tests

---

# Operational Best Practices

- Never manually modify container state
- Keep images version controlled
- Use Docker Compose for orchestration
- Remove unused resources regularly
- Keep environment variables outside source code
- Validate services after every restart

---

# References

- docker-compose.yml
- docker/
- README.md
- Local Development Runbook