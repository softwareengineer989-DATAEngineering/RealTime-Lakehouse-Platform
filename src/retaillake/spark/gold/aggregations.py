from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    count,
    avg,
    max,
    min,
    col,
)


def build_customer_metrics(df: DataFrame) -> DataFrame:
    """
    Build Gold customer-level metrics.
    """

    return (
        df.groupBy("user_id")
        .agg(
            count("*").alias("total_orders"),
            avg("order_hour_of_day").alias("avg_order_hour"),
            avg("days_since_previous_order").alias("avg_days_between_orders"),
            min("order_number").alias("first_order"),
            max("order_number").alias("last_order"),
        )
    )