# Integration Tests

These tests validate interactions between multiple project components.

Unlike unit tests, integration tests verify that modules work correctly when used together.

Examples include:

- Spark Session + Configuration
- Runtime + Logging
- Runtime + Checkpoint Management
- Monitoring + Logger
- Spark + Runtime
- Kafka + Configuration

Integration tests should avoid external services unless explicitly required.

External dependencies (Kafka brokers, databases, cloud services) should be mocked unless the test is designed as an end-to-end validation.