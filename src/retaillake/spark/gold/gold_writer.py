from pyspark.sql import DataFrame

from retaillake.utils.constants import (
    GOLD_PATH,
    GOLD_CHECKPOINT,
)


def write_gold(df: DataFrame):
    """
    Persist Gold customer metrics
    into Delta Lake.
    """

    return (
        df.writeStream
        .format("delta")
        .outputMode("complete")
        .option(
            "checkpointLocation",
            GOLD_CHECKPOINT,
        )
        .start(GOLD_PATH)
    )