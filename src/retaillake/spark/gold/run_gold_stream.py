from retaillake.logging.logger_factory import LoggerFactory

from retaillake.spark.gold.gold_stream import (
    create_silver_source,
)

from retaillake.spark.gold.transformations import (
    transform_gold,
)

from retaillake.spark.gold.gold_writer import (
    write_gold,
)

logger = LoggerFactory.get_logger(__name__)


def run_gold_stream() -> None:
    """
    Enterprise Gold Pipeline.
    """

    logger.info(
        "Starting Gold Streaming Pipeline..."
    )

    silver_df = create_silver_source()

    gold_df = transform_gold(
        silver_df
    )

    query = write_gold(
        gold_df
    )

    logger.info(
        "Gold Streaming Pipeline started."
    )

    query.awaitTermination()


if __name__ == "__main__":
    run_gold_stream()