from pathlib import Path

from retaillake.utils.constants import (
    APP_NAME,
    SPARK_APP_NAME,
    BRONZE_PATH,
    SILVER_PATH,
    GOLD_PATH,
    CHECKPOINT_LOCATION,
)

from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class ConfigurationValidator(BaseValidator):
    """
    Validates platform configuration.

    Enterprise checks:

    • Spark application configuration
    • Dataset locations
    • Checkpoint configuration
    • Required project directories
    """

    REQUIRED_PATHS = {
        "Bronze": BRONZE_PATH,
        "Silver": SILVER_PATH,
        "Gold": GOLD_PATH,
        "Checkpoint": CHECKPOINT_LOCATION,
    }

    REQUIRED_NAMES = {
        "APP_NAME": APP_NAME,
        "SPARK_APP_NAME": SPARK_APP_NAME,
    }

    def validate(self) -> ValidationResult:

        try:

            metrics = {}

            missing_names = []

            for key, value in self.REQUIRED_NAMES.items():

                if value is None or str(value).strip() == "":
                    missing_names.append(key)

            missing_paths = []

            for name, path in self.REQUIRED_PATHS.items():

                exists = Path(path).exists()

                metrics[f"{name.lower()}_exists"] = exists

                if not exists:
                    missing_paths.append(path)

            metrics["required_paths"] = len(self.REQUIRED_PATHS)

            metrics["missing_paths"] = len(missing_paths)

            metrics["configured_constants"] = len(self.REQUIRED_NAMES)

            if missing_names:

                return ValidationResult(

                    component="Configuration",

                    passed=False,

                    message=f"Missing configuration constants: {missing_names}",

                    metrics=metrics,
                )

            if missing_paths:

                return ValidationResult(

                    component="Configuration",

                    passed=False,

                    message=f"Missing directories: {missing_paths}",

                    metrics=metrics,
                )

            return ValidationResult(

                component="Configuration",

                passed=True,

                message="Platform configuration validated successfully.",

                metrics=metrics,
            )

        except Exception as ex:

            return ValidationResult(

                component="Configuration",

                passed=False,

                message=str(ex),

                metrics={},
            )