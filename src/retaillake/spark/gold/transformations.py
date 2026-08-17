from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory

from retaillake.spark.gold.aggregations import (
    build_customer_metrics,
)

from retaillake.spark.gold.metrics import (
    calculate_customer_metrics,
)

logger = LoggerFactory.get_logger(__name__)


def transform_gold(
    dataframe: DataFrame,
) -> DataFrame:
    """
    Gold business transformations.
    """

    logger.info(
        "Executing Gold transformations..."
    )

    dataframe = build_customer_metrics(
        dataframe
    )

    dataframe = calculate_customer_metrics(
        dataframe
    )

    return dataframe