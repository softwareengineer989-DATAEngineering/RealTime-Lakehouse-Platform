"""
Data Quality Metrics.
"""

from dataclasses import dataclass


@dataclass
class QualityMetrics:
    """
    Data Quality Metrics.
    """

    total_records: int = 0

    valid_records: int = 0

    invalid_records: int = 0

    failed_rules: int = 0

    @property
    def quality_score(self):

        if self.total_records == 0:
            return 0.0

        return round(
            (
                self.valid_records
                / self.total_records
            )
            * 100,
            2,
        )