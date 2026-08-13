
"""
Enterprise Configuration Validator

Validates platform configuration before pipeline startup.
"""
from pathlib import Path
from typing import Any
import re
from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)

SEMANTIC_VERSION_PATTERN = r"^\d+\.\d+\.\d+$"

def validate_configuration(config: dict) -> None:
    """
    Master validation function.
    """

    logger.info(
        "Starting configuration validation."
    )

    required = [

        "application.name",
        "application.version",

        "spark.app_name",

        "paths.bronze",
        "paths.silver",
        "paths.gold",

        "checkpoint.bronze",
        "checkpoint.silver",
        "checkpoint.gold",

        "kafka.topic",
        "environment.name",

    ]

    validate_required_keys(config, required)

    validate_non_empty(config, required)

    validate_types(config)

    validate_semantic_rules(config)

    validate_business_rules(config)

    validate_paths(config)

    logger.info(
        "Configuration validation completed successfully."
    )


def validate_required_keys(config: dict, required_keys: list[str]) -> None:
    """
    Validate required configuration keys exist.

    Raises:
        KeyError
    """

    missing = []

    for key in required_keys:

        current: Any = config

        for part in key.split("."):

            if isinstance(current, dict) and part in current:
                current = current[part]

            else:
                missing.append(key)
                break

    if missing:

        raise KeyError(
            f"Missing required configuration keys: {missing}"
        )

def validate_non_empty(config: dict, required_keys: list[str]) -> None:
    """
    Ensure required configuration values are not empty.
    """

    for key in required_keys:

        current = config

        for part in key.split("."):
            current = current[part]

        if current in ("", None):

            raise ValueError(
                f"Configuration '{key}' cannot be empty."
            )


# Type Validation
def validate_types(config: dict) -> None:
    """
    Validate expected configuration data types.
    """

    expected = {
        "application.name": str,
        "application.version": str,

        "spark.app_name": str,

        "kafka.topic": str,

        "environment.name": str,

        "paths.bronze": str,
        "paths.silver": str,
        "paths.gold": str,

        "checkpoint.bronze": str,
        "checkpoint.silver": str,
        "checkpoint.gold": str,
    }

    for key, expected_type in expected.items():

        current = config

        for part in key.split("."):

            if not isinstance(current, dict):
                raise KeyError(
                    f"Missing configuration section before '{part}' while validating '{key}'."
                )

            current = current.get(part)

            if current is None:
                raise KeyError(
                    f"Missing configuration key '{key}'."
                )

        if not isinstance(current, expected_type):
            raise TypeError(
                f"Configuration '{key}' should be {expected_type.__name__}."
            )


# Semantic Version Validation




def validate_semantic_rules(config: dict) -> None:
    """
    Validate semantic configuration rules.
    """

    version = config["application"]["version"]

    if not re.fullmatch(SEMANTIC_VERSION_PATTERN, version):

        raise ValueError(
            "application.version must follow semantic version format (e.g. 1.0.0)"
        )



# Business Rule Validation

def validate_business_rules(config: dict) -> None:
    """
    Validate platform business rules.
    """

    if config["paths"]["bronze"] == config["paths"]["silver"]:
        raise ValueError(
            "Invalid configuration: paths.bronze and paths.silver must not reference the same directory."
        )

    if config["paths"]["silver"] == config["paths"]["gold"]:
        raise ValueError(

            "Invalid configuration: paths.silver and paths.gold must not reference the same directory."

        )

    if config["checkpoint"]["bronze"] == config["checkpoint"]["gold"]:
        raise ValueError(

            "Invalid configuration: checkpoint.bronze and checkpoint.gold must not reference the same directory."

        )

# Filesystem Validation

def validate_paths(config: dict) -> None:
    """
    Validate configured directories exist.
    """

    directories = {

        "paths.bronze": config["paths"]["bronze"],
        "paths.silver": config["paths"]["silver"],
        "paths.gold": config["paths"]["gold"],

        "checkpoint.bronze": config["checkpoint"]["bronze"],
        "checkpoint.silver": config["checkpoint"]["silver"],
        "checkpoint.gold": config["checkpoint"]["gold"],

    }

    for name, directory in directories.items():

        if not Path(directory).exists():
            raise FileNotFoundError(

                f"{name} -> Directory does not exist: {directory}"

            )