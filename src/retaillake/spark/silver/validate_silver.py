from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.spark.session.spark_session import get_spark

from retaillake.utils.constants import SILVER_PATH

logger = LoggerFactory.get_logger(__name__)


def validate_silver() -> None:
    """
    Validate Silver Delta table.
    """

    spark = get_spark()

    logger.info(
        "Validating Silver Delta..."
    )

    df: DataFrame = (
        spark.read
        .format("delta")
        .load(SILVER_PATH)
    )

    logger.info(
        f"Silver Records = {df.count()}"
    )

    df.show(
        10,
        truncate=False
    )


if __name__ == "__main__":
    validate_silver()