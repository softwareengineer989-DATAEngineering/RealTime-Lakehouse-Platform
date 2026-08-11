"""
Pipeline Health Checks.

Enterprise health
monitoring utilities.
"""

from pathlib import Path


class PlatformHealth:
    """
    Platform health validation.
    """

    @staticmethod
    def check_directory(path: str):

        exists = Path(path).exists()

        print(
            f"[HEALTH] {path}: {'OK' if exists else 'MISSING'}"
        )

        return exists