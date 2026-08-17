from pyspark.sql import DataFrame
from pyspark.sql.functions import col

from retaillake.spark.quality.rules import (
    validate_required_fields,
    validate_order_id,
    validate_order_number,
    validate_user_id,
)


def validate(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Executes enterprise validation rules.
    """

    dataframe = validate_required_fields(dataframe)

    dataframe = validate_order_id(dataframe)

    dataframe = validate_user_id(dataframe)

    dataframe = validate_order_number(dataframe)

    dataframe = dataframe.withColumn(
        "is_valid",
        (
            col("order_id").isNotNull()
            & col("user_id").isNotNull()
            & (col("order_number") > 0)
        ),
    )

    return dataframe