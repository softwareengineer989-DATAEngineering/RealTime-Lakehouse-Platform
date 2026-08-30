from pathlib import Path
import sys

from retaillake.validation.validation_report_writer import write_report
from retaillake.validation.validators import (
    BronzeValidator,
    SilverValidator,
    GoldValidator,
    QualityValidator,
)

from retaillake.validation.validate_runtime import RuntimeValidator

from retaillake.validation.validate_environment import EnvironmentValidator

from retaillake.validation.validate_kafka import KafkaValidator

from retaillake.validation.validate_configuration import ConfigurationValidator


def run():

    validators = [

        RuntimeValidator(),

        EnvironmentValidator(),

        BronzeValidator(),

        SilverValidator(),

        GoldValidator(),

        QualityValidator(),

        KafkaValidator(),

        ConfigurationValidator(),



    ]

    results = []

    for validator in validators:

        result = validator.validate()

        results.append(result)

        print("=" * 70)
        print(f"Component : {result.component}")
        print(f"PASS      : {result.passed}")
        print(f"Message   : {result.message}")
        print(f"Metrics   : {result.metrics}")

    report_path = Path(
        "validation_artifacts/reports/platform_validation_report.json"
    )

    write_report(
        results,
        report_path,
    )

    failed = any(
        not result.passed
        for result in results
    )

    if failed:
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    run()