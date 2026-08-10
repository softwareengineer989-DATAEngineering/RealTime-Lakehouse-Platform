from pyspark.sql import DataFrame

from retaillake.utils.constants import (
    BRONZE_PATH,
    CHECKPOINT_LOCATION
)


def write_bronze(df: DataFrame):

    return (
        df.writeStream
        .format("delta")
        .option(
            "checkpointLocation",
            CHECKPOINT_LOCATION
        )
        .outputMode("append")
        .start(BRONZE_PATH)
    )


