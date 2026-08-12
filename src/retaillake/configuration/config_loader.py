from pathlib import Path

import yaml

from retaillake.configuration.environment import get_environment


BASE_DIR = Path(__file__).resolve().parents[1]

CONFIG_DIR = BASE_DIR / "configs"


def load_yaml(filename: str):

    with open(CONFIG_DIR / filename, "r") as file:
        return yaml.safe_load(file)


def load_configuration():

    app = load_yaml("application.yml")

    env = get_environment()

    env_config = load_yaml(f"{env}.yml")

    return {
        **app,
        **env_config,
    }