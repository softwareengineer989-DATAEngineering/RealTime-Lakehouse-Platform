# Validation Artifacts

This directory contains execution evidence generated while validating the Real-Time Lakehouse Platform.

The artifacts are intended to demonstrate reproducible platform execution, operational validation, and engineering evidence commonly expected in production data engineering environments.

---

# Purpose

Validation artifacts provide evidence that the platform executed successfully and that all major engineering components operated as expected.

Examples include:

- Platform validation reports
- Runtime execution logs
- Delta Lake metadata validation
- Streaming execution evidence
- Dataset profile execution results
- Kafka topic validation
- Docker runtime information
- Spark execution logs

These files are generated during platform validation and are not considered source code.

---

# Directory Structure

```text
validation_artifacts/

├── executions/
│
├── reports/
│
├── runtime/
│
├── kafka/
│
├── spark/
│
└── timing/
```

Actual contents may vary depending on the executed validation profile.

---

# Validation Workflow

Typical validation sequence:

```text
Platform Startup
        │
        ▼
Kafka Producer
        │
        ▼
Bronze Stream
        │
        ▼
Silver Stream
        │
        ▼
Gold Stream
        │
        ▼
scripts/validate_all.py
        │
        ▼
Validation Artifacts
```

---

# Dataset Profiles

Artifacts may differ depending on the selected dataset profile.

| Profile | Description |
|----------|-------------|
| Default | Quick validation using the lightweight dataset |
| FULL | Complete production-scale validation using the 3.4 million record dataset |

---

# Generated Reports

Typical reports include:

- Platform validation report
- Runtime validation report
- Delta metadata report
- Delta layer validation
- Kafka topic information
- Docker environment information
- Streaming execution logs
- Timing summaries

---

# Notes

Validation artifacts are generated outputs intended to support engineering verification and repository demonstrations.

They may be regenerated at any time by executing the platform and running:

```bash
python scripts/validate_all.py
```

These files are included as engineering evidence for this portfolio project.