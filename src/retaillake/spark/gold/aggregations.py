from pyspark.sql import DataFrame
from pyspark.sql.functions import (
    avg,
    count,
    max,
    min,
)

from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)


def build_customer_metrics(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Build customer-level Gold metrics.
    """

    logger.info(
        "Building customer aggregations..."
    )

    return (
        dataframe.groupBy("user_id")
        .agg(
            count("*").alias("total_orders"),
            avg("order_hour_of_day").alias("avg_order_hour"),
            avg("days_since_previous_order").alias("avg_days_between_orders"),
            min("order_number").alias("first_order"),
            max("order_number").alias("last_order"),
        )
    )