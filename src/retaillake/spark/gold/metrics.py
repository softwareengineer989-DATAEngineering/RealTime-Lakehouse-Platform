from pyspark.sql import DataFrame
from pyspark.sql.functions import when, col


def calculate_metrics(df: DataFrame) -> DataFrame:
    """
    Adds business metrics to Gold layer.
    """

    return (
        df

        .withColumn(
            "is_repeat_customer",
            when(col("total_orders") > 1, True).otherwise(False)
        )

        .withColumn(
            "customer_order_span",
            col("last_order") - col("first_order")
        )

        .withColumn(
            "shopping_window",
            when(col("avg_order_hour") < 12, "Morning")
            .when(col("avg_order_hour") < 17, "Afternoon")
            .when(col("avg_order_hour") < 22, "Evening")
            .otherwise("Night")
        )

        .withColumn(
            "customer_segment",
            when(col("total_orders") == 1, "New Customer")
            .when(col("total_orders") <= 5, "Regular")
            .otherwise("Loyal")
        )
    )