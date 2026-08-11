"""
Pipeline Metrics.

Tracks execution statistics
for Bronze, Silver,
and Gold pipelines.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class PipelineMetrics:
    """
    Stores pipeline execution metrics.
    """

    pipeline_name: str

    processed_records: int = 0

    invalid_records: int = 0

    start_time: datetime | None = None

    end_time: datetime | None = None

    def start(self):
        """Mark pipeline start."""
        self.start_time = datetime.now()

    def finish(self):
        """Mark pipeline finish."""
        self.end_time = datetime.now()

    @property
    def duration_seconds(self):
        """
        Pipeline execution duration.
        """

        if self.start_time and self.end_time:
            return (
                self.end_time - self.start_time
            ).total_seconds()

        return None