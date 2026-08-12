# Configuration Platform

## Overview

The Configuration Platform provides centralized configuration management for the RealTime Lakehouse Platform.

The platform supports:

- Base application configuration
- Environment-specific overrides
- Configuration validation
- Business rule validation
- Filesystem validation
- Runtime configuration loading

---

# Configuration Files

```
application.yml
development.yml
testing.yml
production.yml
```

application.yml contains shared configuration.

Environment YAML files override only environment-specific values.

---

# Configuration Loading

```
application.yml
        │
        ▼
Environment YAML
        │
        ▼
Merge
        │
        ▼
Validation Pipeline
        │
        ▼
Application Configuration
```

---

# Validation Pipeline

Configuration validation executes in the following order:

1. Required Keys
2. Non-empty Values
3. Type Validation
4. Semantic Validation
5. Business Rules
6. Filesystem Validation

The validator immediately stops when an error is detected.

---

# Validation Examples

Missing key

```
KeyError:
Missing required configuration keys
```

Empty value

```
ValueError:
Configuration cannot be empty
```

Wrong type

```
TypeError:
Expected string
```

Duplicate directories

```
ValueError:
Bronze and Silver cannot use same directory
```

Missing directory

```
FileNotFoundError:
Directory does not exist
```

---

# Running Validation

Run:

```bash
docker exec -it retail-spark \
python3 /app/src/retaillake/configuration/test_config.py
```

---

# Future Enhancements

- Pydantic models
- JSON Schema validation
- Secret Manager integration
- AWS Parameter Store
- Azure Key Vault
- Vault integration
- Configuration versioning
- Configuration hot reload