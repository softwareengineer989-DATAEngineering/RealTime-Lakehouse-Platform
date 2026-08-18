from pyspark.sql.functions import (
    col,
    from_json
)

from retaillake.spark.schemas.order_schemas import ORDER_SCHEMA
from retaillake.spark.streaming.kafka_source import create_kafka_source
from retaillake.spark.bronze.bronze_writer import write_bronze
from retaillake.runtime.shutdown import GracefulShutdown
from retaillake.runtime.signal_handler import SignalHandler

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def run_bronze_stream() -> None:
    """
    Enterprise Bronze Streaming Pipeline.

    Kafka
        ↓

    Parse JSON
        ↓

    Bronze Delta
    """

    logger.info(
        "Starting Bronze Streaming Pipeline..."
    )

    kafka_df = create_kafka_source()

    parsed = (
        kafka_df
        .selectExpr(
            "CAST(value AS STRING)"
        )
        .select(
            from_json(
                col("value"),
                ORDER_SCHEMA
            ).alias("data")
        )
        .select("data.*")
    )


    logger.info(
        "Writing Bronze Delta Stream..."
    )

    query = write_bronze(parsed)

    signal_handler = SignalHandler()

    signal_handler.register()

    shutdown_manager = GracefulShutdown()

    logger.info(
        "Bronze Streaming Pipeline started."
    )

    while query.isActive:

        query.awaitTermination(5)

        if signal_handler.shutdown_requested:
            shutdown_manager.stop_query(query)

            break


if __name__ == "__main__":
    run_bronze_stream()