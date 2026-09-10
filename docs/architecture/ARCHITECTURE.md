# RealTime-Lakehouse-Platform Architecture

---

Version: Sprint 17 – Phase 6E

Status: Authoritative Architecture Document

Repository Scope: Local Production-Oriented Portfolio Implementation

---

# 1. Purpose

RealTime-Lakehouse-Platform is a production-oriented local streaming data platform that demonstrates modern Data Engineering practices using Apache Kafka, Apache Spark Structured Streaming, Delta Lake and a Medallion Architecture.

The project was built as a portfolio implementation to demonstrate engineering practices commonly expected from Senior Data Engineers and Data Platform Engineers while remaining technically accurate to the implemented repository.

The repository focuses on:

- streaming ingestion
- layered data architecture
- Delta Lake
- structured validation
- automated testing
- reproducible local execution
- operational documentation
- engineering discipline

The implementation targets a local Docker-based execution model and intentionally does not claim cloud-native production deployment.

---

# 2. Architectural Goals

The platform was designed around the following engineering objectives.

## Functional Goals

- Stream Instacart order events through Kafka
- Process data continuously using Spark Structured Streaming
- Persist Bronze, Silver and Gold Delta tables
- Validate platform configuration and runtime state
- Produce reproducible execution evidence

## Engineering Goals

- Modular architecture
- Clear separation of responsibilities
- Independent streaming stages
- Configuration-driven runtime
- Maintainable repository structure
- Observable execution
- Repeatable validation
- Production-oriented engineering practices

---

# 3. High-Level Architecture

```
                    Instacart Dataset
                            │
                            ▼
                  Python Kafka Producer
                            │
                            ▼
                    Kafka Topic (orders.raw)
                            │
                            ▼
             Spark Structured Streaming
                  Bronze Pipeline
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
             │                      (Quality Branch)
             ▼                             │
      Silver Transformations         Split from stream
             │                             │
             ▼                             │
        Silver Delta Table                 │
             │                             │
             ▼                             │
        Gold Aggregations                  │
             │                             │
             ▼                             │
         Gold Delta Table                  │
             │
             ▼
    Platform Validation Framework
             │
             ▼
     Validation Reports & Evidence
```

---

# 4. Core Platform Components

## Dataset Layer

Provides the source data used for streaming.

Current implementation uses the Instacart Orders dataset together with generated sample datasets for validation.

Responsibilities

- input dataset
- schema consistency
- repeatable execution

---

## Kafka Ingestion Layer

Responsible for event ingestion.

Current implementation publishes order records into Kafka where Spark Structured Streaming consumes them.

Primary streaming topic:

```
orders.raw
```

Additional platform topics are defined for future platform evolution, including validated, dead-letter, customer and audit topics, although the implemented Bronze pipeline consumes the `orders.raw` topic. fileciteturn225file10 fileciteturn226file10

Responsibilities

- event ingestion
- buffering
- decoupling producer and consumers
- streaming source

---

## Bronze Layer

Purpose

Capture incoming events with minimal transformation.

Responsibilities

- consume Kafka events
- deserialize JSON
- preserve source structure
- persist Bronze Delta table

Characteristics

- append-only streaming writes
- Delta Lake storage
- dedicated checkpoint
- independent streaming query

---

## Silver Layer

Purpose

Improve data quality and standardize records before downstream analytics.

Current implementation performs:

- required field validation
- positive ID validation
- order number validation
- valid/invalid record split
- lowercase normalization
- first-order flag derivation
- business-friendly column naming

Only valid records continue into Silver processing. Invalid records are separated logically by the quality split stage in the current implementation. fileciteturn226file1 fileciteturn226file2 fileciteturn226file3 fileciteturn226file4

---

## Gold Layer

Purpose

Provide analytical datasets.

Current implementation performs customer-level aggregations including:

- total orders
- average order hour
- average days between orders
- first order number
- last order number

The Gold layer writes streaming aggregation results into a Delta table using Complete output mode. fileciteturn226file6 fileciteturn226file7 fileciteturn226file8

---

## Validation Framework

The platform includes a dedicated validation framework that executes independent validators for:

- Runtime
- Environment
- Configuration
- Kafka
- Bronze
- Silver
- Gold
- Quality

Validation reports are generated automatically after execution and provide reproducible execution evidence. fileciteturn225file13 fileciteturn226file11

---

# 5. Runtime Architecture

The repository separates runtime artifacts from source code.

```
Repository

├── datasets/
├── src/
├── tests/
├── docker/
├── docs/
├── validation_artifacts/

Runtime

├── data/
│   ├── bronze/
│   ├── silver/
│   ├── gold/
│   └── dlq/
│
├── checkpoints/
│   ├── bronze/
│   ├── silver/
│   └── gold/
│
└── logs/
```

Runtime paths are resolved centrally through the `ProjectPaths` abstraction, allowing consistent execution across local development, Docker and CI-oriented environments. fileciteturn226file0

---

# 6. Streaming Architecture

The platform implements three independent Spark Structured Streaming jobs.

Bronze

Kafka

↓

Bronze Delta

Silver

Bronze Delta

↓

Validation

↓

Transformation

↓

Silver Delta

Gold

Silver Delta

↓

Aggregations

↓

Gold Delta

Each stage owns its own checkpoint directory and streaming lifecycle.

---

# 7. Storage Architecture

Persistent storage uses Delta Lake.

Implemented tables

- Bronze
- Silver
- Gold

Characteristics

- ACID transactions
- Delta transaction logs
- version history
- streaming read/write support

No partition columns are currently configured for these Delta tables according to the validated execution evidence. fileciteturn226file11

---

# 8. Checkpoint Strategy

Each streaming stage maintains an independent checkpoint location.

```
checkpoints/

├── bronze/

├── silver/

└── gold/
```

Benefits

- independent recovery boundaries
- isolated stream state
- reduced coupling between streaming jobs
- stage-level restart capability

The current implementation documents checkpoint-backed streaming but does not claim end-to-end exactly-once guarantees or validated restart semantics beyond the implemented checkpoint mechanism.

---

# 9. Spark Runtime Configuration

The Spark runtime is configured centrally.

Current configuration includes:

- Delta Lake extensions
- Delta catalog
- Adaptive Query Execution
- Kryo serialization
- UTC session timezone
- Driver memory: 2 GB
- Executor memory: 2 GB

These settings are defined through a unified Spark configuration used when constructing the Spark session. fileciteturn226file9 fileciteturn225file6

---

# 10. Reliability Considerations

Implemented

- isolated streaming stages
- dedicated checkpoints
- graceful shutdown support
- centralized path management
- validation framework
- structured logging
- runtime configuration abstraction

Not claimed

- exactly-once processing
- distributed cluster deployment
- high availability
- cloud-native orchestration
- automatic failover
- multi-region deployment

---

# 11. Validation Evidence

The current repository includes validated execution evidence.

Verified results include:

| Layer | Records |
|---------|---------:|
| Bronze | 3,421,083 |
| Silver | 3,421,083 |
| Gold | 206,209 |

Platform validation reports confirm:

- 8 validators executed
- 8 validators passed
- 0 validation failures

These results represent a successful full-dataset local validation of the implemented platform.

---

### Validation Architecture Evolution

The validation layer is intentionally structured as an independent architectural component within the streaming pipeline. This separation allows validation rules, operational reporting, and downstream quality workflows to evolve independently of the ingestion and transformation stages while preserving the overall pipeline architecture.

The current implementation demonstrates rule-based validation integrated with the streaming data flow and establishes the architectural foundation for future expansion of operational quality capabilities without requiring changes to the Medallion architecture or the platform deployment model.

# 12. Architectural Scope

This repository intentionally represents a production-oriented local implementation.

Included

- Docker-based execution
- Kafka streaming
- Spark Structured Streaming
- Delta Lake
- Medallion Architecture
- Validation framework
- Testing
- Documentation
- Operational runbooks

Outside Current Scope

- Kubernetes
- Cloud object storage
- Managed Kafka
- Airflow
- dbt
- Terraform
- OpenTelemetry
- Prometheus
- Grafana
- Multi-node Spark clusters

These technologies may be introduced in future platform evolution but are not part of the implemented Sprint 17 architecture.

---

# 13. Architecture Principles

The implementation follows the following engineering principles.

- Separate ingestion from processing.
- Isolate streaming stages.
- Keep runtime artifacts outside source code.
- Validate continuously.
- Prefer reproducible execution over undocumented assumptions.
- Organize the repository for long-term maintainability.
- Document implemented behavior rather than aspirational architecture.

---

# Related Documentation

This document describes the overall architecture of the Real-Time Lakehouse Platform.

For related engineering documentation, see:

- [Project Overview](../../README.md)
- [Platform Components](COMPONENTS.md)
- [Streaming Data Flow](DATA_FLOW.md)
- [Repository Structure](REPOSITORY_STRUCTURE.md)
- [Operational Runbooks](../runbooks/)
- [Architecture Decision Records](../decisions/)
- [Project Roadmap](../ROADMAP.md)