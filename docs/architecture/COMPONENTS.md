# RealTime-Lakehouse-Platform Components

---

Version: Sprint 17 – Phase 6E

Status: Authoritative Component Reference

Repository Scope: Local Production-Oriented Portfolio Implementation

---

# 1. Purpose

This document describes the primary software components that make up the RealTime-Lakehouse-Platform repository.

Each component is documented using its implemented responsibility, interfaces, dependencies, runtime behavior, operational considerations, and testing responsibilities.

This document reflects the implemented repository and does not describe technologies that are outside the current project scope.

---

# 2. Platform Overview

The platform is composed of several independent but coordinated components.

```
                    Source Dataset
                           │
                           ▼
                    Python Producer
                           │
                           ▼
                    Apache Kafka
                           │
                           ▼
              Spark Structured Streaming
                           │
        ┌──────────┬──────────┬──────────┐
        ▼          ▼          ▼
     Bronze     Silver      Gold
        │          │          │
        └──────────┴──────────┘
                   │
                   ▼
        Validation Framework
                   │
                   ▼
        Runtime Evidence & Reports
```

Every component owns a clearly defined responsibility and communicates only through well-defined interfaces.

---

# 3. Source Dataset Component

## Responsibility

Provides the input data streamed through the platform.

## Inputs

None

## Outputs

CSV records consumed by the Kafka producer.

## Dependencies

- Local dataset files

## Operational Notes

- Read-only component
- Supports repeatable executions
- Enables full-dataset validation

---

# 4. Kafka Producer Component

## Responsibility

Reads the dataset and publishes events into Kafka.

## Inputs

Dataset records

## Outputs

Kafka messages

## Dependencies

- Python runtime
- Kafka broker

## Failure Modes

- Kafka unavailable
- Invalid dataset path
- Serialization failure

## Recovery

Execution can be restarted after resolving the underlying issue.

---

# 5. Kafka Broker Component

## Responsibility

Acts as the streaming backbone of the platform.

## Inputs

Producer events

## Outputs

Streaming events consumed by Spark Structured Streaming.

## Dependencies

- Docker Compose
- Kafka container

## Operational Considerations

- Topic must exist before streaming begins.
- Broker must be healthy before producer execution.
- Consumers operate independently from the producer.

---

# 6. Bronze Processing Component

## Responsibility

Captures incoming Kafka events with minimal transformation.

## Inputs

Kafka topic

## Outputs

Bronze Delta table

## Processing

- JSON deserialization
- Schema application
- Raw event persistence

## Dependencies

- Spark Structured Streaming
- Delta Lake
- Bronze checkpoint

## Failure Modes

- Kafka unavailable
- Invalid schema
- Delta write failure

## Recovery

Streaming resumes using the Bronze checkpoint.

---

# 7. Data Quality Component

## Responsibility

Validates records before downstream processing.

## Inputs

Bronze records

## Outputs

Validated records for Silver processing.

## Implemented Validation Rules

- Required fields
- Positive identifiers
- Order number validation

## Current Behavior

Valid records continue through the processing pipeline.

Invalid records are separated logically during validation.

A dedicated persisted quarantine table is outside the current implementation scope.

---

# 8. Silver Processing Component

## Responsibility

Transforms validated Bronze data into standardized business records.

## Inputs

Validated Bronze records

## Outputs

Silver Delta table

## Implemented Transformations

- Column normalization
- Business-friendly naming
- Derived columns
- First-order indicator

## Dependencies

- Silver checkpoint
- Delta Lake

## Failure Modes

- Invalid transformation
- Delta write error

## Recovery

Streaming resumes using the Silver checkpoint.

---

# 9. Gold Processing Component

## Responsibility

Produces analytical datasets from Silver records.

## Inputs

Silver Delta table

## Outputs

Gold Delta table

## Implemented Aggregations

- Total customer orders
- Average order hour
- Average days between orders
- First order number
- Last order number

## Output Mode

Complete

## Dependencies

- Gold checkpoint
- Delta Lake

## Failure Modes

- Aggregation failure
- Streaming interruption

## Recovery

Streaming resumes using the Gold checkpoint.

---

# 10. Delta Lake Storage Component

## Responsibility

Provides transactional storage for all Medallion layers.

## Managed Tables

- Bronze
- Silver
- Gold

## Characteristics

- ACID transactions
- Version history
- Transaction log
- Streaming support

## Dependencies

Spark SQL with Delta Lake extensions.

---

# 11. Checkpoint Component

## Responsibility

Maintains streaming state independently for each processing stage.

## Checkpoint Locations

- Bronze
- Silver
- Gold

## Responsibilities

- Offset tracking
- Stateful streaming metadata
- Restart support

## Operational Notes

Checkpoint deletion resets streaming progress and should be treated as a destructive maintenance operation.

---

# 12. Validation Framework Component

## Responsibility

Validates platform correctness after execution.

## Inputs

Runtime environment

Delta tables

Platform configuration

Execution artifacts

## Outputs

Validation reports

Execution evidence

## Validation Areas

- Runtime
- Configuration
- Kafka
- Bronze
- Silver
- Gold
- Metadata
- Data quality

---

# 13. Runtime Configuration Component

## Responsibility

Provides centralized configuration for the platform.

## Responsibilities

- Resolve project paths
- Configure Spark
- Configure runtime locations
- Environment abstraction

## Benefits

- Reduced hard-coded paths
- Consistent execution
- Easier maintenance

---

# 14. Docker Platform Component

## Responsibility

Provides the local execution environment.

## Managed Services

- Apache Kafka
- Apache Spark

## Responsibilities

- Container lifecycle
- Networking
- Volume mounting
- Local reproducibility

---

# 15. Testing Component

## Responsibility

Verifies repository correctness.

## Coverage

- Unit tests
- Integration tests
- Pipeline validation
- CI execution

Large-scale execution evidence complements automated testing but is documented separately within the validation artifacts.

---

# 16. Documentation Component

## Responsibility

Documents the implemented platform.

The documentation system is organized into:

- Architecture
- ADRs
- Runbooks
- Security
- Diagrams
- Repository README

This structure ensures that architectural explanations, operational guidance, and design decisions remain independent and maintainable.

---

# 17. Component Interaction Summary

The overall execution sequence is:

```
Dataset
   │
Producer
   │
Kafka
   │
Bronze
   │
Quality Validation
   │
Silver
   │
Gold
   │
Validation
   │
Execution Evidence
```

Each component owns a single responsibility and communicates with adjacent components through clearly defined interfaces.

This modular design simplifies testing, maintenance, operational troubleshooting, and future enhancement while remaining faithful to the implemented repository.

---

# Related Documentation

- [Platform Architecture](ARCHITECTURE.md)
- [Streaming Data Flow](DATA_FLOW.md)
- [Repository Structure](REPOSITORY_STRUCTURE.md)
- [Operational Runbooks](../runbooks/)
- [Project Overview](../../README.md)