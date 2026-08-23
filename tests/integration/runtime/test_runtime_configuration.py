from retaillake.configuration.environment import get_environment
from retaillake.runtime.retry_policy import RetryPolicy


def test_runtime_configuration():
    env = get_environment()

    retry = RetryPolicy()

    assert env is not None
    assert retry.max_attempts > 0