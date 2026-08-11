from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from retaillake.spark.quality.rules import validate_required_fields


def validate(df: DataFrame) -> DataFrame:
    """
    Executes all validation rules.

    Returns DataFrame with validation status.
    """

    # Existing validation rules
    df = validate_required_fields(df)

    # Enterprise validation flag
    df = (
        df.withColumn(
            "is_valid",
            (
                col("order_id").isNotNull()
                & col("user_id").isNotNull()
                & (col("order_number") > 0)
            )
        )
    )

    return df