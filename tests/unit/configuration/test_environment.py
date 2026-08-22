from retaillake.configuration.environment import get_environment


def test_environment_exists():
    assert get_environment is not None