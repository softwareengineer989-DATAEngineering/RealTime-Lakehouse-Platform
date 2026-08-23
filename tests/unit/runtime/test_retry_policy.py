import pytest
from retaillake.runtime.retry_policy import RetryPolicy


def test_retry_policy_creation():
    policy = RetryPolicy()

    assert policy is not None


def test_retry_policy_defaults():
    policy = RetryPolicy()

    assert policy.max_attempts == 5
    assert policy.initial_delay == 1.0
    assert policy.multiplier == 2.0
    assert policy.max_delay == 30.0

def test_retry_policy_custom_values():
    policy = RetryPolicy(
        max_attempts=10,
        initial_delay=2.0,
        multiplier=3.0,
        max_delay=60.0,
    )

    assert policy.max_attempts == 10
    assert policy.initial_delay == 2.0
    assert policy.multiplier == 3.0
    assert policy.max_delay == 60.0



@pytest.mark.parametrize(
    "attempts,delay,multiplier,max_delay",
    [
        (1, 0.5, 2.0, 5.0),
        (3, 1.0, 2.0, 20.0),
        (10, 5.0, 3.0, 120.0),
    ],
)
def test_retry_policy_parameterized(
    attempts,
    delay,
    multiplier,
    max_delay,
):
    policy = RetryPolicy(
        max_attempts=attempts,
        initial_delay=delay,
        multiplier=multiplier,
        max_delay=max_delay,
    )

    assert policy.max_attempts == attempts
    assert policy.initial_delay == delay
    assert policy.multiplier == multiplier
    assert policy.max_delay == max_delay