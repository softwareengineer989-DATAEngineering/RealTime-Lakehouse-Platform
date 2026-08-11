"""
Observability utilities.

Provides production
monitoring helpers.
"""

from datetime import datetime


class PlatformObservability:
    """
    Platform observability utilities.
    """

    @staticmethod
    def startup(pipeline: str):

        print()

        print("=" * 60)

        print(
            f"Pipeline Startup : {pipeline}"
        )

        print(
            f"Timestamp        : {datetime.now()}"
        )

        print("=" * 60)

        print()

    @staticmethod
    def shutdown(pipeline: str):

        print()

        print("=" * 60)

        print(
            f"Pipeline Shutdown : {pipeline}"
        )

        print(
            f"Timestamp         : {datetime.now()}"
        )

        print("=" * 60)

        print()