from pyspark.sql import DataFrame

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import SILVER_PATH


def read_silver_stream() -> DataFrame:
    """
    Read Silver Delta as a streaming source.
    """

    spark = get_spark()

    return (
        spark.readStream
        .format("delta")
        .load(SILVER_PATH)
    )