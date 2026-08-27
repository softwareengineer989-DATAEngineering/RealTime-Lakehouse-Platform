# Screenshot Evidence Guide

> **RealTime Lakehouse Platform**  
> Visual Evidence Collection Standards for Production Validation

---

# 1. Purpose

The `screenshots/` directory contains visual evidence collected during production validation of the RealTime Lakehouse Platform.

Screenshots supplement runtime logs, validation reports, and operational metrics by providing a visual record of important execution states.

They are intended to:

- Support engineering reviews
- Demonstrate successful execution
- Improve troubleshooting
- Preserve operational evidence
- Strengthen portfolio presentation
- Assist release validation

Screenshots should never replace logs or reports. They provide visual confirmation of system state at specific points during execution.

---

# 2. Evidence Philosophy

The RealTime Lakehouse Platform follows an **Evidence-First Validation** approach.

Validation evidence is collected in four complementary forms:

```text
Logs
        │
        ▼
Metrics
        │
        ▼
Reports
        │
        ▼
Screenshots
```

Each type of evidence serves a different purpose.

| Evidence Type | Purpose |
|---------------|---------|
| Logs | Detailed runtime diagnostics |
| Metrics | Resource utilization and performance |
| Reports | Human-readable validation summaries |
| Screenshots | Visual confirmation of important states |

Screenshots should support—not duplicate—other evidence.

---

# 3. Screenshot Directory Structure

```text
screenshots/

sprint-15.5/

docker/

spark/

kafka/

delta/

system/

testing/

github-actions/
```

Future sprint evidence should be stored separately.

Example:

```text
screenshots/

sprint-15.5/

sprint-16/

sprint-17/
```

This preserves the historical evolution of the project.

---

# 4. Docker Screenshots

Purpose:

Capture infrastructure readiness.

Typical screenshots include:

- Docker Desktop running
- `docker ps`
- `docker compose ps`
- Container health
- Docker statistics

Examples:

```text
100K_docker_running.png

500K_docker_stats.png

docker_compose_running.png
```

---

# 5. Spark Screenshots

Purpose:

Capture Spark execution state.

Recommended screenshots:

- Bronze stream running
- Silver stream running
- Gold stream running
- Spark UI (future enhancement)
- Structured Streaming status

Examples:

```text
100K_bronze_stream.png

500K_gold_stream.png
```

---

# 6. Kafka Screenshots

Purpose:

Capture messaging infrastructure.

Examples:

- Producer execution
- Kafka topics
- Consumer groups
- Successful message flow
- Topic verification

Typical filenames:

```text
100K_topics_created.png

producer_completed.png
```

---

# 7. Delta Screenshots

Purpose:

Verify generated data.

Capture:

- Bronze Delta tables
- Silver Delta tables
- Gold Delta tables
- Checkpoint directories
- Output directory structure

These screenshots demonstrate successful pipeline execution.

---

# 8. System Screenshots

Purpose:

Capture host environment.

Examples:

- Python version
- Java version
- Docker version
- Operating System
- Environment validation

These screenshots help document the execution environment.

---

# 9. Testing Screenshots

Purpose:

Capture validation activities.

Recommended screenshots:

- pytest success
- Coverage report
- JUnit generation
- Integration tests

Testing screenshots should demonstrate successful validation without duplicating console logs.

---

# 10. GitHub Actions Screenshots

Purpose:

Document CI/CD execution.

Examples:

- Successful workflow
- Passing jobs
- Pull Request checks
- Release workflow
- Completed pipeline

These screenshots strengthen the portfolio by demonstrating automated validation.

---

# 11. Naming Convention

Screenshots should follow a consistent naming standard.

Format:

```text
YYYY-MM-DD_HH-MM-SS_<description>.png
```

Examples:

```text
2026-08-26_100K_docker_running.png

2026-08-26_spark_bronze_running.png

2026-08-26_kafka_topics.png
```

Descriptive filenames improve traceability and simplify future audits.

---

# 12. Screenshot Timing

Screenshots should be captured only at meaningful milestones.

Typical sequence:

```text
Infrastructure Ready
        │
        ▼
Producer Started
        │
        ▼
Bronze Running
        │
        ▼
Silver Running
        │
        ▼
Gold Running
        │
        ▼
Pipeline Completed
        │
        ▼
Delta Outputs
        │
        ▼
Performance Metrics
        │
        ▼
Validation Complete
```

Avoid taking repeated screenshots of the same state unless documenting a significant change.

---

# 13. Screenshot Quality Standards

All screenshots should:

- Be high resolution
- Show the full terminal or application window
- Avoid unnecessary cropping
- Include timestamps where practical
- Exclude unrelated desktop content
- Be clearly readable
- Use meaningful filenames

Screenshots should represent the system accurately without modification.

---

# 14. Evidence Retention Policy

Screenshots are permanent validation artifacts.

Do not delete screenshots associated with completed production validations unless they are accidental duplicates or contain sensitive information.

Historical screenshots provide valuable evidence for:

- Engineering reviews
- Portfolio demonstrations
- Troubleshooting
- Regression comparisons
- Release documentation

---

# 15. Relationship to Other Documentation

This directory complements:

- Validation README
- Execution README
- Validation Reports
- Performance Reports
- Operational Runbooks
- Troubleshooting Guide

Screenshots should always be referenced from reports rather than embedded unnecessarily.

---

# 16. Future Enhancements

Future screenshot categories may include:

- Spark Web UI
- Kafka monitoring dashboards
- Prometheus metrics
- Grafana dashboards
- Airflow UI
- Cloud deployment validation
- Kubernetes dashboards
- Distributed cluster monitoring

---

# 17. Engineering Principles

Visual evidence should be:

- Accurate
- Traceable
- Reproducible
- Well organized
- Easy to review
- Easy to locate

Every screenshot should provide value.

Screenshots are collected to complement engineering evidence—not to increase repository size. A small collection of meaningful screenshots is significantly more valuable than a large number of repetitive images.