# ADR-001: Kafka Container Selection

## Status

Accepted

## Context

The initial implementation used the Bitnami Kafka image.

During development, Bitnami moved Kafka container images from the public Docker Hub distribution to commercial OCI artifacts.

Because this project is designed as an open-source portfolio repository, requiring a commercial image would reduce reproducibility.

## Decision

Use the Confluent Platform Kafka image.

## Consequences

Advantages

- Free for development
- Enterprise adoption
- Stable Docker support
- Excellent documentation
- Compatible with Spark Structured Streaming

Trade-offs

- Slightly larger image size
- Includes Confluent-specific tooling