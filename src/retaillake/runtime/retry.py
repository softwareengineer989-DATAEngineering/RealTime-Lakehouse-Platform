"""
Enterprise Retry Engine.

Provides reusable retry execution for transient failures.
"""

from __future__ import annotations

import time
from typing import Callable, TypeVar

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.runtime.retry_policy import RetryPolicy
from retaillake.monitoring.alert_manager import AlertManager

T = TypeVar("T")

logger = LoggerFactory.get_logger(__name__)

alerts = AlertManager()

def run_with_retry(
    operation: Callable[[], T],
    retry_policy: RetryPolicy | None = None,
    operation_name: str = "Operation",
) -> T:
    """
    Execute an operation with exponential retry.

    Raises the original exception if all retries fail.
    """

    if retry_policy is None:
        retry_policy = RetryPolicy()

    last_exception = None

    for attempt in range(
        1,
        retry_policy.max_attempts + 1,
    ):

        try:

            result = operation()

            logger.info(
                "%s succeeded on attempt %s",
                operation_name,
                attempt,
            )

            return result

        except retry_policy.retryable_exceptions as exc:

            last_exception = exc

            if attempt == retry_policy.max_attempts:

                logger.exception(
                    "%s failed after %s attempts.",
                    operation_name,
                    attempt,
                )

                alerts.error(
                    "Retry",
                    f"{operation_name} retry policy exhausted after "
                    f"{attempt} attempts."
                )

                raise

            delay = retry_policy.get_delay(
                attempt
            )

            logger.warning(
                "%s failed on attempt %s. Retrying in %.1f sec.",
                operation_name,
                attempt,
                delay,
            )

            time.sleep(delay)

    raise last_exception