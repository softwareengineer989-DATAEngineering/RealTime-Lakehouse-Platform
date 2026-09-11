# Real-Time Lakehouse Platform

> **Production-Oriented, Enterprise-Inspired Streaming Data Engineering Platform**

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://www.python.org/)
[![Apache Spark](https://img.shields.io/badge/Apache%20Spark-4.0-orange.svg)](https://spark.apache.org/)
[![Apache Kafka](https://img.shields.io/badge/Apache%20Kafka-4.1-black.svg)](https://kafka.apache.org/)
[![Delta Lake](https://img.shields.io/badge/Delta%20Lake-4.0-green.svg)](https://delta.io/)
[![Data Quality](https://img.shields.io/badge/Data%20Quality-Validation-success.svg)](docs/architecture/ARCHITECTURE.md)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED.svg)](https://www.docker.com/)
[![Pytest](https://img.shields.io/badge/Tested%20With-Pytest-success.svg)](https://pytest.org/)
[![GitHub Actions](https://img.shields.io/badge/CI-GitHub%20Actions-blue.svg)](https://github.com/features/actions)

---

# Overview

Real-Time Lakehouse Platform is a production-oriented, enterprise-inspired streaming data engineering project that demonstrates how modern data platforms ingest, validate, process, and serve streaming data using **Apache Kafka**, **Apache Spark Structured Streaming**, and **Delta Lake**.

The platform implements a streaming **Medallion Architecture (Bronze → Silver → Gold)** inside a fully containerized local environment while emphasizing engineering practices commonly expected in Senior Data Engineering and Data Platform roles, including modular architecture, automated validation, operational runbooks, testing, continuous integration, reproducible execution, and architecture decision records.

Rather than focusing on cloud infrastructure, this repository demonstrates production engineering principles through a complete end-to-end streaming implementation that is reproducible, observable, and supported by automated validation artifacts.

---

# Validation Workload

The pipeline has been validated locally using the complete **Instacart `orders.csv` dataset** containing **3,421,083 order records**.

This larger-scale validation workload was used to verify streaming execution, Delta Lake processing, Medallion layer outputs, runtime behavior, validation artifacts, and operational reproducibility within the local platform.

# Platform Architecture

```
                   Instacart Dataset
                           │
                           ▼
                  Kafka Producer (Python)
                           │
                           ▼
                    Apache Kafka Topic
                           │
                           ▼
             Spark Structured Streaming
                           │
          ┌────────────────┴────────────────┐
          ▼                                 ▼
   Bronze Delta                     Data Validation
          │
          ▼
    Silver Delta
          │
          ▼
     Gold Delta
          │
          ▼
 Validation & Operational Evidence
```

The platform is organized around independent streaming services that continuously process data through Bronze, Silver, and Gold Delta Lake layers while maintaining checkpoint recovery, runtime validation, and engineering evidence.

For complete architecture documentation, component descriptions, repository structure, and data flow diagrams, see:

- [Platform Architecture](docs/architecture/ARCHITECTURE.md)
- [Platform Components](docs/architecture/COMPONENTS.md)
- [Data Flow](docs/architecture/DATA_FLOW.md)
- [Repository Structure](docs/architecture/REPOSITORY_STRUCTURE.md)



---

# Engineering Highlights

This project demonstrates practical implementation of:

- Apache Kafka event streaming
- Apache Spark Structured Streaming
- Delta Lake Medallion Architecture
- Data Quality Validation Framework
- Docker-based platform deployment
- Automated platform validation
- Runtime health verification
- Operational runbooks
- Architecture Decision Records (ADRs)
- GitHub Actions CI
- Unit and integration testing
- Validation using 3,421,083 Instacart order records

---

# Technology Stack

| Category | Technology |
|-----------|------------|
| Programming Language | Python 3.13 |
| Streaming Platform | Apache Kafka |
| Stream Processing | Apache Spark Structured Streaming |
| Storage Layer | Delta Lake |
| Architecture Pattern | Medallion (Bronze / Silver / Gold) |
| Infrastructure | Docker Compose |
| Configuration | YAML |
| Logging | Python Logging |
| Testing | Pytest |
| Continuous Integration | GitHub Actions |
| Version Control | Git & GitHub |

---

# Repository Structure

```text
RealTime-Lakehouse-Platform/

├── datasets/                  # Source datasets
├── docker/                    # Container configuration
├── docs/                      # Architecture & engineering documentation
├── scripts/                   # Operational scripts & validation
├── src/                       # Application source code
├── tests/                     # Unit and integration tests
├── validation_artifacts/      # Generated execution evidence
│
├── docker-compose.yml
├── pyproject.toml
├── requirements.txt
└── README.md
```

A detailed walkthrough of the repository organization is available in:

```
docs/architecture/REPOSITORY_STRUCTURE.md
```

---

# Quick Start

## 1. Clone the Repository

```bash
git clone https://github.com/<your-github-username>/RealTime-Lakehouse-Platform.git

cd RealTime-Lakehouse-Platform
```

---

## 2. Create Python Environment

```bash
python -m venv .venv
```

Windows

```powershell
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Download the Dataset

Download the Instacart Online Grocery Basket Analysis dataset from Kaggle:

https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset

Place the required dataset files into the project's `datasets/` directory before starting the streaming platform.

## 5. Start Docker Services

```bash
docker compose up -d
```

Verify:

```bash
docker compose ps
```

---

## 6. Create Kafka Topics

```powershell
.\scripts\create_topics.ps1
```

---

## 7. Start the Streaming Platform

```powershell
.\scripts\start_platform.ps1
```

This starts the streaming services in the correct dependency order:

- Bronze Streaming
- Silver Streaming
- Gold Streaming

The platform remains running until explicitly stopped.

---

## 8. Publish Streaming Events

```bash
python src/retaillake/kafka/producer/stream_instacart.py
```

---

## 9. Validate the Platform

```bash
python scripts/validate_all.py
```

---

## 10. Stop the Streaming Platform

```powershell
.\scripts\stop_platform.ps1
```

If you also want to stop the Docker environment:

```bash
docker compose down
```

---

# Dataset Profiles

The platform supports multiple execution profiles.

| Profile | Purpose | Runtime |
|----------|----------|---------|
| Default | Quick demonstration | Under 1 minute |
| FULL | Complete validation using 3,421,083 Instacart order records | Approximately 5–10 minutes |

Default execution uses the lightweight dataset.

For complete dataset validation:

Windows

```powershell
$env:DATASET_PROFILE="FULL"
```

Linux / macOS

```bash
export DATASET_PROFILE=FULL
```

Run the producer normally afterwards.

---

# Dataset

This project uses the **Instacart Online Grocery Basket Analysis** dataset.

## Source

The dataset was obtained from Kaggle:

https://www.kaggle.com/datasets/yasserh/instacart-online-grocery-basket-analysis-dataset

The streaming pipeline uses the **`orders.csv`** file as the event source.

## Validation Dataset

The FULL execution profile validates the platform using:

- Dataset: `orders.csv`
- Records: **3,421,083 order records**
- Purpose:
  - Streaming ingestion validation
  - Bronze → Silver → Gold processing
  - Delta Lake validation
  - Runtime verification
  - Operational evidence generation

The dataset is included solely for educational and portfolio demonstration purposes under the dataset's applicable license and usage terms.

# Validation

The repository includes automated validation scripts that verify platform health, Delta Lake structure, metadata consistency, and project integrity.

Primary validation entry point:

```bash
python scripts/validate_all.py
```

This orchestrates the existing validation suite:

```
scripts/

├── validate_project.py
├── validate_delta_layers.py
├── validate_delta_metadata.py
└── test_delta_smoke.py
```

Each validation script can also be executed independently for targeted verification.

---

# Documentation

Complete engineering documentation is available under the `docs/` directory.

## Project Planning

- [Project Roadmap](docs/ROADMAP.md)

## Architecture

- [Platform Architecture](docs/architecture/ARCHITECTURE.md)
- [Platform Components](docs/architecture/COMPONENTS.md)
- [Data Flow](docs/architecture/DATA_FLOW.md)
- [Repository Structure](docs/architecture/REPOSITORY_STRUCTURE.md)

---

## Operational Runbooks

- [Docker Operations](docs/runbooks/docker-operations.md)
- [Kafka Operations](docs/runbooks/kafka-operations.md)
- [Spark Operations](docs/runbooks/spark-operations.md)
- [Local Development Guide](docs/runbooks/local-development.md)
- [Validation Runbook](docs/runbooks/validation-runbook.md)
- [Troubleshooting Guide](docs/runbooks/troubleshooting.md)

---

## Architecture Decision Records (ADRs)

- [ADR-0001 — Kafka Container Runtime](docs/decisions/ADR-0001-kafka-container-runtime.md)
- [ADR-0002 — Kafka Topic Design](docs/decisions/ADR-0002-kafka-topic-design.md)
- [ADR-0003 — GitHub Actions CI](docs/decisions/ADR-0003-github-actions.md)

---

## Release Notes

- [Sprint 17 Release Notes](docs/release-notes/SPRINT_17.md)

---

## Security

- [Security Policy](docs/security/SECURITY.md)

---

# Testing

The platform includes automated testing and validation covering multiple engineering layers.

| Category | Purpose |
|----------|----------|
| Unit Tests | Validate individual components |
| Smoke Tests | Verify runtime dependencies |
| Delta Validation | Verify Bronze, Silver, and Gold tables |
| Metadata Validation | Validate schemas and Delta metadata |
| Platform Validation | Verify end-to-end platform readiness |
| CI Validation | Automated execution through GitHub Actions |

Run the complete validation suite:

```bash
python scripts/validate_all.py
```

Run individual validation scripts when required:

```bash
python scripts/validate_project.py
```

```bash
python scripts/validate_delta_layers.py
```

```bash
python scripts/validate_delta_metadata.py
```

```bash
python scripts/test_delta_smoke.py
```

---

# Project Scope

This repository demonstrates production-oriented engineering practices for a local streaming data platform.

Current implementation includes:

- Kafka event ingestion
- Spark Structured Streaming
- Bronze → Silver → Gold Medallion Architecture
- Delta Lake storage
- Data quality validation
- Operational automation scripts
- Platform validation framework
- Runtime monitoring
- Containerized execution
- CI with GitHub Actions
- Engineering documentation
- Architecture Decision Records (ADRs)

The project intentionally focuses on engineering quality, maintainability, reproducibility, and operational excellence rather than cloud-specific deployment.

---

# Future Enhancements

Potential future extensions include:

- Apache Airflow orchestration
- dbt transformation layer
- Great Expectations integration
- OpenLineage support
- Prometheus metrics
- Grafana dashboards
- Kubernetes deployment
- Cloud object storage integration
- Infrastructure as Code
- Data catalog integration

These enhancements are intentionally excluded from the current release to maintain a focused and production-quality implementation.

---

# Repository Highlights

This repository demonstrates practical experience with:

- Event-driven data pipelines
- Stream processing
- Lakehouse architecture
- Delta Lake engineering
- Data quality validation
- Operational automation
- Software engineering best practices
- CI/CD workflows
- Documentation-first engineering
- Production-oriented repository organization

The project is designed to showcase engineering practices expected in modern Data Engineering and Data Platform roles.

---

# License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.