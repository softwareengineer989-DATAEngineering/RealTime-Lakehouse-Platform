from pyspark.sql.functions import (
    col,
    from_json
)

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.spark.schemas.order_schemas import ORDER_SCHEMA
from retaillake.spark.streaming.kafka_source import create_kafka_source
from retaillake.spark.bronze.bronze_writer import write_bronze

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

    logger.info(
        "Bronze Streaming Pipeline started."
    )

    query.awaitTermination()


if __name__ == "__main__":
    run_bronze_stream()