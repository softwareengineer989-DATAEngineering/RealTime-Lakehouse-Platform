# Local Development Runbook

## Purpose

This runbook provides the standard workflow for setting up, developing, testing, and validating the Real-Time Lakehouse Platform in a local development environment.

It is intended for developers, contributors, and reviewers working on the project.

---

# Supported Environment

| Component | Version |
|------------|----------|
| Operating System | Windows 10 / Windows 11 |
| Python | 3.13+ |
| Docker Desktop | Latest Stable |
| Apache Spark | Configured via Docker |
| Apache Kafka | Confluent Platform |
| Delta Lake | Current Project Version |
| Git | Latest Stable |
| PyCharm | Recommended |

---

# Initial Setup

Clone repository

```bash
git clone https://github.com/softwareengineer989-DATAEngineering/RealTime-Lakehouse-Platform.git

cd RealTime-Lakehouse-Platform
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt

pip install -r requirements-dev.txt
```

---

# Environment Configuration

Verify:

```
.env
.env.example
```

Configure:

- Kafka
- Spark
- Dataset paths
- Logging
- Runtime configuration

---

# Running the Platform

Start Docker services

```bash
docker compose up -d
```

Verify services

```bash
docker ps
```

Create Kafka topics

```powershell
scripts/create_topics.ps1
```

Load sample dataset

```bash
python scripts/load_instacart_dataset.py
```

Run producer

```bash
python src/retaillake/kafka/producer/stream_instacart.py
```

Run Bronze Stream

```bash
python src/retaillake/spark/streaming/bronze_stream.py
```

Run Silver Stream

```bash
python src/retaillake/spark/silver/run_silver_stream.py
```

Run Gold Stream

```bash
python src/retaillake/spark/gold/run_gold_stream.py
```

---

## Kafka CLI

Kafka administration commands are executed from inside the Kafka container.

Example:

docker exec kafka kafka-topics --bootstrap-server localhost:9092 --list

# Running Tests

Run all tests

```bash
pytest
```

Run coverage

```bash
pytest --cov=src
```

Run unit tests

```bash
pytest tests/unit
```

Run integration tests

```bash
pytest tests/integration
```

---



# Development Workflow

1. Create feature branch
2. Implement change
3. Execute tests
4. Validate Docker services
5. Commit changes
6. Push branch
7. Open Pull Request
8. Review CI results
9. Merge after approval

---

# Validation Checklist

- Docker healthy
- Kafka topics created
- Producer running
- Consumer running
- Bronze pipeline active
- Silver pipeline active
- Gold pipeline active
- Delta tables created
- Tests passing
- CI passing

---

# Logs

Common locations

```
logs/

docker logs

Spark logs

GitHub Actions
```

---

# Related Documentation

- [Docker Operations](docker-operations.md)
- [Kafka Operations](kafka-operations.md)
- [Spark Operations](spark-operations.md)
- [Project Overview](../../README.md)