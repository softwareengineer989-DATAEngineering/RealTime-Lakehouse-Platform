"""
Quality Monitoring.
"""

from retaillake.quality.quality_metrics import (
    QualityMetrics,
)


class QualityMonitor:
    """
    Runtime Quality Monitoring.
    """

    @staticmethod
    def report(metrics: QualityMetrics):

        print()

        print("=" * 60)

        print("DATA QUALITY REPORT")

        print("=" * 60)

        print(
            f"Total Records : {metrics.total_records}"
        )

        print(
            f"Valid Records : {metrics.valid_records}"
        )

        print(
            f"Invalid Records : {metrics.invalid_records}"
        )

        print(
            f"Failed Rules : {metrics.failed_rules}"
        )

        print(
            f"Quality Score : {metrics.quality_score}%"
        )

        print("=" * 60)

        print()