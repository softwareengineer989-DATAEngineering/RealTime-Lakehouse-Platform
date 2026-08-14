import os
from pathlib import Path

import yaml

from retaillake.configuration.environment import get_environment
from retaillake.logging.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger(__name__)

BASE_DIR = Path(__file__).resolve().parents[1]

CONFIG_DIR = BASE_DIR / "configs"


def load_yaml(filename: str):
    logger.debug(
        f"Loading YAML file: {filename}"
    )

    with open(CONFIG_DIR / filename, "r") as file:
        return yaml.safe_load(file)


def deep_merge(base: dict, override: dict) -> dict:
    """
    Recursively merge dictionaries.

    Values from override replace values from base.
    Nested dictionaries are merged rather than replaced.
    """

    merged = base.copy()

    for key, value in override.items():

        if (
            key in merged
            and isinstance(merged[key], dict)
            and isinstance(value, dict)
        ):

            merged[key] = deep_merge(
                merged[key],
                value,
            )

        else:

            merged[key] = value

    return merged


def load_configuration():

    app = load_yaml("application.yml")

    logger.info(
        "Loaded base configuration: application.yml"
    )

    env = get_environment()

    logger.info(
        "Selected configuration profile: %s",
        env,
    )

    profile_file = f"{env}.yml"

    logger.info(
        "Loading environment profile: %s",
        profile_file,
    )

    env_config = load_yaml(profile_file)

    if env_config is None:
        raise RuntimeError(
            f"Configuration profile '{profile_file}' is empty."
        )

    logger.info(
        "Successfully loaded profile: %s",
        profile_file,
    )

    logger.info(
        "Configuration successfully assembled."
    )


    merged = deep_merge(
        app,
        env_config,
    )

    logger.debug(
        "Merged configuration successfully."
    )

    return merged