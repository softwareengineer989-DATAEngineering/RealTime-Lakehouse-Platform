from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

from retaillake.logging.logger_factory import LoggerFactory

from retaillake.utils.constants import (
    SILVER_PATH,
    SILVER_CHECKPOINT
)

logger = LoggerFactory.get_logger(__name__)


def write_silver(
    dataframe: DataFrame
) -> StreamingQuery:
    """
    Write Silver Delta stream.
    """

    logger.info(
        f"Writing Silver stream to {SILVER_PATH}"
    )

    return (

        dataframe

        .writeStream

        .format("delta")

        .option(
            "checkpointLocation",
            SILVER_CHECKPOINT
        )

        .outputMode("append")

        .trigger(
            processingTime="10 seconds"
        )

        .start(SILVER_PATH)

    )