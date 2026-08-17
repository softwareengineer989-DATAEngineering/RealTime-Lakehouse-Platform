from retaillake.logging.logger_factory import LoggerFactory

from retaillake.spark.silver.silver_stream import create_bronze_source
from retaillake.spark.quality.validation import validate
from retaillake.spark.quality.dlq import split_valid_invalid
from retaillake.spark.silver.transformations import transform_orders
from retaillake.spark.silver.silver_writer import write_silver

logger = LoggerFactory.get_logger(__name__)


def run_silver_stream() -> None:
    """
    Enterprise Silver Streaming Pipeline.

    Bronze

        ↓

    Validation

        ↓

    Transform

        ↓

    Silver Delta
    """

    logger.info(
        "Starting Silver Streaming Pipeline..."
    )

    bronze_df = create_bronze_source()

    # Validate incoming records
    validated = validate(bronze_df)

    # Split into valid / invalid
    valid_df, invalid_df = split_valid_invalid(validated)

    logger.info(
        "Invalid records redirected to DLQ."
    )

    # Transform only valid records
    transformed = transform_orders(valid_df)

    query = write_silver(transformed)

    logger.info(
        "Silver Streaming Pipeline started."
    )

    query.awaitTermination()


if __name__ == "__main__":
    run_silver_stream()