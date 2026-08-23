"""
Reusable Spark Session fixture.
"""

import pytest

from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():

    spark = (

        SparkSession.builder

        .master("local[*]")

        .appName("RetailLake-Tests")

        .config(
            "spark.ui.enabled",
            "false"
        )

        .config(
            "spark.sql.shuffle.partitions",
            "1"
        )

        .getOrCreate()

    )

    yield spark

    spark.stop()