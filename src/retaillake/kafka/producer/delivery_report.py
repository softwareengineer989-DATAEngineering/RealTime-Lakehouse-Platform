from retaillake.utils.logger import get_logger

logger = get_logger("Producer")


def delivery_report(err, msg):

    if err is not None:

        logger.error(
            f"Delivery failed: {err}"
        )

        return

    logger.debug(
        f"{msg.topic()} "
        f"Partition={msg.partition()} "
        f"Offset={msg.offset()}"
    )