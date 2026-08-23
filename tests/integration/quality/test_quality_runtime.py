from retaillake.quality.quality_metrics import QualityMetrics
from retaillake.runtime.retry_policy import RetryPolicy


def test_quality_runtime_modules():
    metrics = QualityMetrics()

    retry = RetryPolicy()

    assert metrics is not None
    assert retry is not None