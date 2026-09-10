# RealTime-Lakehouse-Platform Repository Structure

---

Version: Sprint 17 – Phase 6E

Status: Authoritative Repository Structure Document

Repository Scope: Local Production-Oriented Portfolio Implementation

---

# 1. Purpose

This document describes the organization of the RealTime-Lakehouse-Platform repository.

The repository has been intentionally structured to separate application source code, runtime artifacts, operational evidence, documentation, testing, and infrastructure.

The objective is to provide a maintainable project layout that supports development, testing, validation, and long-term evolution.

---

# 2. Repository Design Principles

The repository follows several engineering principles.

- Separate source code from runtime artifacts.
- Keep infrastructure isolated from application logic.
- Store validation evidence independently from implementation.
- Organize documentation by purpose.
- Preserve operational reproducibility.
- Minimize coupling between platform components.

---

# 3. High-Level Repository Layout

```text
RealTime-Lakehouse-Platform/

├── datasets/
├── docker/
├── docs/
├── scripts/
├── src/
├── tests/
├── validation_artifacts/
├── checkpoints/
├── data/
├── logs/
├── artifacts/
├── .github/
├── requirements.txt
├── requirements-dev.txt
├── docker-compose.yml
├── pyproject.toml
├── pytest.ini
└── README.md
```

---

# 4. Source Code

## src/

Contains the application implementation.

Responsibilities

- streaming pipelines
- business transformations
- Spark configuration
- Kafka integration
- Delta Lake interaction
- utilities
- runtime configuration

This directory represents the primary implementation of the platform.

---

# 5. Scripts

## scripts/

Contains operational utilities used outside the core application.

Examples include

- validation utilities
- smoke tests
- metadata inspection
- project verification
- release support

These scripts assist development and validation but are not part of the runtime streaming pipeline.

---

# 6. Tests

## tests/

Contains the automated test suite.

Typical responsibilities include

- unit testing
- integration testing
- transformation validation
- configuration verification
- pipeline correctness

Automated tests complement, but do not replace, full-dataset execution validation.

---

# 7. Docker

## docker/

Contains container definitions required for the local execution environment.

Responsibilities

- Spark image definition
- supporting runtime configuration
- local platform deployment

Docker Compose orchestrates these services during platform execution.

---

# 8. Documentation

## docs/

Contains all engineering documentation.

Current organization

```text
docs/

├── architecture/
├── decisions/
├── diagrams/
├── diagrams-source/
├── assets/
├── runbooks/
├── security/
└── README.md
```

Purpose of each directory

### architecture/

Authoritative technical documentation describing the implemented platform.

### decisions/

Architecture Decision Records (ADRs) documenting important engineering choices.

### diagrams/

Mermaid source diagrams maintained as version-controlled documentation.

### diagrams-source/

Editable Draw.io source files.

### assets/

Exported PNG images referenced by repository documentation.

### runbooks/

Operational procedures for local platform execution and maintenance.

### security/

Repository security guidance and responsible disclosure information.

---

# 9. Runtime Data

The repository intentionally separates runtime outputs from implementation.

## data/

Stores Delta Lake tables generated during execution.

Current structure

```text
data/

├── bronze/
├── silver/
└── gold/
```

These directories are regenerated during pipeline execution.

---

# 10. Streaming Checkpoints

## checkpoints/

Stores Spark Structured Streaming checkpoints.

Current structure

```text
checkpoints/

├── bronze/
├── silver/
└── gold/
```

Each streaming query owns an independent checkpoint.

Deleting these directories resets the streaming state and should therefore be treated as a destructive maintenance operation.

---

# 11. Logs

## logs/

Stores runtime log files generated during execution.

Typical contents include

- application logs
- execution logs
- troubleshooting information

These files are considered runtime artifacts and may be regenerated.

---

# 12. Validation Artifacts

## validation_artifacts/

Contains reproducible evidence generated during platform validation.

Typical categories include

- execution reports
- runtime information
- Kafka evidence
- metadata validation
- release evidence
- screenshots
- timing reports
- testing outputs

This directory represents the engineering evidence supporting the repository.

---

# 13. Datasets

## datasets/

Stores input datasets used during local execution.

Responsibilities

- source data
- sample datasets
- development utilities

These files are read-only inputs for the streaming pipeline.

---

# 14. GitHub Configuration

## .github/

Contains repository automation.

Typical contents include

- CI workflow
- issue templates
- pull request template
- CODEOWNERS
- Dependabot configuration

These files support repository governance rather than application execution.

---

# 15. Root Configuration Files

The repository root contains project-level configuration.

| File | Purpose |
|------|---------|
| README.md | Project overview |
| docker-compose.yml | Local platform orchestration |
| pyproject.toml | Python project configuration |
| pytest.ini | Pytest configuration |
| requirements.txt | Runtime dependencies |
| requirements-dev.txt | Development dependencies |

---

# 16. Repository Boundaries

The repository intentionally separates five concerns.

```text
Application
      │
Infrastructure
      │
Runtime
      │
Validation
      │
Documentation
```

This separation improves maintainability and keeps implementation, operational evidence, and documentation independent.

---

# 17. Engineering Characteristics

The repository organization demonstrates

- modular structure
- clear separation of concerns
- reproducible execution
- isolated runtime state
- maintainable documentation
- validation discipline
- production-oriented engineering practices

The layout is intended for a local Docker-based streaming platform and provides a strong foundation for future production-oriented evolution while accurately reflecting the implemented repository.

---

# Related Documentation

- [Project Overview](../../README.md)
- [Platform Architecture](ARCHITECTURE.md)
- [Platform Components](COMPONENTS.md)
- [Local Development Guide](../runbooks/local-development.md)