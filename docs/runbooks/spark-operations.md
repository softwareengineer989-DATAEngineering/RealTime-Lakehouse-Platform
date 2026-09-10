# Spark Operations Runbook

## Purpose

This runbook documents operational procedures for Apache Spark Structured Streaming within the Real-Time Lakehouse Platform.

Spark performs real-time stream processing across the Bronze, Silver, and Gold layers while ensuring scalable, fault-tolerant data transformations.

---

# Scope

This document covers

- Spark startup
- Streaming execution
- Job monitoring
- Checkpoint management
- Recovery
- Operational validation

---

# Platform Responsibilities

Spark is responsible for

- Reading Kafka events
- Streaming transformations
- Data quality validation
- Delta Lake writes
- Incremental processing

---

# Startup Procedure

Start Docker platform

```bash
docker compose up -d
```

Verify Spark

```bash
docker ps
```

View logs

```bash
docker compose logs spark
```

Expected

- Spark container running
- No startup exceptions

---

# Execute Bronze Layer

```bash
python src/retaillake/spark/streaming/bronze_stream.py
```

Validation

- Stream started
- Checkpoint created
- Delta table written

---

# Execute Silver Layer

```bash
python src/retaillake/spark/silver/run_silver_stream.py
```

Validation

- Cleansed data
- Schema validation
- Incremental updates

---

# Execute Gold Layer

```bash
python src/retaillake/spark/gold/run_gold_stream.py
```

Validation

- Aggregations created
- Analytics tables updated

---

# Streaming Monitoring

Monitor

- Micro-batch duration
- Processing rate
- Input rows/sec
- Output rows/sec

Healthy pipeline

- Stable processing
- No stalled batches
- No excessive latency

---

# Checkpoint Management

Checkpoint directory

```
checkpoints/
```

Purpose

- Fault tolerance
- Offset tracking
- Recovery

Guidelines

- Never manually edit checkpoints
- Remove checkpoints only after intentional reset
- Keep checkpoint storage persistent

---

# Delta Validation

Validate

- Bronze tables
- Silver tables
- Gold tables

Confirm

- Record counts
- Schema consistency
- Partition integrity

---

# Performance Monitoring

Review

- CPU utilization
- Memory utilization
- Processing latency
- Batch completion time

Investigate

- Long GC pauses
- Executor failures
- OOM exceptions

---

# Failure Recovery

## Streaming Job Failure

Procedure

1. Review Spark logs
2. Identify failed stage
3. Resolve root cause
4. Restart stream
5. Validate checkpoints
6. Verify Delta outputs

---

## Checkpoint Issues

If checkpoint corruption occurs

1. Stop stream
2. Backup checkpoint
3. Remove checkpoint
4. Restart pipeline
5. Validate data integrity

---

## Memory Issues

Symptoms

- OutOfMemory
- Executor crashes
- Slow batches

Actions

- Increase executor memory
- Reduce batch size
- Optimize transformations

---

# Operational Checklist

Verify

- Spark container healthy
- Kafka connected
- Checkpoints available
- Delta writes successful
- Streaming active
- Resource utilization acceptable

---

# Best Practices

- Avoid unnecessary wide transformations.
- Cache only when beneficial.
- Monitor streaming latency continuously.
- Keep transformations modular.
- Validate schemas before writes.
- Use checkpointing for fault tolerance.
- Maintain idempotent processing logic.

---

#  Streaming Shutdown Procedure

1. Stop producer
2. Wait for micro-batches
3. Stop Spark stream
4. Stop Kafka
5. Verify checkpoints

---

# Related Documentation

- [Platform Architecture](../architecture/ARCHITECTURE.md)
- [Validation Runbook](validation-runbook.md)
- [Troubleshooting Guide](troubleshooting.md)
- [Project Overview](../../README.md)