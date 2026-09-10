# Architecture Diagram Index

This directory contains the source-controlled architecture diagrams for the RealTime-Lakehouse-Platform.

The diagrams document the implemented local streaming lakehouse architecture and complement the architecture documentation.

---

# Diagram Lifecycle

Each architecture diagram exists in three forms.

```
Draw.io
     │
     ▼
Mermaid
     │
     ▼
PNG
```

The Draw.io file is the editable source.

The Mermaid file is the version-controlled text representation.

The PNG file is the rendered image used by the repository documentation.

---

# Diagram Inventory

| Diagram | Draw.io | Mermaid | PNG |
|----------|----------|----------|------|
| Platform Architecture | ✓ | ✓ | ✓ |
| Kafka Data Flow | ✓ | ✓ | ✓ |
| Streaming Pipeline | ✓ | ✓ | ✓ |
| Validation Flow | ✓ | ✓ | ✓ |
| Repository Component Map | ✓ | ✓ | ✓ |

---

# Directory Layout

```
docs/

├── diagrams/
│   ├── README.md
│   ├── platform-architecture.mmd
│   ├── kafka-flow.mmd
│   ├── streaming-sequence.mmd
│   ├── validation-flow.mmd
│   └── repository-map.mmd
│
├── diagrams-source/
│   ├── platform-architecture.drawio
│   ├── kafka-flow.drawio
│   ├── streaming-sequence.drawio
│   ├── validation-flow.drawio
│   └── repository-map.drawio
│
└── assets/
    ├── platform-architecture.png
    ├── kafka-flow.png
    ├── streaming-sequence.png
    ├── validation-flow.png
    └── repository-map.png
```

---

# Documentation References

The diagrams support the following documents.

- README.md
- ARCHITECTURE.md
- DATA_FLOW.md
- COMPONENTS.md
- Validation Runbook

---

# Version Control

Draw.io, Mermaid source, and rendered PNG images should be committed together to ensure that editable and rendered representations remain synchronized.

---

# Scope

The diagrams represent the implemented local platform only.

They intentionally avoid depicting technologies that are not part of this repository.

---

# Asset Synchronization Policy

Each architecture diagram is maintained in three synchronized representations:

1. **Draw.io (.drawio)** – authoritative editable source.
2. **Mermaid (.mmd)** – version-controlled text representation used for reviews and Git diffs.
3. **PNG (.png)** – rendered asset used by the repository documentation.

When a diagram changes:

1. Update the Draw.io source.
2. Regenerate the Mermaid representation if the logical structure changes.
3. Export a new PNG.
4. Commit all three artifacts together.

This workflow ensures the documentation remains accurate, reviewable, and easy to maintain.