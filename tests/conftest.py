"""
Global pytest configuration.

Shared fixtures are automatically
available to every test.
"""

from pathlib import Path

import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

SRC_PATH = PROJECT_ROOT / "src"

if str(SRC_PATH) not in sys.path:
    sys.path.insert(0, str(SRC_PATH))

pytest_plugins = [
    "tests.fixtures.spark_session",
    "tests.fixtures.sample_data",
]