from retaillake.quality.monitoring import QualityMonitor
from retaillake.quality.quality_metrics import QualityMetrics


metrics = QualityMetrics(
    total_records=1000,
    valid_records=985,
    invalid_records=15,
    failed_rules=3,
)

QualityMonitor.report(metrics)