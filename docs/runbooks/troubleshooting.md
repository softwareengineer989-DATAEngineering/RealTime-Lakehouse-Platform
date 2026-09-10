# Troubleshooting Runbook

## Purpose

This runbook provides a structured troubleshooting guide for the Real-Time Lakehouse Platform.

It is intended to help developers rapidly diagnose, isolate, and resolve common operational issues encountered during development, testing, and production validation.

---

# Troubleshooting Philosophy

Follow a structured approach:

1. Identify symptoms.
2. Review logs.
3. Verify infrastructure.
4. Validate configuration.
5. Isolate root cause.
6. Apply corrective action.
7. Re-run validation.
8. Document findings.

Never restart services blindly without identifying the underlying issue.

---

# Troubleshooting Flow

```
Issue Reported
       │
       ▼
Review Logs
       │
       ▼
Infrastructure Healthy?
       │
 ┌─────┴─────┐
 │           │
No          Yes
 │           │
Fix         Validate Configuration
Infrastructure
             │
             ▼
       Verify Runtime
             │
             ▼
      Reproduce Issue
             │
             ▼
      Root Cause Found
             │
             ▼
      Apply Resolution
             │
             ▼
     Execute Validation
```

---

# Common Issues

---

## Docker Containers Not Starting

### Symptoms

- Container exits immediately
- Restart loop
- Health check failures

### Diagnosis

Check status

```bash
docker ps -a
```

Inspect logs

```bash
docker compose logs
```

### Resolution

- Verify Docker Desktop is running.
- Verify compose configuration.
- Check port conflicts.
- Remove stopped containers.
- Restart stack.

---

## Kafka Broker Unavailable

### Symptoms

- Producer cannot connect
- Consumer timeout
- Connection refused

### Diagnosis

```bash
docker compose logs kafka
```

Verify broker

```bash
docker ps
```

### Resolution

- Restart Kafka
- Verify advertised listeners
- Verify network
- Confirm broker port

---

## Spark Streaming Stops

### Symptoms

- Streaming terminates
- No micro-batches
- No Delta output

### Diagnosis

Review Spark logs

Review checkpoint directory

Verify Kafka connectivity

### Resolution

- Restart Spark job
- Verify checkpoint
- Validate Kafka topic
- Review exceptions

---

## Producer Stops Publishing

### Symptoms

- No Kafka messages
- Empty topic
- Consumer idle

### Diagnosis

Verify producer logs

Verify dataset availability

Validate topic

### Resolution

- Restart producer
- Validate source dataset
- Verify broker availability

---

## Consumer Lag Increasing

### Symptoms

- Increasing lag
- Delayed processing

### Diagnosis

```bash
kafka-consumer-groups --describe
```

### Resolution

- Review Spark throughput
- Review CPU utilization
- Increase partitions if required
- Investigate processing bottlenecks

---

## Delta Tables Not Updating

### Symptoms

- Empty tables
- Missing partitions
- Stale analytics

### Diagnosis

Verify streaming jobs

Verify storage paths

Check logs

### Resolution

- Restart stream
- Validate write permissions
- Verify checkpoint integrity

---

## GitHub Actions Failure

### Symptoms

- CI fails
- Tests fail
- Workflow stops

### Diagnosis

Review:

- Workflow logs
- Test output
- Dependency installation
- Python version

### Resolution

- Fix failing tests
- Validate imports
- Review requirements
- Re-run workflow

---

## Test Failures

### Symptoms

- Unit tests failing
- Fixture errors
- Import errors

### Diagnosis

Execute

```bash
pytest -v
```

### Resolution

- Review fixtures
- Validate package imports
- Review recent changes
- Execute isolated tests

---

## Performance Degradation

### Symptoms

- Slow processing
- High CPU
- High memory

### Diagnosis

Review

- Docker resources
- Spark metrics
- Kafka throughput

### Resolution

- Optimize transformations
- Increase resources
- Reduce batch size
- Profile application

---

# Log Locations

| Component | Location |
|------------|----------|
| Docker | docker compose logs |
| Kafka | Container logs |
| Spark | Spark logs |
| Application | logs/ |
| GitHub Actions | Actions tab |

---

# Escalation Checklist

Before escalating:

- Reproduce issue
- Capture logs
- Record configuration
- Document environment
- Save screenshots
- Identify affected component

---

# Preventive Maintenance

- Keep dependencies updated.
- Review CI regularly.
- Validate checkpoints.
- Monitor Kafka lag.
- Clean unused Docker resources.
- Execute automated tests before commits.
- Document recurring issues.

---

# Related Documentation

- [Docker Operations](docker-operations.md)
- [Kafka Operations](kafka-operations.md)
- [Spark Operations](spark-operations.md)
- [Validation Runbook](validation-runbook.md)
- [Project Overview](../../README.md)