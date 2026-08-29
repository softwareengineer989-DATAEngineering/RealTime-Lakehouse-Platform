from pyspark.sql import SparkSession

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import GOLD_PATH

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class GoldValidator(BaseValidator):

    def __init__(self):

        self.spark: SparkSession = get_spark()


    def validate(self) -> ValidationResult:

        try:

            df = self.spark.read.format("delta").load(GOLD_PATH)

            metrics = {

                "row_count": df.count(),

                "columns": len(df.columns),

                "schema": df.schema.simpleString(),

            }

            return ValidationResult(

                component="Gold",

                passed=True,

                message="Gold validation passed.",

                metrics=metrics,

            )

        except Exception as ex:

            return ValidationResult(

                component="Gold",

                passed=False,

                message=str(ex),

            )