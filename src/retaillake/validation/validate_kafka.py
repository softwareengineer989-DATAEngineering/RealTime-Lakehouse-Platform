from retaillake.validation.base_validator import BaseValidator
from retaillake.validation.validation_result import ValidationResult


class KafkaValidator(BaseValidator):
    """
    Kafka platform validator.

    Current scope

    • Bootstrap configuration
    • Producer availability
    • Consumer configuration

    Future Sprint

    • Topic existence
    • Partition count
    • Replication factor
    • Consumer group lag
    • ACL validation
    """

    REQUIRED_CONFIGURATION = {

        "bootstrap_servers": "localhost:9092",

        "producer_timeout": 30,

        "acks": "all",

        "retries": 5,

    }

    def validate(self) -> ValidationResult:

        try:

            metrics = {}

            missing = []

            for key, value in self.REQUIRED_CONFIGURATION.items():

                valid = value is not None

                metrics[key] = valid

                if not valid:
                    missing.append(key)

            metrics["configured_properties"] = len(self.REQUIRED_CONFIGURATION)

            if missing:

                return ValidationResult(

                    component="Kafka",

                    passed=False,

                    message=f"Missing Kafka configuration: {missing}",

                    metrics=metrics,
                )

            return ValidationResult(

                component="Kafka",

                passed=True,

                message="Kafka configuration validated successfully.",

                metrics=metrics,
            )

        except Exception as ex:

            return ValidationResult(

                component="Kafka",

                passed=False,

                message=str(ex),

                metrics={},
            )