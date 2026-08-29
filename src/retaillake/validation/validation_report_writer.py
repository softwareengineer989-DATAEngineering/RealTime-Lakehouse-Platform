import json
from pathlib import Path

from retaillake.validation.validation_result import ValidationResult


def write_report(results: list[ValidationResult], output: Path) -> None:

    report = []

    for result in results:

        report.append(
            {
                "component": result.component,
                "passed": result.passed,
                "message": result.message,
                "metrics": result.metrics,
                "timestamp": result.timestamp.isoformat(),
            }
        )

    output.parent.mkdir(parents=True, exist_ok=True)

    output.write_text(
        json.dumps(report, indent=4),
        encoding="utf-8",
    )