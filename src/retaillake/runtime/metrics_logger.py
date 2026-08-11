"""
Structured Metrics Logger.
"""

from datetime import datetime

from retaillake.monitoring.metrics import PipelineMetrics


class MetricsLogger:
    """
    Logs pipeline execution metrics.
    """

    @staticmethod
    def log(metrics: PipelineMetrics):

        print()

        print("=" * 60)

        print(
            f"Pipeline : {metrics.pipeline_name}"
        )

        print(
            f"Processed: {metrics.processed_records}"
        )

        print(
            f"Invalid  : {metrics.invalid_records}"
        )

        print(
            f"Duration : {metrics.duration_seconds}"
        )

        print(
            f"Finished : {datetime.now()}"
        )

        print("=" * 60)

        print()