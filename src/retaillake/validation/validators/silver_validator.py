from pyspark.sql import SparkSession

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import SILVER_PATH

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class SilverValidator(BaseValidator):

    def validate(self) -> ValidationResult:

        try:

            spark = get_spark()

            df = spark.read.format("delta").load(SILVER_PATH)

            delta_table = (
                spark.sql(
                    f"DESCRIBE DETAIL delta.`{SILVER_PATH}`"
                )
                .first()
            )

            history = spark.sql(
                f"DESCRIBE HISTORY delta.`{SILVER_PATH}`"
            )

            history_count = history.count()

            latest_history = history.first()

            metrics = {

                "table_exists": True,

                "row_count": df.count(),

                "column_count": len(df.columns),

                "schema": df.schema.simpleString(),

                "partition_columns": (
                    delta_table.asDict().get("partitionColumns", [])
                    if delta_table
                    else []
                ),

                "delta_version": (
                    latest_history["version"]
                    if latest_history is not None
                    else None
                ),

                "history_entries": history_count,

            }

            return ValidationResult(

                component="Silver",

                passed=True,

                message="Silver validation passed.",

                metrics=metrics,

            )

        except Exception as ex:

            return ValidationResult(

                component="Silver",

                passed=False,

                message=str(ex),

            )