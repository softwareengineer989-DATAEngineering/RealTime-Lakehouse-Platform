"""
Pipeline Metrics.

Tracks execution statistics
for Bronze, Silver,
and Gold pipelines.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class PipelineMetrics:

    """
    Stores pipeline execution metrics.
    """

    pipeline_name: str

    processed_records: int = 0
    invalid_records: int = 0
    failed_records: int = 0

    batches_processed: int = 0

    start_time: datetime | None = None
    end_time: datetime | None = None

    metadata: dict = field(default_factory=dict)

    def start(self):
        """Mark pipeline start."""

        self.start_time = datetime.now()

    def finish(self):
        """Mark pipeline finish."""

        self.end_time = datetime.now()

    def increment_processed(self, count: int):
        self.processed_records += count

    def increment_invalid(self, count: int):
        self.invalid_records += count

    def increment_failed(self, count: int):
        self.failed_records += count

    def increment_batch(self):
        self.batches_processed += 1

    @property
    def duration_seconds(self):

        """
        Pipeline execution duration.
        """

        if not self.start_time or not self.end_time:
            return None

        return (
            self.end_time -
            self.start_time
        ).total_seconds()

    @property
    def throughput(self):

        duration = self.duration_seconds

        if not duration:
            return 0

        return round(
            self.processed_records / duration,
            2
        )

    @property
    def success_rate(self):

        if self.processed_records == 0:
            return 100.0

        successful = (
            self.processed_records -
            self.failed_records
        )

        return round(
            successful /
            self.processed_records *
            100,
            2
        )

    def summary(self):

        return {

            "pipeline": self.pipeline_name,

            "processed": self.processed_records,

            "invalid": self.invalid_records,

            "failed": self.failed_records,

            "batches": self.batches_processed,

            "duration": self.duration_seconds,

            "throughput": self.throughput,

            "success_rate": self.success_rate

        }





