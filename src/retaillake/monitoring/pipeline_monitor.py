"""
Central monitoring
entry point.
"""

from retaillake.monitoring.health import PlatformHealth

from retaillake.monitoring.observability import (
    PlatformObservability,
)

from retaillake.utils.constants import (
    BRONZE_PATH,
    SILVER_PATH,
    GOLD_PATH,
)


def initialize_pipeline(name: str):
    """
    Initialize pipeline runtime.
    """

    PlatformObservability.startup(name)

    PlatformHealth.check_directory(
        BRONZE_PATH
    )

    PlatformHealth.check_directory(
        SILVER_PATH
    )

    PlatformHealth.check_directory(
        GOLD_PATH
    )


def shutdown_pipeline(name: str):
    """
        Graceful Shutdown pipeline.
    """

    PlatformObservability.shutdown(name)


# def run_health_checks():
#     """
#     Execute platform health checks.
#     """
#
#     PlatformHealth.check_directory(BRONZE_PATH)
#
#     PlatformHealth.check_directory(SILVER_PATH)
#
#     PlatformHealth.check_directory(GOLD_PATH)