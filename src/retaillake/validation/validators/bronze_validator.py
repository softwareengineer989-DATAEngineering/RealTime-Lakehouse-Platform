from pyspark.sql import SparkSession

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import BRONZE_PATH

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class BronzeValidator(BaseValidator):

    def __init__(self):

        self.spark: SparkSession = get_spark()


    def validate(self) -> ValidationResult:

        try:

            df = self.spark.read.format("delta").load(BRONZE_PATH)

            delta_table = (
                self.spark.sql(
                    f"DESCRIBE DETAIL delta.`{BRONZE_PATH}`"
                )
                .first()
            )

            history = self.spark.sql(
                f"DESCRIBE HISTORY delta.`{BRONZE_PATH}`"
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

                component="Bronze",

                passed=True,

                message="Bronze validation passed.",

                metrics=metrics,

            )

        except Exception as ex:

            return ValidationResult(

                component="Bronze",

                passed=False,

                message=str(ex),

            )