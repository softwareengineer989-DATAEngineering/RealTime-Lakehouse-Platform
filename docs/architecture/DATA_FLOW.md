# RealTime-Lakehouse-Platform Data Flow

---

Version: Sprint 17 – Phase 6E

Status: Authoritative Data Flow Document

Repository Scope: Local Production-Oriented Portfolio Implementation

---

# 1. Purpose

This document describes the complete end-to-end data movement implemented within the RealTime-Lakehouse-Platform repository.

It explains how data flows through each processing stage, the responsibilities of every layer, and the validation performed before analytical datasets are produced.

This document reflects the implemented repository and intentionally avoids describing infrastructure or processing stages that do not exist.

---

# 2. End-to-End Pipeline Overview

```text
                    Instacart Orders Dataset
                               │
                               ▼
                    Python Kafka Producer
                               │
                               ▼
                        Kafka Topic
                               │
                               ▼
                Spark Structured Streaming
                     Bronze Ingestion
                               │
                               ▼
                     Bronze Delta Table
                               │
                               ▼
                  Data Quality Validation
                               │
                ┌──────────────┴──────────────┐
                │                             │
                ▼                             ▼
         Valid Records                 Invalid Records
                │                  (Quality Split Branch)
                ▼
        Silver Transformations
                │
                ▼
        Silver Delta Table
                │
                ▼
        Gold Aggregations
                │
                ▼
         Gold Delta Table
                │
                ▼
      Validation & Evidence Generation
```

---

# 3. Source Dataset

The pipeline begins with the Instacart Orders dataset.

Responsibilities

- provide streaming source records
- preserve original business values
- support repeatable validation
- enable full-dataset execution

Input format

- CSV files

Output

- Python event stream

---

# 4. Kafka Producer

The producer converts dataset records into Kafka events.

Responsibilities

- read dataset
- serialize records
- publish events
- maintain processing order during local execution

Input

Dataset records

Output

Kafka messages

---

# 5. Kafka Layer

Kafka acts as the streaming buffer between data production and downstream processing.

Responsibilities

- decouple producer and consumers
- buffer streaming events
- support continuous ingestion
- provide reliable message delivery for local execution

Input

Producer events

Output

Spark Structured Streaming source

---

# 6. Bronze Layer

Purpose

Capture incoming events with minimal transformation.

Input

Kafka events

Processing

- JSON deserialization
- schema application
- metadata preservation
- Delta write

Output

Bronze Delta Table

Characteristics

- append-oriented writes
- immutable raw history
- dedicated checkpoint
- independent streaming query

---

# 7. Data Quality Stage

Before records enter the Silver layer, the pipeline performs validation.

Implemented validation includes

- required fields
- positive identifiers
- order number validation

Processing result

```text
                 Bronze Records
                       │
                       ▼
              Data Quality Rules
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
   Valid Records             Invalid Records
         │                 (Logical Quality Split)
         ▼
   Silver Processing
```

Current implementation

- valid records continue through the pipeline
- invalid records are separated logically during validation
- no dedicated persisted quarantine table is currently implemented

---

# 8. Silver Layer

Purpose

Transform validated records into standardized analytical datasets.

Input

Validated Bronze records

Implemented transformations

- lowercase normalization
- business-friendly naming
- derived attributes
- first-order indicator
- cleaned schema

Output

Silver Delta Table

---

# 9. Gold Layer

Purpose

Produce business-level analytical datasets.

Input

Silver Delta

Implemented aggregations

- customer order totals
- average order hour
- average days between orders
- first order number
- last order number

Output

Gold Delta Table

Output Mode

Complete

---

# 10. Validation Flow

After successful execution the repository generates validation evidence.

```text
Bronze
     │
Silver
     │
Gold
     │
Runtime Validators
     │
Validation Reports
     │
Execution Evidence
```

Validation verifies

- record counts
- Delta metadata
- runtime configuration
- platform configuration
- pipeline completion

---

# 11. Checkpoint Flow

Each streaming stage owns an independent checkpoint.

```text
Kafka
   │
Bronze Stream
   │
bronze checkpoint

Bronze Delta
   │
Silver Stream
   │
silver checkpoint

Silver Delta
   │
Gold Stream
   │
gold checkpoint
```

This separation reduces coupling between streaming stages and allows stage-level recovery using Spark Structured Streaming checkpoints.

---

# 12. Runtime Outputs

Pipeline execution produces

Source Data

↓

Kafka Events

↓

Bronze Delta

↓

Silver Delta

↓

Gold Delta

↓

Validation Reports

↓

Execution Artifacts

↓

Release Evidence

---

# 13. Implemented Data Flow Characteristics

The current implementation provides

- event-driven processing
- streaming ingestion
- Medallion Architecture
- Delta Lake persistence
- independent checkpoints
- validation framework
- repeatable execution
- local Docker deployment

---

# 14. Scope Boundaries

This repository intentionally represents a production-oriented local implementation.

Included

- Kafka
- Spark Structured Streaming
- Delta Lake
- Medallion Architecture
- Docker Compose
- validation evidence

Not included

- cloud deployment
- distributed Spark cluster
- Kubernetes
- Airflow orchestration
- centralized monitoring
- exactly-once guarantees
- persisted quarantine tables

Future productionization may introduce these capabilities without changing the overall pipeline architecture.

---

# Related Documentation

- [Platform Architecture](ARCHITECTURE.md)
- [Platform Components](COMPONENTS.md)
- [Repository Structure](REPOSITORY_STRUCTURE.md)
- [Validation Runbook](../runbooks/validation-runbook.md)
- [Project Overview](../../README.md)