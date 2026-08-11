from pyspark.sql import DataFrame

from pyspark.sql.functions import (
    col,
    lower,
    when,
)


def transform(df: DataFrame) -> DataFrame:
    """
    Enterprise Silver transformations.
    """

    return (

        df

        # Standardize eval_set values
        .withColumn(
            "eval_set",
            lower(col("eval_set"))
        )

        # Business-friendly flag
        .withColumn(
            "is_first_order",

            when(
                col("order_number") == 1,
                True
            ).otherwise(False)

        )

        # Rename for readability
        .withColumnRenamed(
            "days_since_prior_order",
            "days_since_previous_order"
        )

    )