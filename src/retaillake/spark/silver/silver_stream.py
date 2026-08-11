from pyspark.sql import DataFrame

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import BRONZE_PATH


def read_bronze_stream() -> DataFrame:
    """
    Reads the Bronze Delta table as a streaming source.
    """

    spark = get_spark()

    return (
        spark.readStream
        .format("delta")
        .load(BRONZE_PATH)
    )