from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory
from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import BRONZE_PATH

logger = LoggerFactory.get_logger(__name__)


def create_bronze_source() -> DataFrame:
    """
    Create the Bronze Delta streaming source.
    """

    logger.info(
        "Creating Bronze Delta streaming source..."
    )

    spark = get_spark()

    return (
        spark.readStream
        .format("delta")
        .load(BRONZE_PATH)
    )