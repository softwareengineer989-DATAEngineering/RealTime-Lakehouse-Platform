from pyspark.sql import SparkSession

from retaillake.utils.constants import SPARK_APP_NAME
from retaillake.spark.runtime.spark_config import SPARK_CONFIG


def get_spark() -> SparkSession:
    """
    Enterprise Spark Session.

    Single SparkSession used across the platform.
    """

    builder = (
        SparkSession.builder
        .appName(SPARK_APP_NAME)
        .master("local[*]")
    )

    for key, value in SPARK_CONFIG.items():
        builder = builder.config(key, value)

    spark = builder.getOrCreate()

    spark.sparkContext.setLogLevel("WARN")

    return spark