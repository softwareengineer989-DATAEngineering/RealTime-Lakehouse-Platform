from pyspark.sql import SparkSession

from retaillake.utils.constants import SPARK_APP_NAME
from retaillake.spark.runtime.spark_config import SPARK_CONFIG

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


class SparkSessionFactory:
    """
    Enterprise Spark Session Factory.

    Responsible for creating and configuring the
    platform SparkSession.
    """

    @staticmethod
    def create() -> SparkSession:

        logger.info(
            "Creating Spark Session..."
        )

        builder = (

            SparkSession.builder
            .appName(SPARK_APP_NAME)
            .master("local[*]")

        )

        for key, value in SPARK_CONFIG.items():

            builder = builder.config(
                key,
                value,
            )

        try:

            spark = builder.getOrCreate()

        except Exception as exc:

            raise RuntimeError(
                "Failed to create SparkSession."
            ) from exc

        spark.sparkContext.setLogLevel("WARN")

        logger.info(
            "Spark Version: %s",
            spark.version,
        )

        logger.info(
            "Spark Session created successfully."
        )

        return spark


def get_spark() -> SparkSession:
    """
    Public entry point.

    Keeps backward compatibility while delegating
    session creation to SparkSessionFactory.
    """

    return SparkSessionFactory.create()