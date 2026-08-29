from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from retaillake.spark.session.spark_session import get_spark
from retaillake.utils.constants import SILVER_PATH

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class QualityValidator(BaseValidator):

    def __init__(self):

        self.spark: SparkSession = get_spark()

    def validate(self) -> ValidationResult:

        try:

            df = (
                self.spark
                .read
                .format("delta")
                .load(SILVER_PATH)
            )

            metrics = {

                "row_count": df.count(),

                "column_count": len(df.columns),

                "duplicate_rows":
                    df.count() - df.dropDuplicates().count(),

                "null_customer_id":

                    df.filter(
                        col("customer_id").isNull()
                    ).count()

                if "customer_id" in df.columns else "N/A",

            }

            passed = (

                metrics["duplicate_rows"] == 0

                and

                metrics["null_customer_id"] == 0
                if metrics["null_customer_id"] != "N/A"
                else True

            )

            return ValidationResult(

                component="Quality",

                passed=passed,

                message="Quality validation completed.",

                metrics=metrics,

            )

        except Exception as ex:

            return ValidationResult(

                component="Quality",

                passed=False,

                message=str(ex),

            )