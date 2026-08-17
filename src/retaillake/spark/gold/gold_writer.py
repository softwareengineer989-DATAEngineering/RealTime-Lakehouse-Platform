from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

from retaillake.logging.logger_factory import LoggerFactory

from retaillake.utils.constants import (
    GOLD_CHECKPOINT,
    GOLD_PATH,
)

logger = LoggerFactory.get_logger(__name__)


def write_gold(
    dataframe: DataFrame,
) -> StreamingQuery:
    """
    Write Gold Delta stream.
    """

    logger.info(
        f"Writing Gold Delta to {GOLD_PATH}"
    )

    return (

        dataframe.writeStream

        .format("delta")

        .outputMode("complete")

        .option(
            "checkpointLocation",
            GOLD_CHECKPOINT,
        )

        .trigger(
            processingTime="10 seconds"
        )

        .start(GOLD_PATH)

    )