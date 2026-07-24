import time

from retaillake.utils.logger import get_logger

logger = get_logger("Retry")


MAX_RETRIES = 3

BACKOFF_SECONDS = 2


def retry(func, *args, **kwargs):

    attempts = 0

    while attempts < MAX_RETRIES:

        try:

            return func(*args, **kwargs)

        except Exception as e:

            attempts += 1

            logger.warning(

                f"Retry {attempts}/{MAX_RETRIES}"

            )

            logger.error(e)

            time.sleep(BACKOFF_SECONDS)

    raise RuntimeError(

        "Maximum retries exceeded."

    )