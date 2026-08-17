"""
Enterprise Spark Configuration.

Single source of truth for Spark runtime settings.
"""

# ---------------------------------------------------------
# SQL Configuration
# ---------------------------------------------------------

SPARK_SQL_CONFIG = {

    "spark.sql.extensions":
        "io.delta.sql.DeltaSparkSessionExtension",

    "spark.sql.catalog.spark_catalog":
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",

    "spark.sql.shuffle.partitions":
        "8",

    "spark.sql.adaptive.enabled":
        "true",

    "spark.sql.adaptive.coalescePartitions.enabled":
        "true",

    "spark.sql.session.timeZone":
        "UTC",
}


# ---------------------------------------------------------
# Runtime Configuration
# ---------------------------------------------------------

SPARK_RUNTIME_CONFIG = {

    "spark.serializer":
        "org.apache.spark.serializer.KryoSerializer",

    "spark.driver.memory":
        "2g",

    "spark.executor.memory":
        "2g",
}


# ---------------------------------------------------------
# Unified Configuration
# ---------------------------------------------------------

SPARK_CONFIG = {
    **SPARK_SQL_CONFIG,
    **SPARK_RUNTIME_CONFIG,
}