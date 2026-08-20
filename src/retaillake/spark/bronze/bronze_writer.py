from pyspark.sql import DataFrame
from pyspark.sql.streaming import StreamingQuery

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.utils.constants import (
    BRONZE_PATH,
    CHECKPOINT_LOCATION
)

logger = LoggerFactory.get_logger(__name__)


def write_bronze(
    dataframe: DataFrame
) -> StreamingQuery:
    """
    Write the Bronze Delta Streaming layer.
    """

    logger.info(
        "Writing Bronze stream "
        f"to {BRONZE_PATH}"
    )

    query = (
        dataframe
        .writeStream
        .format("delta")
        .option(
            "checkpointLocation",
            CHECKPOINT_LOCATION
        )
        .outputMode("append")
        .trigger(
            processingTime="10 seconds"
        )
        .start(BRONZE_PATH)
    )

    logger.info("Bronze Streaming Query Started")
    logger.info(f"Query ID : {query.id}")

    return query
