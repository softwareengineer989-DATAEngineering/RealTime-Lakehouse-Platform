from pyspark.sql import DataFrame

from retaillake.utils.constants import (
    SILVER_PATH,
    SILVER_CHECKPOINT,
)


def write_silver(df: DataFrame):
    """
    Persist validated Silver records to Delta Lake.
    """

    return (
        df.writeStream
        .format("delta")
        .option(
            "checkpointLocation",
            SILVER_CHECKPOINT,
        )
        .outputMode("append")
        .start(SILVER_PATH)
    )