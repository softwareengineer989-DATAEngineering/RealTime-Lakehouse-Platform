# ADR-0001: Adopt GitHub Actions for Continuous Integration

**Status:** Accepted

**Date:** 2026-08-24

**Sprint:** Sprint 15 – Production Readiness

---

# Context

The RealTime Lakehouse Platform consists of multiple production-oriented components including:

- Python application modules
- Kafka integration
- Spark Structured Streaming
- Delta Lake processing
- Data quality framework
- Enterprise retry framework
- Logging and monitoring utilities
- Unit and integration tests
- Repository governance documentation

As the platform evolved, validating changes manually became increasingly difficult and error-prone.

Without an automated validation pipeline:

- Regressions could reach the main branch.
- Contributors might merge code without executing tests.
- Repository quality would depend on manual verification.
- Documentation and implementation could drift over time.
- Production-readiness claims would lack automated evidence.

To align the repository with enterprise software engineering practices, an automated Continuous Integration (CI) solution was required.

---

# Problem Statement

How should the project automatically validate every code change before it is merged into the main branch?

The solution should:

- execute automatically on repository events
- install dependencies consistently
- build the project
- execute unit tests
- execute integration tests
- generate coverage reports
- fail fast on errors
- integrate naturally with GitHub Pull Requests

---

# Decision Drivers

The selected CI solution should satisfy the following requirements.

## Functional

- Automatic execution
- Python support
- PyTest integration
- Coverage reporting
- Pull Request validation
- Branch validation

## Operational

- Minimal maintenance
- Easy onboarding
- Cloud-hosted runners
- Version controlled configuration

## Portfolio

The project should demonstrate modern DevOps practices commonly expected in product engineering organizations.

---

# Options Considered

## Option 1 — Manual Validation

### Advantages

- No CI configuration
- Simple setup

### Disadvantages

- High human error
- Inconsistent execution
- Difficult to enforce
- Not production ready

Decision:

Rejected.

---

## Option 2 — Jenkins

### Advantages

- Highly customizable
- Enterprise adoption
- Extensive plugin ecosystem

### Disadvantages

- Infrastructure management required
- Increased operational overhead
- Excessive complexity for this repository

Decision:

Rejected.

---

## Option 3 — GitHub Actions

### Advantages

- Native GitHub integration
- Automatic Pull Request execution
- YAML workflow configuration
- Hosted runners
- Simple maintenance
- Excellent Python support
- Industry adoption
- Free for public repositories

### Disadvantages

- GitHub-hosted environment limits
- Workflow syntax learning curve

Decision:

Accepted.

---

# Decision

The project adopts **GitHub Actions** as the standard Continuous Integration platform.

The repository uses GitHub Actions to:

- Install Python
- Install project dependencies
- Install the package
- Compile source code
- Execute unit tests
- Execute integration tests
- Generate coverage reports
- Validate pull requests
- Validate pushes

Every Pull Request must successfully complete CI before being merged.

---

# Workflow Overview

Developer Push

↓

GitHub Actions Trigger

↓

Checkout Repository

↓

Setup Python

↓

Install Dependencies

↓

Install Project

↓

Compile Source

↓

Run Unit Tests

↓

Run Integration Tests

↓

Generate Coverage

↓

CI Result

↓

Pull Request Review

↓

Merge

---

# Repository Impact

This decision introduced:

- `.github/workflows/python-ci.yml`
- Automated testing
- Coverage generation
- Pull Request validation
- Push validation
- Repeatable build pipeline

---

# Benefits

The selected approach provides:

- Repeatable validation
- Early defect detection
- Improved code quality
- Faster feedback
- Automated regression detection
- Improved contributor experience
- Portfolio evidence of DevOps practices

---

# Risks

## Hosted Runner Availability

GitHub-hosted runners may occasionally experience queue delays.

Mitigation:

- Hosted runners are sufficient for this project.
- Self-hosted runners remain a future option.

---

## Dependency Failures

Third-party dependency updates may introduce unexpected failures.

Mitigation:

- Pin dependency versions where appropriate.
- Review Dependabot pull requests before merging.

---

## Workflow Maintenance

Workflow definitions require periodic updates.

Mitigation:

- Keep actions versions current.
- Review deprecation notices.
- Validate workflow changes through Pull Requests.

---

# Alternatives for Future Consideration

Future enterprise deployments may migrate to:

- Azure DevOps Pipelines
- GitLab CI/CD
- Jenkins
- Self-hosted GitHub Actions Runners

The current GitHub Actions implementation provides the best balance of simplicity, maintainability, and enterprise relevance for this repository.

---

# Consequences

## Positive

- Automated validation
- Higher repository quality
- Consistent testing
- Reliable pull request gating
- Improved onboarding
- Better engineering governance

## Negative

- Slightly longer Pull Request lifecycle
- Dependency on GitHub-hosted infrastructure
- Workflow maintenance over time

---

# Validation

The GitHub Actions workflow has been validated by:

- Successful dependency installation
- Successful package installation
- Successful source compilation
- Successful unit tests
- Successful integration tests
- Successful coverage generation
- Successful push validation
- Successful pull request validation

These validations establish the CI pipeline as the repository's quality gate.

---

# References

- GitHub Actions workflow (`.github/workflows/python-ci.yml`)
- Sprint 15 – Production Readiness
- Repository Testing Strategy
- Project README

---

## Related Documentation

- [Project Overview](../../README.md)
- [Project Roadmap](../ROADMAP.md)