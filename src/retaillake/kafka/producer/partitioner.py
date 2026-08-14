from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def get_message_key(record: dict) -> bytes:
    """
    Generate a deterministic Kafka key.

    Records for the same customer
    always reach the same partition.
    """

    if "user_id" not in record:

        raise KeyError(
            "user_id missing from record."
        )

    key = str(
        record["user_id"]
    ).encode()

    logger.debug(
        "Generated partition key."
    )

    return key