from pyspark.sql import SparkSession

from retaillake.spark.session.spark_session import get_spark
from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class RuntimeValidator(BaseValidator):

    def validate(self) -> ValidationResult:

        metrics = {}

        try:

            spark = get_spark()

            metrics["spark_version"] = spark.version

            metrics["master"] = spark.sparkContext.master

            metrics["application_name"] = spark.sparkContext.appName

            metrics["python_version"] = spark.sparkContext.pythonVer

            metrics["executor_memory"] = (
                spark.sparkContext.getConf()
                .get("spark.executor.memory")
            )

            metrics["driver_memory"] = (
                spark.sparkContext.getConf()
                .get("spark.driver.memory")
            )

            return ValidationResult(

                component="Runtime",

                passed=True,

                message="Spark runtime initialized successfully.",

                metrics=metrics,

            )

        except Exception as ex:

            return ValidationResult(

                component="Runtime",

                passed=False,

                message=str(ex),

                metrics=metrics,

            )