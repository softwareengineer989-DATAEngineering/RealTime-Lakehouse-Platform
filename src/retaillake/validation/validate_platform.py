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

        ConfigurationValidator(),

        KafkaValidator(),

        BronzeValidator(),

        SilverValidator(),

        GoldValidator(),

        QualityValidator(),

    ]

    results = []

    execution_summary = []

    import time

    total_start = time.perf_counter()

    for validator in validators:

        validator_name = validator.__class__.__name__

        start = time.perf_counter()

        try:

            result = validator.validate()

        except Exception as ex:

            from retaillake.validation.validation_result import ValidationResult

            result = ValidationResult(

                component=validator_name,

                passed=False,

                message=str(ex),

                metrics={},

            )

        duration = round(

            time.perf_counter() - start,

            3,

        )

        result.metrics["execution_time_seconds"] = duration

        execution_summary.append(

            {

                "component": result.component,

                "passed": result.passed,

                "duration": duration,

            }

        )

        results.append(result)

        print("=" * 70)

        print(f"Component : {result.component}")

        print(f"PASS      : {result.passed}")

        print(f"Duration  : {duration:.3f} sec")

        print(f"Message   : {result.message}")

        print(f"Metrics   : {result.metrics}")

    total_duration = round(

        time.perf_counter() - total_start,

        3,

    )

    report_directory = Path(

        "validation_artifacts/reports"

    )

    report_directory.mkdir(

        parents=True,

        exist_ok=True,

    )

    write_report(

        results,

        report_directory,

    )

    passed = sum(

        result.passed

        for result in results

    )

    failed = len(results) - passed

    print()

    print("=" * 70)

    print("Validation Summary")

    print("=" * 70)

    print(f"Total Validators : {len(results)}")

    print(f"Passed           : {passed}")

    print(f"Failed           : {failed}")

    print(f"Duration         : {total_duration:.3f} sec")

    print(f"Reports          : {report_directory}")

    print("=" * 70)

    if failed:

        sys.exit(1)

    sys.exit(0)