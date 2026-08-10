"""
Enterprise Spark configuration.
"""

SPARK_CONFIG = {

    "spark.sql.extensions":
        "io.delta.sql.DeltaSparkSessionExtension",

    "spark.sql.catalog.spark_catalog":
        "org.apache.spark.sql.delta.catalog.DeltaCatalog",

    "spark.sql.shuffle.partitions":
        "8",

    "spark.sql.adaptive.enabled":
        "true"

}