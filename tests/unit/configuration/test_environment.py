import pytest
import os

from retaillake.configuration.environment import get_environment


@pytest.mark.parametrize(
    "env_name",
    [
        "development",
        "testing",
        "production",
    ],
)
def test_environment_values(monkeypatch, env_name):
    monkeypatch.setenv("APP_ENV", env_name)

    assert get_environment() == env_name


def test_default_environment(monkeypatch):
    monkeypatch.delenv("APP_ENV", raising=False)

    assert get_environment() == "development"


def test_environment_custom(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")

    assert get_environment() == "production"