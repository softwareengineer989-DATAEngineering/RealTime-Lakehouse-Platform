"""
Retry framework validation.
"""

from retaillake.runtime.retry import run_with_retry

counter = 0


def unstable_operation():

    global counter

    counter += 1

    if counter < 3:
        raise RuntimeError("Temporary failure")

    return "SUCCESS"


if __name__ == "__main__":

    result = run_with_retry(
        operation=unstable_operation,
        operation_name="Retry Test",
    )

    print(result)