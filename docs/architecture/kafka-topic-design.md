# Kafka Topic Design

**Document Type:** Architecture Decision Record (ADR)

**Status:** Accepted

**Date:** 2026-08-24

**Sprint:** Sprint 5 (Initial Design), Updated in Sprint 15.5

---

# Context

The RealTime Lakehouse Platform processes streaming events using Apache Kafka as the messaging backbone.

Kafka topics provide the communication channel between event producers and downstream Spark Structured Streaming consumers.

An appropriate topic design is essential to ensure:

- reliable event delivery
- ordered processing
- scalability
- maintainability
- future extensibility

The platform currently targets a production-inspired architecture while remaining simple enough for local development and educational purposes.

---

# Problem Statement

How should Kafka topics be organized to support:

- streaming ingestion
- Spark Structured Streaming
- Bronze / Silver / Gold processing
- future scalability
- maintainable event routing
- enterprise engineering practices

The design should support future platform growth without requiring major architectural changes.

---

# Decision Drivers

The topic strategy should satisfy the following goals.

## Functional

- Reliable event ingestion
- Ordered event processing
- Spark compatibility
- Producer simplicity
- Consumer simplicity

## Operational

- Easy topic management
- Predictable routing
- Straightforward monitoring
- Minimal operational complexity

## Architectural

- Loose coupling
- Event-driven design
- Future scalability
- Independent processing components

---

# Current Topic Strategy

The platform currently uses a primary topic for streaming order events.

```
instacart-orders
```

The producer publishes order events to this topic.

Spark Structured Streaming consumes events and processes them through the Lakehouse pipeline.

---

# Processing Flow

```
Source Dataset

↓

Producer

↓

Kafka Topic

(instacart-orders)

↓

Spark Structured Streaming

↓

Bronze Layer

↓

Silver Layer

↓

Gold Layer
```

---

# Topic Naming Convention

Topic names should be:

- lowercase
- hyphen-separated
- descriptive
- business-oriented

Examples:

```
instacart-orders

customer-events

inventory-updates

payment-events
```

Avoid generic names such as:

```
topic1

orders

test-topic
```

Descriptive names improve maintainability and operational visibility.

---

# Partitioning Strategy

## Current Implementation

The project currently uses a development-friendly partition configuration suitable for local execution.

This minimizes operational complexity while allowing deterministic processing.

---

## Future Production Strategy

For production-scale deployments, topic partitions should be selected based on:

- expected throughput
- consumer parallelism
- ordering requirements
- hardware capacity

Partition count should be reviewed as workload characteristics evolve.

---

# Message Keys

Kafka message keys determine partition assignment.

Recommended keys include stable business identifiers such as:

- customer_id
- order_id
- user_id

Using business identifiers helps preserve event ordering for related records while distributing workload across partitions.

---

# Ordering Considerations

Kafka guarantees ordering **within a partition**.

The platform therefore favors stable business keys for partition assignment when event order is important.

Examples:

- all events for a single customer
- all updates for a single order

This approach balances ordering guarantees with scalability.

---

# Replication Strategy

## Current Environment

The local development environment uses a single Kafka broker.

Replication is therefore not applicable.

---

## Future Production Environment

Production deployments should configure replication according to infrastructure requirements.

Typical considerations include:

- fault tolerance
- high availability
- maintenance windows

Replication settings should be determined alongside cluster architecture.

---

# Retention Policy

## Development

Development environments prioritize simplicity and reproducibility.

Retention settings remain suitable for local testing.

---

## Production

Retention should be determined by:

- storage capacity
- recovery requirements
- replay requirements
- compliance policies

Retention policies should be documented alongside operational procedures.

---

# Topic Compaction

The current implementation does not require log compaction.

Future event types involving mutable entity state may benefit from compacted topics where appropriate.

---

# Consumer Groups

Spark Structured Streaming operates as the primary consumer of the streaming topic.

Future platform evolution may introduce additional independent consumer groups such as:

- monitoring services
- alerting services
- analytics consumers
- audit pipelines

Consumer groups enable independent processing without duplicating producers.

---

# Dead Letter Queue (Future)

The current platform handles validation failures within the processing pipeline.

Future production deployments may introduce dedicated Dead Letter Queue (DLQ) topics.

Example:

```
instacart-orders-dlq
```

Potential use cases include:

- malformed messages
- schema validation failures
- unrecoverable processing errors

A DLQ allows failed events to be isolated for later inspection without interrupting normal processing.

---

# Monitoring Considerations

Operational monitoring should include:

- topic availability
- consumer lag
- message throughput
- partition health
- producer errors
- consumer errors

These metrics help identify bottlenecks and operational issues.

---

# Benefits

The selected topic design provides:

- clear event organization
- simple producer logic
- straightforward consumer implementation
- compatibility with Spark Structured Streaming
- future scalability
- maintainable naming conventions

---

# Risks

## Single Topic Limitation

A single topic simplifies the current platform but may become insufficient as additional business domains are introduced.

### Mitigation

Introduce additional domain-specific topics as the platform evolves.

---

## Ordering Constraints

Ordering is guaranteed only within a partition.

### Mitigation

Use stable business identifiers as message keys where ordering is required.

---

## Future Operational Complexity

Additional topics increase operational overhead.

### Mitigation

Adopt consistent naming conventions and monitoring practices.

---

# Future Evolution

Possible future enhancements include:

- domain-based topic organization
- schema registry integration
- event versioning
- compacted topics
- dead letter queues
- multiple consumer groups
- exactly-once semantics
- multi-cluster replication

These enhancements can be introduced without changing the application's high-level architecture.

---

# Consequences

## Positive

- Simple architecture
- Easy onboarding
- Clear event routing
- Strong Spark compatibility
- Scalable design foundation

## Negative

- Single-topic architecture is intentionally simplified
- Additional topics will be required as business capabilities expand

---

# Validation

The topic strategy has been validated through:

- Kafka producer execution
- Spark Structured Streaming consumption
- Bronze layer ingestion
- Silver transformations
- Gold processing
- Runtime monitoring
- Retry framework
- Recovery framework
- End-to-end platform validation using the development dataset

Final production-scale validation will be completed using the full Instacart dataset during Sprint 15.5.

---

# References

- Apache Kafka documentation
- Spark Structured Streaming implementation
- Docker Compose configuration
- Project README
- ADR-001: Kafka Container Runtime Selection
- Sprint 5 – Kafka Foundation
- Sprint 15 – Production Readiness