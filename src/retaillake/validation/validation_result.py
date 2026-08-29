from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass
class ValidationResult:
    """
    Standard validation result returned by every validator.
    """

    component: str

    passed: bool

    message: str

    metrics: dict[str, Any] = field(default_factory=dict)

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )