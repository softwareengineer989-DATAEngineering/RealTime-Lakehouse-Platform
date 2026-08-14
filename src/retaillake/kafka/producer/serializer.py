import json

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def serialize(record: dict) -> bytes:
    """
    Serialize a Python dictionary into UTF-8 JSON bytes.
    """

    try:

        return json.dumps(
            record,
            ensure_ascii=False,
        ).encode("utf-8")

    except Exception as exc:

        logger.exception(
            "Record serialization failed."
        )

        raise exc