from pyspark.sql import SparkSession


def test_spark_fixture(spark):
    assert isinstance(spark, SparkSession)