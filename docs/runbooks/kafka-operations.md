# Kafka Operations Runbook

## Purpose

This runbook documents the operational procedures for administering, validating, monitoring, and troubleshooting the Apache Kafka environment used by the Real-Time Lakehouse Platform.

The Kafka platform is responsible for transporting streaming order events between producers and downstream Spark Structured Streaming consumers.

---

# Scope

This document covers:

- Kafka startup
- Topic administration
- Producer validation
- Consumer validation
- Monitoring
- Operational maintenance
- Recovery procedures

---

# Platform Components

| Component | Purpose |
|------------|----------|
| Kafka Broker | Message broker |
| Producer | Publishes Instacart events |
| Consumer | Spark Structured Streaming |
| Topics | Event transport |
| Consumer Groups | Offset management |

---

# Startup Procedure

Start Docker platform

```bash
docker compose up -d
```

Verify broker

```bash
docker ps
```

Verify logs

```bash
docker compose logs kafka
```

Expected

- Broker starts successfully
- No fatal exceptions
- Topics available

---

# Kafka Topic Administration

List topics

```bash
kafka-topics --bootstrap-server localhost:9092 --list
```

Describe topic

```bash
kafka-topics \
--bootstrap-server localhost:9092 \
--describe \
--topic orders
```

Create topic

```bash
kafka-topics \
--create \
--bootstrap-server localhost:9092 \
--topic orders \
--partitions 4 \
--replication-factor 1
```

Delete topic

```bash
kafka-topics \
--delete \
--bootstrap-server localhost:9092 \
--topic orders
```

---

# Producer Operations

Start producer

```bash
python src/retaillake/kafka/producer/stream_instacart.py
```

Expected

- Records continuously published
- No serialization errors
- Stable throughput

Validation

```bash
docker compose logs producer
```

---

# Consumer Operations

Spark Streaming consumes messages.

Verify:

- Consumer active
- Offsets increasing
- No lag accumulation

List consumer groups

```bash
kafka-consumer-groups \
--bootstrap-server localhost:9092 \
--list
```

Describe group

```bash
kafka-consumer-groups \
--bootstrap-server localhost:9092 \
--describe \
--group bronze-consumer
```

---

# Offset Management

Monitor

- Current offset
- Log end offset
- Consumer lag

Healthy platform

Consumer Lag

```
≈ 0
```

---

# Throughput Validation

Validate

- Messages/sec
- Producer latency
- Consumer latency
- Spark processing rate

Expected

- Continuous processing
- No message backlog

---

# Monitoring Checklist

Daily

- Broker healthy
- Topics available
- Producers connected
- Consumers connected
- Consumer lag acceptable
- Disk utilization healthy
- Docker healthy

---

# Failure Recovery

## Broker Failure

Steps

1. Stop producer
2. Restart Kafka
3. Validate broker
4. Restart producer
5. Restart Spark stream
6. Verify offsets

---

## Topic Corruption

Procedure

1. Stop producers
2. Backup logs
3. Recreate topic
4. Restart producer
5. Validate downstream processing

---

## Consumer Lag

Possible causes

- Slow Spark processing
- Large batch size
- Resource exhaustion

Actions

- Verify Spark health
- Scale resources
- Restart consumer if necessary

---

# Performance Guidelines

Recommended

| Setting | Recommendation |
|----------|---------------|
| Partitions | 4+ |
| Producer ACK | all |
| Compression | snappy |
| Batch Size | Tuned for throughput |
| Retry | Enabled |

---

# Operational Best Practices

- Never delete production topics without approval.
- Monitor consumer lag continuously.
- Preserve message ordering using deterministic keys.
- Use idempotent producers where applicable.
- Maintain topic naming standards.
- Keep retention policies documented.
- Monitor disk usage regularly.

---

# Related Documents

- README.md
- docs/architecture/kafka-topic-design.md
- ADR-001 Kafka Container Choice
- Docker Operations Runbook