from pyspark.sql import DataFrame
from pyspark.sql.functions import col


REQUIRED_COLUMNS = [
    "order_id",
    "user_id",
    "order_number",
]


def validate_required_fields(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Validate required columns.

    Removes rows containing NULL values.
    """

    for column_name in REQUIRED_COLUMNS:

        dataframe = dataframe.filter(
            col(column_name).isNotNull()
        )

    return dataframe


def validate_order_number(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Order number must be positive.
    """

    return dataframe.filter(
        col("order_number") > 0
    )


def validate_user_id(
    dataframe: DataFrame,
) -> DataFrame:
    """
    User ID must be positive.
    """

    return dataframe.filter(
        col("user_id") > 0
    )


def validate_order_id(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Order ID must be positive.
    """

    return dataframe.filter(
        col("order_id") > 0
    )