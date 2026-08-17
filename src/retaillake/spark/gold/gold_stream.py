from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory

from retaillake.spark.session.spark_session import (
    get_spark,
)

from retaillake.utils.constants import SILVER_PATH

logger = LoggerFactory.get_logger(__name__)


def create_silver_source() -> DataFrame:
    """
    Create Silver streaming source.
    """

    logger.info(
        "Creating Silver Delta source..."
    )

    spark = get_spark()

    return (

        spark.readStream

        .format("delta")

        .load(SILVER_PATH)

    )