"""
Enterprise Retry Policy.

Reusable retry configuration shared across the platform.
"""

from dataclasses import dataclass, field


@dataclass(slots=True)
class RetryPolicy:
    """
    Defines retry behavior for transient failures.
    """

    max_attempts: int = 5

    initial_delay: float = 1.0

    multiplier: float = 2.0

    max_delay: float = 30.0

    retryable_exceptions: tuple[type[Exception], ...] = field(
        default_factory=lambda: (Exception,)
    )

    def get_delay(self, attempt: int) -> float:
        """
        Exponential backoff.

        attempt=1 -> 1 sec
        attempt=2 -> 2 sec
        attempt=3 -> 4 sec
        attempt=4 -> 8 sec
        """

        delay = self.initial_delay * (
            self.multiplier ** (attempt - 1)
        )

        return min(delay, self.max_delay)