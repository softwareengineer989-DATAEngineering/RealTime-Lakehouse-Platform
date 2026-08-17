from pyspark.sql import DataFrame

from retaillake.logging.logger_factory import LoggerFactory

from retaillake.spark.session.spark_session import (
    get_spark,
)

from retaillake.utils.constants import GOLD_PATH

logger = LoggerFactory.get_logger(__name__)


def validate_gold() -> None:
    """
    Validate Gold Delta table.
    """

    spark = get_spark()

    logger.info(
        "Validating Gold Delta..."
    )

    dataframe: DataFrame = (

        spark.read

        .format("delta")

        .load(GOLD_PATH)

    )

    logger.info(
        f"Gold Records = {dataframe.count()}"
    )

    dataframe.show(
        20,
        truncate=False,
    )


if __name__ == "__main__":
    validate_gold()