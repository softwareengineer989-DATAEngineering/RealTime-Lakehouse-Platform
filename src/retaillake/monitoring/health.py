"""
Pipeline Health Checks.

Enterprise health
monitoring utilities.
"""

from pathlib import Path

import shutil


class PlatformHealth:

    @staticmethod
    def check_directory(path: str):

        exists = Path(path).exists()

        return {

            "path": path,

            "status": "OK" if exists else "MISSING",

            "exists": exists

        }

    @staticmethod
    def check_disk_usage(path: str):

        usage = shutil.disk_usage(path)

        return {

            "total_gb": round(
                usage.total / (1024 ** 3),
                2
            ),

            "used_gb": round(
                usage.used / (1024 ** 3),
                2
            ),

            "free_gb": round(
                usage.free / (1024 ** 3),
                2
            )

        }

    @staticmethod
    def platform_summary(*paths):

        summary = []

        for path in paths:

            summary.append(

                PlatformHealth.check_directory(path)

            )

        return summary