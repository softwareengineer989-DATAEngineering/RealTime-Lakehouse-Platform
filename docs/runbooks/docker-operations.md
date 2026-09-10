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

# View Running Containers

```bash
docker ps
```

All containers

```bash
docker ps -a
```

---



---

## Kafka CLI Examples

### List Topics

```bash
docker exec kafka kafka-topics \
  --bootstrap-server localhost:9092 \
  --list
```

### Describe Topic

```bash
docker exec kafka kafka-topics \
  --bootstrap-server localhost:9092 \
  --describe \
  --topic orders.raw
```

### List Consumer Groups

```bash
docker exec kafka kafka-consumer-groups \
  --bootstrap-server localhost:9092 \
  --list
```

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

# Stopping Services

```bash
docker compose down
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

# Restart Services

```bash
docker compose restart
```

Restart single service

```bash
docker compose restart kafka
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


# Disaster Recovery

If Docker metadata becomes corrupted:

1. Export required volumes.
2. Remove containers.
3. Remove orphaned networks.
4. Rebuild images.
5. Restore required data volumes.
6. Validate platform health.

# References

- docker-compose.yml
- docker/
- README.md
- Local Development Runbook

---

# Related Documentation

- [Platform Architecture](../architecture/ARCHITECTURE.md)
- [Local Development Guide](local-development.md)
- [Troubleshooting Guide](troubleshooting.md)
- [Project Overview](../../README.md)