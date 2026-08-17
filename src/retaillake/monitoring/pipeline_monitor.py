from retaillake.monitoring.health import PlatformHealth
from retaillake.monitoring.metrics import PipelineMetrics
from retaillake.monitoring.observability import PlatformObservability

from retaillake.utils.constants import (
    BRONZE_PATH,
    SILVER_PATH,
    GOLD_PATH,
)


class PipelineMonitor:

    def __init__(self, pipeline):

        self.metrics = PipelineMetrics(
            pipeline
        )

        self.pipeline = pipeline

    def startup(self):

        PlatformObservability.startup(
            self.pipeline
        )

        self.metrics.start()

        for path in (
            BRONZE_PATH,
            SILVER_PATH,
            GOLD_PATH,
        ):

            PlatformObservability.log_health(

                PlatformHealth.check_directory(path)

            )

    def shutdown(self):

        self.metrics.finish()

        PlatformObservability.log_metrics(

            self.metrics

        )

        PlatformObservability.shutdown(

            self.pipeline

        )