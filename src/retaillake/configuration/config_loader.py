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


def load_configuration():

    app = load_yaml("application.yml")

    logger.info(
        "Loaded application.yml"
    )

    env = get_environment()

    logger.info(
        f"Active environment: {env}"
    )

    env_config = load_yaml(f"{env}.yml")

    logger.info(
        f"Loaded {env}.yml"
    )

    logger.info(
        "Configuration successfully assembled."
    )

    return {
        **app,
        **env_config,
    }