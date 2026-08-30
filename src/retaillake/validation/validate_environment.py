import os
import platform

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class EnvironmentValidator(BaseValidator):

    REQUIRED_ENVIRONMENT_VARIABLES = [

        "JAVA_HOME",

        "HADOOP_HOME",

    ]

    def validate(self) -> ValidationResult:

        metrics = {}

        missing = []

        for variable in self.REQUIRED_ENVIRONMENT_VARIABLES:

            value = os.getenv(variable)

            if value:

                metrics[variable] = value

            else:

                missing.append(variable)

        metrics["platform"] = platform.platform()

        metrics["python"] = platform.python_version()

        metrics["processor"] = platform.processor()

        metrics["docker"] = os.path.exists("/.dockerenv")

        if missing:

            return ValidationResult(

                component="Environment",

                passed=False,

                message=f"Missing environment variables: {missing}",

                metrics=metrics,

            )

        return ValidationResult(

            component="Environment",

            passed=True,

            message="Environment validated successfully.",

            metrics=metrics,

        )