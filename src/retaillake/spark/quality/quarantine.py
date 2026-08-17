from pyspark.sql import DataFrame
from pyspark.sql.functions import current_timestamp
from pyspark.sql.functions import lit


QUARANTINE_PATH = "/app/data/quarantine"


def quarantine_records(
    dataframe: DataFrame,
):
    """
    Persist invalid records.

    Invalid records are isolated
    from the production pipeline.
    """

    quarantine = (

        dataframe

        .withColumn(
            "pipeline",
            lit("orders")
        )

        .withColumn(
            "quarantined_at",
            current_timestamp()
        )

    )

    return (

        quarantine.writeStream

        .format("delta")

        .outputMode("append")

        .option(
            "checkpointLocation",
            "/app/data/checkpoints/quarantine",
        )

        .start(
            QUARANTINE_PATH
        )

    )