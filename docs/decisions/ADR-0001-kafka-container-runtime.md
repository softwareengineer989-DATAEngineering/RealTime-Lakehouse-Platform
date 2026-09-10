# ADR-001: Kafka Container Runtime Selection

**Status:** Accepted

**Date:** 2026-08-24

**Sprint:** Sprint 5 (Initial Adoption), Updated in Sprint 15.5

---

# Context

The RealTime Lakehouse Platform requires a reliable Apache Kafka environment to support real-time event ingestion and streaming data processing.

Kafka serves as the event backbone connecting the data producer, Spark Structured Streaming jobs, and downstream Lakehouse processing layers.

To support local development, automated testing, and reproducible execution, the project required a containerized Kafka deployment.

---

# Problem Statement

The platform requires a Kafka runtime that:

- is reproducible across development environments
- integrates cleanly with Docker Compose
- supports Spark Structured Streaming
- minimizes manual configuration
- is stable for local development
- aligns with production-oriented engineering practices

The selected solution should also provide a low onboarding cost for contributors while remaining representative of enterprise deployment patterns.

---

# Decision Drivers

The following requirements guided the selection.

## Functional

- Apache Kafka compatibility
- Docker support
- Stable networking
- Topic management
- Producer compatibility
- Consumer compatibility
- Spark Structured Streaming compatibility

## Operational

- Simple startup
- Reproducible environment
- Easy troubleshooting
- Minimal configuration
- Community adoption

## Portfolio

The repository should demonstrate realistic containerized infrastructure while remaining easy for recruiters and contributors to execute locally.

---

# Options Considered

## Option 1 — Native Kafka Installation

### Advantages

- Direct access to Kafka binaries
- Maximum configuration flexibility

### Disadvantages

- Platform-specific setup
- Difficult onboarding
- Inconsistent developer environments
- Higher maintenance effort

**Decision**

Rejected.

---

## Option 2 — Bitnami Kafka Container

### Advantages

- Well-documented image
- Active maintenance
- Docker support

### Disadvantages

- More opinionated configuration
- Environment variable complexity
- Additional abstraction over upstream Kafka

**Decision**

Considered during early project planning but not selected for the final platform implementation.

---

## Option 3 — Apache Kafka Container (Official Apache Distribution)

### Advantages

- Uses Apache Kafka directly
- Close alignment with upstream project
- Predictable behavior
- Strong compatibility with Spark Structured Streaming
- Suitable for local development and portfolio demonstrations

### Disadvantages

- Still represents a single-node local deployment
- Does not model production clustering

**Decision**

Accepted.

---

# Decision

The project adopts an Apache Kafka Docker container managed through Docker Compose as the standard local runtime.

Kafka is treated as an independent platform service that can be started, stopped, or rebuilt without modifying application code.

This separation reinforces modularity and simplifies development workflows.

---

Kafka CLI tools are intentionally executed inside the running Docker container using docker exec rather than requiring a host-level Kafka installation. This keeps development environments reproducible across contributors and operating systems.

# Architecture

```
Docker Compose

│

├── Kafka

├── Spark

├── Producer

└── Supporting Services
```

Kafka acts as the messaging backbone between producers and streaming consumers.

---

# Operational Workflow

Developer

↓

Docker Compose Up

↓

Kafka Starts

↓

Producer Publishes Events

↓

Spark Structured Streaming Consumes Events

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer

---

# Benefits

The selected approach provides:

- Consistent development environments
- Reproducible execution
- Simplified onboarding
- Platform isolation
- Easy container lifecycle management
- Compatibility with automated testing
- Reduced host machine dependencies

---

# Risks

## Single Node Deployment

The development environment uses a single Kafka broker.

### Impact

Does not represent production-scale clustering.

### Mitigation

The application is designed so that Kafka infrastructure can be replaced by a multi-node cluster without changing application logic.

---

## Local Resource Constraints

Kafka containers consume CPU, memory, and disk resources.

### Mitigation

Sample datasets are used during development to reduce resource requirements.

Production-scale validation is performed separately using the complete dataset.

---

## Docker Dependency

Running the platform requires Docker Desktop (or an equivalent container runtime).

### Mitigation

Containerization improves reproducibility and simplifies environment setup across contributors.

---

# Alternatives for Production

Future production deployments may replace the local Docker runtime with:

- Amazon MSK
- Confluent Platform
- Azure Event Hubs (Kafka API)
- Self-managed Kafka clusters
- Kubernetes-based Kafka operators

The application architecture intentionally avoids coupling business logic to the underlying Kafka deployment.

---

# Operational Considerations

The platform treats Kafka as infrastructure rather than application code.

Operational responsibilities include:

- Topic management
- Broker monitoring
- Container health
- Log inspection
- Restart procedures
- Configuration management

These responsibilities remain isolated from business processing logic.

---

# Consequences

## Positive

- Simplified local setup
- Reproducible environments
- Faster onboarding
- Clean Docker integration
- Reliable Spark compatibility
- Improved portability

## Negative

- Not representative of production clustering
- Requires Docker installation
- Limited scalability in local mode

---

# Validation

The selected runtime has been validated through:

- Kafka producer execution
- Spark Structured Streaming ingestion
- Bronze layer processing
- Silver layer processing
- Gold layer processing
- Graceful shutdown
- Runtime recovery
- Retry framework
- GitHub Actions validation (application-level testing)

These validations demonstrate that the selected runtime satisfies the project's development and portfolio objectives.

---

# Future Considerations

Potential future enhancements include:

- Multi-broker Kafka clusters
- Kafka KRaft production configuration
- Kubernetes deployment
- High availability
- Monitoring with Prometheus
- Grafana dashboards
- Schema Registry integration

These enhancements can be introduced without changing the platform's application architecture.

---

# References

- Docker Compose configuration
- Kafka platform configuration
- Spark Structured Streaming implementation
- Project README
- Sprint 5 – Kafka Foundation
- Sprint 15 – Production Readiness

---

## Related Documentation

- [Platform Architecture](../architecture/ARCHITECTURE.md)
- [Kafka Operations](../runbooks/kafka-operations.md)