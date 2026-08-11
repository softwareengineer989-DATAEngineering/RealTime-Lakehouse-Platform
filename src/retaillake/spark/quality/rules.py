from pyspark.sql import DataFrame

from pyspark.sql.functions import col


REQUIRED_COLUMNS = [
    "order_id",
    "user_id",
    "order_number",
]


def validate_required_fields(
    df: DataFrame,
) -> DataFrame:

    for column in REQUIRED_COLUMNS:

        df = df.filter(
            col(column).isNotNull()
        )

    return df