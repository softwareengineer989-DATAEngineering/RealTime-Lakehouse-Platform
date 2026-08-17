import os

from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.spark.session.spark_session import get_spark

logger = LoggerFactory.get_logger(__name__)


def create_kafka_source(topic: str | None = None) -> DataFrame:
    """
    Create the enterprise Kafka Structured Streaming source.
    """

    spark = get_spark()

    bootstrap_servers = os.getenv(
        "KAFKA_BOOTSTRAP_SERVERS",
        "kafka:29092"
    )

    kafka_topic = topic or os.getenv(
        "KAFKA_TOPIC_ORDERS",
        "orders.raw"
    )

    logger.info(
        "Creating Kafka streaming source "
        f"(Topic={kafka_topic})"
    )

    return (
        spark.readStream
        .format("kafka")
        .option(
            "kafka.bootstrap.servers",
            bootstrap_servers
        )
        .option(
            "subscribe",
            kafka_topic
        )
        .option(
            "startingOffsets",
            "earliest"
        )
        .load()
    )