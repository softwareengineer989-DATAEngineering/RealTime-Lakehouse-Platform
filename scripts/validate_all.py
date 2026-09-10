#!/usr/bin/env python3
"""
RealTime Lakehouse Platform

Validation Orchestrator

Executes all repository validation scripts
in the recommended order and prints a
single consolidated validation summary.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent

VALIDATIONS = [

    (
        "Delta Smoke Test",
        ROOT / "scripts" / "test_delta_smoke.py",
    ),

    (
        "Delta Layer Validation",
        ROOT / "scripts" / "validate_delta_layers.py",
    ),

    (
        "Delta Metadata Validation",
        ROOT / "scripts" / "validate_delta_metadata.py",
    ),

    (
        "Platform Validation",
        ROOT / "scripts" / "validate_project.py",
    ),

]


LINE = "=" * 72


def run_validation(
    name: str,
    script: Path,
) -> tuple[bool, float]:

    print()
    print(LINE)
    print(f"Running : {name}")
    print(f"Script  : {script.name}")
    print(LINE)

    if not script.exists():

        print(f"ERROR: {script.name} not found.")

        return False, 0.0

    start = time.perf_counter()

    try:

        result = subprocess.run(

            [sys.executable, str(script)],

            cwd=ROOT,

            check=False,

        )

    except Exception as ex:

        duration = time.perf_counter() - start

        print(f"ERROR: {ex}")

        return False, duration

    duration = time.perf_counter() - start

    if result.returncode == 0:

        print(f"\nPASS : {name}")
        print(f"Time : {duration:.2f} sec")

        return True, duration

    print(f"\nFAIL : {name}")
    print(f"Time : {duration:.2f} sec")

    return False, duration


def main() -> int:

    overall_start = time.perf_counter()

    print()
    print(LINE)
    print("RealTime Lakehouse Platform")
    print("Validation Orchestrator")
    print(LINE)

    results = []

    for name, script in VALIDATIONS:

        passed, duration = run_validation(

            name,

            script,

        )

        results.append(

            (

                name,

                passed,

                duration,

            )

        )

    total_duration = time.perf_counter() - overall_start

    print()
    print(LINE)
    print("Validation Summary")
    print(LINE)

    passed_count = 0

    for name, passed, duration in results:

        status = "PASS" if passed else "FAIL"

        if passed:
            passed_count += 1

        print(

            f"{status:5}"

            f"  {duration:7.2f} sec"

            f"  {name}"

        )

    failed_count = len(results) - passed_count

    print()
    print(LINE)

    print(f"Total Validators : {len(results)}")

    print(f"Passed           : {passed_count}")

    print(f"Failed           : {failed_count}")

    print(f"Total Time       : {total_duration:.2f} sec")

    print(LINE)

    if failed_count == 0:

        print()
        print("Platform validation completed successfully.")
        print()

        return 0

    print()
    print("Platform validation completed with failures.")
    print()

    return 1


if __name__ == "__main__":

    sys.exit(main())